from googletrans import Translator
from fpdf import FPDF


translator = Translator()

from googletrans import Translator

def translate_answer(text, target_lang):
    translator = Translator()
    return translator.translate(text, dest=target_lang).text


import os
from fpdf import FPDF

def save_to_pdf(query, answer, sources):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, f"Query: {query}\n\nAnswer:\n{answer}\n\nSources:")
    for src in sources:
        pdf.cell(0, 10, src, ln=True)

    # 🔽 Save to Desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "output.pdf")
    pdf.output(desktop_path)

    print(f"✅ PDF saved to {desktop_path}")

