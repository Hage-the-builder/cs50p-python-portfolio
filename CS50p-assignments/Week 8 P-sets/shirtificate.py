import sys
from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        # Set up a title header matching layout requirements
        self.set_font("Helvetica", "B", 45)
        self.cell(0, 50, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")


def main():
    name = input("Name: ")

    # Initialize portrait, A4 layout PDF
    pdf = Shirtificate(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Draw the background shirt image centered on the page
    pdf.image("shirtificate.png", x=15, y=70, w=180)

    # Configure font specifications and color overlay for the name text
    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255) # Clear white text

    # Move coordinates down to place text in the center-chest region of the shirt image
    pdf.set_y(130)
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    # Export and save
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
