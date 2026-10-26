from collections import Counter
from pathlib import Path

import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas

ROOT = Path(__file__).parent
OUTPUT = ROOT / "Intelligent_Placement_System_5_Page_Evaluation.pdf"
DATA_FILE = ROOT / "Data" / "student_data_100.xlsx"

PAGE_W, PAGE_H = landscape(A4)
NAVY = colors.HexColor("#0C1E32")
INK = colors.HexColor("#182330")
TEAL = colors.HexColor("#009694")
MINT = colors.HexColor("#EAF7F5")
ORANGE = colors.HexColor("#F58F38")
SKY = colors.HexColor("#DCECF4")
MUTED = colors.HexColor("#647480")
WHITE = colors.white
RED = colors.HexColor("#B93D3D")
LIGHT = colors.HexColor("#F6F9F9")


def text(c, value, x, y, size=12, color=INK, font="Helvetica", align="left"):
    c.setFont(font, size)
    c.setFillColor(color)
    if align == "center":
        c.drawCentredString(x, y, value)
    elif align == "right":
        c.drawRightString(x, y, value)
    else:
        c.drawString(x, y, value)


def wrapped(c, value, x, y, width, size=12, leading=17, color=INK, font="Helvetica"):
    words = value.split()
    lines, line = [], ""
    for word in words:
        candidate = f"{line} {word}".strip()
        if stringWidth(candidate, font, size) <= width:
            line = candidate
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    for index, line in enumerate(lines):
        text(c, line, x, y - index * leading, size, color, font)
    return y - len(lines) * leading


def bullet_list(c, items, x, y, width, size=12, gap=26, color=INK):
    for item in items:
        c.setFillColor(ORANGE)
        c.circle(x + 4, y + 4, 3, fill=1, stroke=0)
        end_y = wrapped(c, item, x + 18, y + 8, width - 18, size, size + 4, color)
        y = min(y - gap, end_y - 7)
    return y


def rounded_card(c, x, y, w, h, title, body, accent=TEAL, body_size=10.5):
    c.setFillColor(MINT)
    c.setStrokeColor(colors.HexColor("#D7E9E7"))
    c.roundRect(x, y, w, h, 10, fill=1, stroke=1)
    c.setFillColor(accent)
    c.roundRect(x, y, 7, h, 3, fill=1, stroke=0)
    text(c, title, x + 18, y + h - 23, 13, NAVY, "Helvetica-Bold")
    wrapped(c, body, x + 18, y + h - 43, w - 32, body_size, body_size + 4, INK)


def header(c, section, title, page_no):
    c.setFillColor(WHITE)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(TEAL)
    c.rect(0, PAGE_H - 12, PAGE_W, 12, fill=1, stroke=0)
    text(c, section.upper(), 42, PAGE_H - 43, 9, TEAL, "Helvetica-Bold")
    text(c, title, 42, PAGE_H - 73, 24, NAVY, "Helvetica-Bold")
    text(c, "INTELLIGENT PLACEMENT SYSTEM  /  EVALUATION BRIEF", 42, 20, 8, MUTED, "Helvetica-Bold")
    text(c, f"0{page_no}", PAGE_W - 42, 20, 9, TEAL, "Helvetica-Bold", "right")


def arrow(c, x1, y1, x2, y2, color=ORANGE):
    c.setStrokeColor(color)
    c.setLineWidth(2)
    c.line(x1, y1, x2, y2)
    c.setFillColor(color)
    c.setStrokeColor(color)
    c.line(x2, y2, x2 - 6, y2 + 4)
    c.line(x2, y2, x2 - 6, y2 - 4)


def page_one(c):
    c.setFillColor(NAVY)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    c.setFillColor(ORANGE)
    c.rect(0, 0, 15, PAGE_H, fill=1, stroke=0)
    text(c, "MSE-1  /  ROBOTIC AGENTIC AUTOMATION", 50, PAGE_H - 53, 10, colors.HexColor("#9BE1DA"), "Helvetica-Bold")
    text(c, "Intelligent", 50, PAGE_H - 140, 40, WHITE, "Helvetica-Bold")
    text(c, "Placement System", 50, PAGE_H - 187, 40, WHITE, "Helvetica-Bold")
    wrapped(c, "From an unstructured job description to an explainable candidate shortlist.", 53, PAGE_H - 235, 430, 17, 24, colors.HexColor("#D9E8EA"))
    text(c, "AI-ASSISTED SCREENING  |  PDF + EXCEL  |  RAG + AGENTS", 53, 82, 10, colors.HexColor("#9BE1DA"), "Helvetica-Bold")
    text(c, "Evaluation presentation", 53, 55, 11, colors.HexColor("#AABDC4"))
    for i, (label, sub, accent) in enumerate([
        ("INGEST", "JD PDF", TEAL),
        ("INTERPRET", "Gemini + Pydantic", ORANGE),
        ("MATCH", "Student shortlist", colors.HexColor("#5AA5D8")),
    ]):
        y = PAGE_H - 130 - i * 92
        c.setFillColor(colors.HexColor("#17334A"))
        c.roundRect(PAGE_W - 275, y, 200, 62, 9, fill=1, stroke=0)
        c.setFillColor(accent)
        c.rect(PAGE_W - 275, y, 8, 62, fill=1, stroke=0)
        text(c, label, PAGE_W - 250, y + 36, 13, WHITE, "Helvetica-Bold")
        text(c, sub, PAGE_W - 250, y + 17, 11, colors.HexColor("#B5CBD0"))
    c.showPage()


def page_two(c):
    header(c, "01  /  Problem", "Why placement screening needs intelligence", 2)
    bullet_list(c, [
        "Job descriptions are semi-structured documents: role, responsibilities, mandatory skills, and optional skills are mixed together.",
        "Student profiles live in a separate Excel workbook, so every placement drive requires repeated manual comparison.",
        "Manual screening becomes slow, inconsistent, and difficult to audit as the number of candidates grows.",
        "The target outcome is a shortlist with a visible path from job requirement to candidate decision.",
    ], 52, PAGE_H - 135, 395, 13, 48)
    rounded_card(c, 500, 280, 230, 122, "THE INPUT REALITY", "Job Description\nPDF document\n\nStudent Database\n100 Excel records", ORANGE, 12)
    rounded_card(c, 765, 280, 230, 122, "THE DECISION", "Who is eligible?\n\nWhat skills matched?\n\nWhat should be reviewed next?", TEAL, 12)
    c.setFillColor(SKY)
    c.roundRect(500, 125, 495, 105, 10, fill=1, stroke=0)
    text(c, "SUCCESS MEASURE", 525, 195, 10, TEAL, "Helvetica-Bold")
    wrapped(c, "Reduce repetitive screening while preserving traceability from JD evidence to candidate output.", 525, 170, 435, 18, 23, NAVY, "Helvetica-Bold")
    c.showPage()


def page_three(c):
    header(c, "02  /  Architecture", "A focused RAG and agent workflow", 3)
    nodes = [
        ("JD PDF", "source", 45, TEAL),
        ("PDF Loader", "extract", 220, ORANGE),
        ("Text Splitter", "500 / 50", 395, TEAL),
        ("Embeddings", "MiniLM", 570, ORANGE),
        ("FAISS", "top-k=2", 745, TEAL),
        ("JD Agent", "Gemini", 920, ORANGE),
    ]
    y = 365
    for index, (title, sub, x, accent) in enumerate(nodes):
        c.setFillColor(MINT if accent == TEAL else colors.HexColor("#FFF2E7"))
        c.setStrokeColor(accent)
        c.roundRect(x, y, 135, 78, 10, fill=1, stroke=1)
        text(c, title, x + 67, y + 44, 12, NAVY, "Helvetica-Bold", "center")
        text(c, sub, x + 67, y + 23, 10, accent, "Helvetica-Bold", "center")
        if index < len(nodes) - 1:
            arrow(c, x + 140, y + 39, x + 166, y + 39)
    c.setFillColor(MINT)
    c.roundRect(220, 145, 270, 105, 10, fill=1, stroke=0)
    text(c, "STUDENT DATA", 245, 215, 10, TEAL, "Helvetica-Bold")
    text(c, "Excel workbook", 245, 184, 17, NAVY, "Helvetica-Bold")
    text(c, "Pandas DataFrame  /  100 rows", 245, 160, 11, INK)
    c.setFillColor(colors.HexColor("#FFF2E7"))
    c.roundRect(600, 145, 295, 105, 10, fill=1, stroke=0)
    text(c, "ELIGIBILITY AGENT", 625, 215, 10, ORANGE, "Helvetica-Bold")
    text(c, "Skill matching", 625, 184, 17, NAVY, "Helvetica-Bold")
    text(c, "Normalize -> compare -> shortlist", 625, 160, 11, INK)
    arrow(c, 490, 198, 595, 198, ORANGE)
    text(c, "RETRIEVE", 530, 222, 9, MUTED, "Helvetica-Bold", "center")
    text(c, "OUTPUT  /  EXPLAINABLE CANDIDATE SHORTLIST", PAGE_W / 2, 82, 13, NAVY, "Helvetica-Bold", "center")
    c.setStrokeColor(TEAL)
    c.setLineWidth(3)
    c.line(330, 110, 840, 110)
    c.showPage()


def page_four(c):
    header(c, "03  /  AI Solution", "What makes the prototype intelligent", 4)
    rounded_card(c, 48, 320, 285, 130, "1  /  RETRIEVAL", "The system retrieves the most relevant JD context before asking the model to interpret it. This keeps analysis grounded in the source document.", TEAL, 11)
    rounded_card(c, 365, 320, 285, 130, "2  /  STRUCTURE", "Gemini returns a validated JDRequirements object instead of loose text. Downstream code receives predictable fields.", ORANGE, 11)
    rounded_card(c, 682, 320, 285, 130, "3  /  MATCHING", "A separate eligibility agent applies a visible rule to every student skill list and returns matching records for review.", colors.HexColor("#5AA5D8"), 11)
    text(c, "STRUCTURED REQUIREMENTS", 55, 262, 10, TEAL, "Helvetica-Bold")
    fields = ["job_role", "qualification", "10th / 12th / graduation", "technical_skills", "experience"]
    x = 55
    for field in fields:
        width = 168 if field == "10th / 12th / graduation" else 142
        c.setFillColor(SKY)
        c.roundRect(x, 205, width, 32, 7, fill=1, stroke=0)
        text(c, field, x + width / 2, 216, 9.5, NAVY, "Helvetica-Bold", "center")
        x += width + 10
    c.setFillColor(colors.HexColor("#FFF2E7"))
    c.roundRect(55, 92, 912, 73, 9, fill=1, stroke=0)
    text(c, "IMPORTANT TRANSPARENCY", 78, 140, 10, RED, "Helvetica-Bold")
    wrapped(c, "The current prototype extracts academic thresholds but applies technical-skill matching only. Academic filtering, ranking, and match reasons are the next release improvements.", 78, 120, 850, 13, 18, NAVY, "Helvetica-Bold")
    c.showPage()


def page_five(c):
    header(c, "04  /  Evaluation", "Evidence, feasibility, and the next step", 5)
    students = pd.read_excel(DATA_FILE)
    counts = Counter()
    for value in students["Skills"].fillna(""):
        counts.update(skill.strip() for skill in str(value).split(",") if skill.strip())
    top = counts.most_common(5)
    max_count = max((count for _, count in top), default=1)
    text(c, f"DATA EVIDENCE  /  {len(students)} STUDENT RECORDS", 52, 430, 10, TEAL, "Helvetica-Bold")
    for index, (skill, count) in enumerate(top):
        y = 390 - index * 33
        text(c, skill, 55, y, 11, INK, "Helvetica-Bold")
        c.setFillColor(TEAL)
        c.roundRect(165, y - 3, 250 * count / max_count, 15, 5, fill=1, stroke=0)
        text(c, str(count), 430, y, 11, NAVY, "Helvetica-Bold")
    rounded_card(c, 520, 288, 215, 145, "FEASIBILITY", "Python-based\nLocal PDF + Excel inputs\nBatch-ready pipeline\nIncremental architecture", TEAL, 12)
    rounded_card(c, 765, 288, 215, 145, "NOVELTY", "RAG-grounded analysis\nTyped AI output\nAgent separation\nAuditable matching", ORANGE, 12)
    c.setFillColor(NAVY)
    c.roundRect(52, 105, 928, 105, 10, fill=1, stroke=0)
    text(c, "THE TAKEAWAY", 78, 176, 10, colors.HexColor("#9BE1DA"), "Helvetica-Bold")
    wrapped(c, "The system converts an unstructured job description and a student Excel database into a repeatable, AI-assisted, and explainable screening workflow.", 78, 151, 850, 19, 25, WHITE, "Helvetica-Bold")
    text(c, "Recommended next demo: show the JD extraction, run the shortlist, and explain one candidate decision end-to-end.", 52, 65, 11, MUTED, "Helvetica-Bold")
    c.showPage()


def build_pdf():
    pdf = canvas.Canvas(str(OUTPUT), pagesize=landscape(A4))
    pdf.setTitle("Intelligent Placement System - Evaluation Brief")
    page_one(pdf)
    page_two(pdf)
    page_three(pdf)
    page_four(pdf)
    page_five(pdf)
    pdf.save()
    print(f"Created {OUTPUT}")


if __name__ == "__main__":
    build_pdf()
