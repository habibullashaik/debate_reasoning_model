from graph import debate_graph


question = input("Enter your question: ")

for chunk in debate_graph.stream(
    {
        "question": question
    },
    stream_mode="updates"
):
    print(chunk)