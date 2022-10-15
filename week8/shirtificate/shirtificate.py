from fpdf import FPDF


name = input("Name: ")



pdf = FPDF(orientation="portrait", format="A4")
pdf.add_page()
pdf.set_font("Helvetica", size=60)
pdf.text(25, 50, "CS50 Shirtificate")
pdf.image("shirtificate.png", x=10, y=70, w=pdf.epw)
pdf.set_font("Helvetica", size=30)
pdf.set_text_color(255,255,255)
pdf.text(65, 140, f"{name} took CS50")
#pdf.image("shirtificate.png", x=10, y=70, w=pdf.epw)
pdf.output("shirtificate.pdf")