import streamlit as st
from dotenv import load_dotenv
from graph.research_graph import build_graph
from tools.export_tool import PDFReport
from memory.session_memory import SessionMemory

load_dotenv()

# Use Streamlit's session_state for memory
if "memory" not in st.session_state:
    st.session_state.memory = SessionMemory()

st.title("🧠 AI Research Assistant")

query = st.text_input("🔍 Enter your research question:")

if st.button("Run Research") and query:
    graph = build_graph()
    result = graph.invoke({"input": query, "improvement_count": 0})
    st.session_state.memory.add_entry(query, result)
    st.subheader("✅ Final Report")
    st.write(result['output'])

    # Export PDF
    if st.button("Export as PDF"):
        pdf = PDFReport()
        pdf.output_report(result['output'], result.get("citations", []))
        with open("exports/research_report.pdf", "rb") as f:
            st.download_button("Download PDF", f, file_name="research_report.pdf")

# Show session history
if st.checkbox("Show session history"):
    st.subheader("Session History")
    for entry in st.session_state.memory.get_history():
        st.markdown(f"**Query:** {entry['query']}")
        st.markdown(f"**Result:** {entry['result']['output']}")
        st.markdown("---")