from fpdf import FPDF

COLUMNS = 80
FONT_SIZE = 12
LINE_HEIGHT = 5


def wrap_lines(text, columns=COLUMNS):
    lines = []
    for raw in text.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        raw = raw.expandtabs(4)
        if raw == "":
            lines.append("")
            continue
        for i in range(0, len(raw), columns):
            lines.append(raw[i:i + columns])
    return lines

def convert(text, font_path):
    pdf = FPDF(format="A4")
    pdf.set_margins(15, 15, 15)
    pdf.add_font("Custom", fname=font_path)
    pdf.add_page()
    pdf.set_font("Custom", size=FONT_SIZE)
    for line in wrap_lines(text):
        pdf.cell(0, LINE_HEIGHT, line, new_x="LMARGIN", new_y="NEXT")
    return bytes(pdf.output())