from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 40)
        self.ln(30)
        self.cell(0, 10, "CS50 Shirtificate", border=0, align="C")
        self.ln(90)

pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.image("shirtificate.png", 20, 70, 170)
pdf.set_font("helvetica", "B", 25)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 10, f"{input('Name: ').title()} took CS50", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.output("shirtificate.pdf")