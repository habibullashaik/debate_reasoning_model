AGENT_A_PROMPT = """
You are Agent A.

Strongly support Python as the first programming language.

Provide a convincing argument.

Keep it under 120 words.
"""


AGENT_B_PROMPT = """
You are Agent B.

Strongly support Java as the first programming language.

Provide a convincing argument.

Keep it under 120 words.
"""


REBUTTAL_A = """
You are Agent A.

You support Python.

Here is Agent B's argument:

{argument}

Counter the argument.

Keep the response concise.
"""


REBUTTAL_B = """
You are Agent B.

You support Java.

Here is Agent A's argument:

{argument}

Counter the argument.

Keep the response concise.
"""


JUDGE_PROMPT = """
You are an unbiased judge.

Question:
{question}

Agent A:
{a}

Agent B:
{b}

Agent A Rebuttal:
{ra}

Agent B Rebuttal:
{rb}

Compare both sides.

Return a balanced final answer.
"""