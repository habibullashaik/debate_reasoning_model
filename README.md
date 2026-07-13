# 🧠 Debate Reasoning Pattern using LangGraph

> A beginner-friendly implementation of the **Debate Reasoning Pattern** in Agentic AI using **LangGraph** and **LLMs**.

---

## 📌 Overview

Large Language Models are powerful, but a single model may sometimes produce biased or incomplete answers.

The **Debate Reasoning Pattern** improves decision-making by allowing multiple AI agents to present different viewpoints, challenge each other's reasoning, and let an independent judge produce the final answer.

This project demonstrates that workflow in a simple, easy-to-understand way using **LangGraph**.

---

## 🎯 Objective

The goal of this project is to understand:

* How multiple AI agents collaborate
* How independent reasoning improves answer quality
* How rebuttals strengthen arguments
* How a Judge agent combines multiple perspectives
* How to build parallel multi-agent workflows using LangGraph

---

# 🏗️ Architecture

```text
                          User Question
                                │
                                ▼
                             START
                            /     \
                           ▼       ▼
                  🟦 Agent A    🟩 Agent B
                 (Opinion A)   (Opinion B)
                           │       │
                           └───┬───┘
                               ▼
                    Opening Arguments Completed
                          /               \
                         ▼                 ▼
              🟦 Agent A Rebuttal   🟩 Agent B Rebuttal
                         \                 /
                          └───────┬───────┘
                                  ▼
                           ⚖️ Judge Agent
                                  │
                                  ▼
                           Final Decision
```

---

# 🚀 Features

* ✅ Multi-Agent Debate
* ✅ Parallel Agent Execution
* ✅ Independent Argument Generation
* ✅ Rebuttal Generation
* ✅ Judge-Based Decision Making
* ✅ LangGraph Workflow
* ✅ Clean Project Structure
* ✅ Beginner Friendly

---

# 📂 Project Structure

```text
debate_reasoning_model/
│
├── main.py
├── graph.py
├── nodes.py
├── prompts.py
├── state.py
├── llm.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Workflow

### Step 1

The user asks a question.

Example:

> Should I learn Python or Java first?

---

### Step 2

Two AI agents independently generate their opinions.

**Agent A**

Supports:

> Python

**Agent B**

Supports:

> Java

Both agents execute **in parallel**.

---

### Step 3

Each agent reads the opponent's argument and generates a rebuttal.

Example:

**Agent A**

> Python is easier for beginners and has a larger AI ecosystem.

**Agent B**

> Java builds stronger programming fundamentals and is widely used in enterprise applications.

---

### Step 4

A Judge agent reviews:

* Original Question
* Agent A Argument
* Agent B Argument
* Agent A Rebuttal
* Agent B Rebuttal

Finally, the Judge produces the most balanced answer.

---

# 🧩 Agent Responsibilities

## 🟦 Agent A

* Supports Python
* Generates an opening argument
* Defends its position
* Counters Agent B

---

## 🟩 Agent B

* Supports Java
* Generates an opening argument
* Defends its position
* Counters Agent A

---

## ⚖️ Judge

* Reads every argument
* Evaluates reasoning
* Removes bias
* Produces a balanced conclusion

---

# 🔄 Debate Flow

```text
User Question
      │
      ▼
Parallel Debate
      │
      ▼
Opening Arguments
      │
      ▼
Parallel Rebuttals
      │
      ▼
Judge Evaluation
      │
      ▼
Final Answer
```

---

# 🛠️ Technologies Used

* Python
* LangGraph
* LangChain
* Groq API
* Llama 3.3
* dotenv

---

# 💡 Why Use the Debate Pattern?

Instead of relying on a single AI response, multiple agents contribute different viewpoints.

This approach helps:

* Improve reasoning quality
* Reduce hallucinations
* Encourage balanced answers
* Simulate collaborative problem solving
* Produce more reliable decisions

---

# 📈 Learning Outcomes

After completing this project, you will understand:

* Multi-Agent Systems
* Debate-Based Reasoning
* Shared State Management
* Parallel Execution in LangGraph
* Agent Communication
* Rebuttal-Based Reasoning
* Judge Pattern
* Workflow Orchestration

---

# ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/habibullashaik/debate_reasoning_model.git
```

### 2. Navigate to the project

```bash
cd debate_reasoning_model
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file.

```text
GROQ_API_KEY=your_api_key
```

### 5. Run the project

```bash
python main.py
```

---

# 📸 Example

```text
Question

Should I learn Python or Java first?

↓

Agent A
Python is easier for beginners...

↓

Agent B
Java provides stronger programming fundamentals...

↓

Agent A Rebuttal
Python also supports OOP while reducing complexity...

↓

Agent B Rebuttal
Java builds disciplined coding habits...

↓

Judge
Start with Python if you're new to programming.
Learn Java afterward to strengthen your software engineering skills.
```

---

# 🌟 Future Improvements

* Multi-round debates
* More than two debating agents
* Human-in-the-Loop review
* Tool-using agents
* Web Search integration
* Memory-enabled agents
* Debate scoring
* Streaming debate visualization
* RAG-powered evidence retrieval

---

# 🤝 Contributing

Contributions are welcome!

Feel free to fork the repository, improve the implementation, and submit a pull request.

---

# 📚 Related Concepts

* Agentic AI
* Multi-Agent Systems
* LangGraph
* Reflection Pattern
* Critic–Generator Pattern
* Reviewer–Editor Pattern
* Human-in-the-Loop
* AI Reasoning Patterns

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

It motivates me to continue building and sharing more Agentic AI reasoning patterns.

---

## 👨‍💻 Author

**Habibulla Shaik**

Building practical implementations of **Agentic AI**, **LangGraph**, **GenAI**, and **AI Reasoning Patterns** one project at a time.
