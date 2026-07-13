from langgraph.graph import StateGraph,START,END
from nodes import agent_a_node,agent_b_node,agent_a_rebuttal_node,agent_b_rebuttal_node,judge
from state import DebateAgent



graph = StateGraph(DebateAgent)


graph.add_node("agent_A",agent_a_node)
graph.add_node("agent_B",agent_b_node)
graph.add_node("agent_A_Reb",agent_a_rebuttal_node)
graph.add_node("agent_B_Reb",agent_b_rebuttal_node)

graph.add_node("judge",judge)
graph.add_edge(START, "agent_A")
graph.add_edge(START, "agent_B")

graph.add_edge(
    ["agent_A", "agent_B"],
    "agent_A_Reb"
)

graph.add_edge("agent_A_Reb","agent_B_Reb")
graph.add_edge("agent_B_Reb","judge")
graph.add_edge("judge",END)

debate_graph = graph.compile()
