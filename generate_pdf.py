from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Congratulations!", ln=True, align='C')
pdf.cell(200, 10, txt="You have successfully completed the CTF challenge.", ln=True, align='C')
pdf.cell(200, 10, txt="COMMIT KAAVIYAM - Final Round", ln=True, align='C')
pdf.cell(200, 10, txt="Flag: vault{FOSSUNITED}", ln=True, align='C')
pdf.output("assets/certificate.pdf")