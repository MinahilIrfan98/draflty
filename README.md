# Draftly

Draftly is an AI drafting agent that runs on a local model through Ollama. You type a request, the agent works out what you need, and it hands back a draft in a fixed, structured format. You can talk to it from the terminal, through a small web page, or by calling the API directly.

Everything runs on your own machine. No API keys, no data sent anywhere.

## How it works

![Draftly architecture](diagram.png)

A request goes in through one of three entry points: the chat loop in `main.py`, the web page in `page.tsx`, or the API endpoint in `main.py`. The entry point builds the agent and invokes it.

The agent itself lives in `agent.py` and pulls four things together:

- **Date tool** (`tools.py`): a tool the agent can call when a draft needs today's date or a relative date like "next Friday".
- **Draft schema** (`schemas.py`): the shape every response has to follow, so the output is always structured the same way.
- **Agent prompt** (`prompts.py`): the system prompt that tells the model what it is and how to write.
- **Agent middleware** (`middleware.py`): hooks that run around the model calls.

The agent talks to a local Ollama model for generation. A checkpoint store keeps conversation state between turns, so a follow-up like "make it shorter" still knows what "it" is.

## Project structure

```
draftly/
├── agent.py        # builds the agent
├── tools.py        # date tool
├── schemas.py      # draft schema
├── prompts.py      # system prompt
├── middleware.py   # agent middleware
├── main.py         # chat loop + API entrypoint
└── web/
    └── page.tsx    # web page
```

Adjust the folder names above to match your repo.

## Getting started

You need Python 3.10+, Node.js (only for the web page) and [Ollama](https://ollama.com) installed.

```bash
# pull a model
ollama pull <model-name>

# clone and install
git clone https://github.com/MinahilIrfan98/draftly.git
cd draftly
pip install -r requirements.txt
```

### Run the chat loop

```bash
python main.py
```

### Run the API

```bash
uvicorn main:app --reload
```

### Run the web page

```bash
cd web
npm install
npm run dev
```

Then open http://localhost:3000.

## Configuration

The model name and checkpoint location are set in `agent.py`. Swap in any model Ollama can serve and the rest keeps working.

## Stack

Python, Ollama, a Next.js web page (TypeScript). Agent framework: [fill in, e.g. LangChain / LangGraph].

## Author

Minahil Irfan, [github.com/MinahilIrfan98](https://github.com/MinahilIrfan98)
