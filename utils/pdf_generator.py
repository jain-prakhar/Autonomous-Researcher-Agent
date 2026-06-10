from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import enums


def save_pdf(report_text, filename):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    body_style = styles["BodyText"]

    story = []

    story.append(
        Paragraph(
            "Autonomous Research Team Report",
            title_style
        )
    )

    story.append(Spacer(1, 20))

    sections = report_text.split("\n")

    for line in sections:

        if line.strip():

            story.append(
                Paragraph(
                    line.replace("\n", "<br/>"),
                    body_style
                )
            )

            story.append(
                Spacer(1, 6)
            )

    doc.build(story)

    print(f"PDF saved successfully: {filename}")