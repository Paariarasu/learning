import fitz
import calendar
import sys


def generate_calendar_pdf(start_year):
    if start_year is None:
        raise ValueError("Start year is required as a command-line argument.")

    if not str(start_year).isdigit() or start_year <= 0:
        raise ValueError("Year must be a positive numeric value.")

    doc = fitz.open()
    cal = calendar.LocaleTextCalendar(locale="de")
    w, h = fitz.PaperSize("a4-l")

    for i in range(3):
        txt = cal.formatyear(start_year + i, m=4)
        doc.insertPage(-1, txt, fontsize=12, fontname="Courier", width=w, height=h)

    doc.save("Calendar.pdf", garbage=4, deflate=True)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <start_year>")
        sys.exit(1)

    try:
        start_year = int(sys.argv[1])
        generate_calendar_pdf(start_year)
        print("Calendar PDF generated successfully.")
    except ValueError as e:
        print(f"Error: {e}")
