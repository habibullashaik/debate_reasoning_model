from typing_extensions import TypedDict


class DebateAgent(TypedDict):
    question:str
    agent_A_ans:str
    agent_B_ans:str

    agent_A_rebuttal:str
    agent_B_rebuttal:str

    final_answer:str
