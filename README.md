# 🧠 AI Research Assistant

A modular, multi-agent research assistant that leverages LangGraph, LangChain, OpenAI, and Tavily to automate research, summarize findings, and export reports.  
Now with a **Streamlit UI** and **session memory** for interactive, user-friendly research workflows!

---

## 🚀 Features

- **Automated Research Pipeline:** Multi-agent workflow (Planner, Researcher, Summarizer, Critic, Presenter) orchestrated via LangGraph.
- **Web Search Integration:** Uses Tavily for up-to-date web results.
- **Summarization & Critique:** Summarizes findings and iteratively improves them.
- **PDF Export:** Generates Unicode-compatible PDF reports.
- **Session Memory:** Remembers your queries and results for the session.
- **Streamlit UI:** User-friendly web interface for research and report export.

---

## 🗂️ Project Structure

```
ai-research-assistant/
│
├── agents/                # Agent logic (planner, researcher, summarizer, critic, presenter, expert_pool)
├── graph/                 # Research workflow graph definition
├── memory/
│   └── session_memory.py  # Session memory class
├── tools/                 # Utilities (search_tools, export_tool)
│   └── fonts/ttf/         # DejaVuSans.ttf and DejaVuSans-Bold.ttf for Unicode PDF export
├── ui/
│   └── streamlit_app.py   # Streamlit UI app
├── .env                   # API keys (OpenAI, Tavily)
├── main.py                # CLI entry point
└── README.md              # This file
```

---

## 🛠️ Setup Instructions

### 1. **Clone the repository**
```sh
git clone <your-repo-url>
cd ai-research-assistant
```

### 2. **Create and activate a virtual environment**
```sh
python -m venv venv
venv\Scripts\activate   # On Windows
# Or: source venv/bin/activate   # On macOS/Linux
```

### 3. **Install dependencies**
```sh
pip install -r requirements.txt
```
If you don't have a `requirements.txt`, install manually:
```sh
pip install streamlit langchain langgraph langchain-openai langchain-community fpdf python-dotenv
```

### 4. **Add font files for Unicode PDF export**
- Download [DejaVuSans.ttf](https://dejavu-fonts.github.io/Download.html) and [DejaVuSans-Bold.ttf](https://dejavu-fonts.github.io/Download.html).
- Place them in `tools/fonts/ttf/`.

### 5. **Set up your `.env` file**
Create a `.env` file in the project root:
```
OPENAI_API_KEY=sk-...
TAVILY_API_KEY=tvly-...
```
Get your keys from [OpenAI](https://platform.openai.com/) and [Tavily](https://app.tavily.com/).

---

## 🖥️ Running the Assistant

### **A. Command Line Interface**
```sh
python main.py
```
You’ll be prompted for a research question and get a summary in the terminal. A PDF report will be generated in `exports/`.

### **B. Streamlit Web UI**
```sh
streamlit run ui/streamlit_app.py
```
- Enter your research question in the web UI.
- View results, export as PDF, and review your session history.

---

## 🧩 Session Memory

- All queries and results in a session are stored in memory (see `memory/session_memory.py`).
- In the Streamlit UI, check "Show session history" to review your research session.

---

## 📝 Customization

- **Agents:** Modify logic in `agents/` to change how each step works.
- **Graph Workflow:** Edit `graph/research_graph.py` to change the research flow or add new nodes.
- **PDF Export:** Customize formatting in `tools/export_tool.py`.
- **Session Memory:** Extend `memory/session_memory.py` for persistent or multi-user memory.

---

## 🐞 Troubleshooting

- **Streamlit not found:**  
  Make sure you activate your virtual environment and install Streamlit inside it.
- **Unicode PDF errors:**  
  Ensure you have the correct TTF font files in `tools/fonts/ttf/`.
- **API errors:**  
  Double-check your `.env` file for valid API keys.
- **Recursion errors:**  
  The graph is designed to avoid infinite loops; see `improvement_count` logic in `graph/research_graph.py`.

---

## 📦 Deployment

- Deploy on [Streamlit Cloud](https://streamlit.io/cloud), [Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=cmd%2Cbrowser), or your own server.
- For public deployment, add your `.env` secrets in the deployment platform’s UI.

---

## 📚 References

- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Documentation](https://python.langchain.com/docs/langgraph/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Tavily API](https://docs.tavily.com/)
- [FPDF Unicode Fonts](https://pyfpdf.github.io/fpdf2/fonts/index.html)

---

## 🙏 Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Streamlit](https://github.com/streamlit/streamlit)
- [Tavily](https://tavily.com/)
- [FPDF](https://pyfpdf.github.io/)

---

**Enjoy