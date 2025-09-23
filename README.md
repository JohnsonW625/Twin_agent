# Johnson's CrewAI Twin — Homework Example 🚀

A compact example multi-agent project that demonstrates how to build two cooperating agents:
- a twin "research" agent that answers questions on behalf of Johnson using a local `information.txt` file 📄
- a writer agent that converts the twin's draft reply into a polished, formal first-person message and saves it to disk ✍️

This repository is intended as a homework/example project showing agent roles, tasks, and tool usage with `crewai` and `crewai_tools`.

---

## Contents 📁
- `main.py` — example agent definitions and a small runner
- `information.txt` — Johnson Wang's background used by the twin agent
- `requirements.txt` — Python dependencies


## Quick overview 🔍
1. Run the program and enter a question for Johnson.
2. The twin agent reads `information.txt` and drafts a short first-person reply.
3. The writer agent formalizes the draft and saves the reply to `johnson_reply.md`.

## Requirements 📦
- Python 3.8+
- See `requirements.txt` for package versions. The project expects `crewai` and `crewai[tools]` to be available.

## Setup (recommended) 🛠️
1. Make the setup script executable and run it (zsh / macOS):

```bash
pip install -r requirements.txt
```

2. Set your OpenAI API key (required for real runs):

```bash
export OPENAI_API_KEY="sk-..."
```

- Optional (web search):

```bash
export SERPER_API_KEY="serper-..."
```

## Usage ▶️
Run the main script:

```bash
python main.py
```

The script will prompt for a question. If the agents successfully use the file tool, the final reply will be saved to `johnson_reply.md`.

## Agents & Tasks 🤖
- Twin agent (`create_twin_agent`):
  - Role: represent Johnson's persona and knowledge
  - Tools: `FileReadTool` pointing to `information.txt`
  - Task: read `information.txt` and draft a short first-person answer + support notes

- Writer agent (`create_writer_agent`):
  - Role: take the twin draft and produce a formal, concise first-person reply
  - Tools: `FileWriterTool` to save the final reply

Key task functions:
- `create_johnson_response_task(agent, question)` — instructs the twin to answer the question using local info
- `create_writing_task(agent)` — instructs the writer to formalize and save the reply


## Example 🤖
Tell me about LoRA and your expeirence in LoRA

✅ Crew execution completed!
==================================================
📄 Final Result:
At Harvard, I apply LoRA-based fine-tuning in conjunction with retrieval-augmented generation (RAG) to medical QA and explore multimodal models using a VLM+Adapter setup for efficient, domain-specific tagging. This approach leverages my strong foundation in biology, mathematics, and computer science to enable rigorous, scalable experimentation on bio/medical and multimodal AI problems. By combining these techniques, I aim to improve accuracy while avoiding full-model retraining.


## What Worked 
- 🎉 Successfully installed CrewAI and set up project structure
- 🔧 Create reproducible results

## ❌ What Didn't Work
- 💳 Initial OpenAI API charge
- 📋 Dependencies conflict(solved by using virtual envrionment)

## 🎓 What I Learned
- 🧠 How to structure CrewAI agents with personal knowledge and expertise
- 👤 How to orchestrate a crew






