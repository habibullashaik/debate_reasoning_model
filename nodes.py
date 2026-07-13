from langchain_core.messages import HumanMessage

from llm import llm
from prompt import AGENT_A_PROMPT,AGENT_B_PROMPT,REBUTTAL_A,REBUTTAL_B,JUDGE_PROMPT


def agent_a_node(state):

    question = state["question"]

    response = llm.invoke(
        [
            HumanMessage(content=f"""{AGENT_A_PROMPT}
                        Question:
                        {question}
"""
            )
        ]
    )

    return {
        "agent_A_ans": response.content
    }

def agent_b_node(state):

    question = state["question"]

    response = llm.invoke(
        [
            HumanMessage(content=f"""{AGENT_B_PROMPT}
                        Question:
                        {question}
"""
            )
        ]
    )

    return {
        "agent_B_ans": response.content
    }



def agent_a_rebuttal_node(state):

    question = state["question"]
    agent_b_argument = state["agent_B_ans"]

    prompt = REBUTTAL_A.format(
        argument=agent_b_argument
    )

    response = llm.invoke(
        [
            HumanMessage(
                content=f"""
Question:
{question}

{prompt}
"""
            )
        ]
    )

    return {
        "agent_A_rebuttal": response.content
    }


def agent_b_rebuttal_node(state):

    question = state["question"]
    agent_a_argument = state["agent_A_ans"]

    prompt = REBUTTAL_A.format(
        argument=agent_a_argument
    )

    response = llm.invoke(
        [
            HumanMessage(
                content=f"""
Question:
{question}

{prompt}
"""
            )
        ]
    )

    return {
        "agent_B_rebuttal": response.content
    }



def judge(state):
    question = state["question"]
    agent_A_ans = state['agent_A_ans']
    agent_B_ans = state['agent_B_ans']

    agent_A_rebuttal = state['agent_A_rebuttal']
    agent_B_rebuttal = state['agent_B_rebuttal']

    prompt = JUDGE_PROMPT.format(
    question=question,
    a=agent_A_ans,
    b=agent_B_ans,
    ra=agent_A_rebuttal,
    rb=agent_B_rebuttal,
)
    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    return {
        "final_answer":response.content
    }