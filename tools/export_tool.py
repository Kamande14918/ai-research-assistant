from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        self.set_font("DejaVu", "B", 12)
        self.cell(0, 10, "Research Report", 0 , 1, "C")
        
    def add_section(self, title, content):
        self.set_font("DejaVu", "B", 11)
        self.cell(0, 10, title, 0, 1)
        self.set_font("DejaVu", "", 10)
        self.multi_cell(0, 10, content)
        
    def output_report(self, summary, citations):
        # Add Unicode font
        self.add_font("DejaVu", "", "fonts/ttf/DejaVuSans.ttf", uni=True)
        self.add_font("DejaVu", "B", "fonts/ttf/DejaVuSans-Bold.ttf", uni=True)
        self.set_font("DejaVu", "", 10)
        self.add_page()
        self.add_section("Summary", summary)
        self.add_section("Citations", "\n".join(citations))
        self.output("exports/research_report.pdf")