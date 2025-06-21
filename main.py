from dotenv import load_dotenv
import os
from graph.research_graph import build_graph
from tools.export_tool import PDFReport

load_dotenv()
print("TAVILY_API_KEY:", os.getenv("TAVILY_API_KEY"))  # Debug: Should print your key (or at least not None)

def main():
    query = input("🔍 Enter your search question: ")
    graph = build_graph()
    # Initialize improvement_count to 0
    result = graph.invoke({"input": query, "improvement_count": 0})
    print("\n✅ Final Report:\n")
    print(result['output'])
    
    # Export
    pdf = PDFReport()
    pdf.output_report(result['output'], result.get("citations", []))
    
if __name__ == "__main__":
    main()