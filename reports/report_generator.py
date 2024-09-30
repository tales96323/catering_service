#reports/report_generator.py

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_report():
    c = canvas.Canvas("sample_report.pdf", pagesize=letter)
    c.drawString(100, 750, "Relatório de Catering Service")
    c.save()