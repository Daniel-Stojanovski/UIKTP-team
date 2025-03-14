# # import sys
# # from fpdf import FPDF
# # import os
# #
# # # Get values from command-line arguments
# # theme = sys.argv[1]
# # difficulty = sys.argv[2]
# # question = sys.argv[3]
# # equation = sys.argv[4]
# #
# # # Create the PDF
# # pdf = FPDF()
# # pdf.add_page()
# # pdf.set_font("Arial", size=12)
# #
# # pdf.cell(200, 10, f"Theme: {theme}, Difficulty: {difficulty}", ln=True)
# # pdf.set_font("Arial", size=16)
# # pdf.cell(200, 10, "QUESTION:", ln=True)
# # pdf.multi_cell(0, 10, question)
# # pdf.set_font("Arial", size=14)
# # pdf.cell(200, 10, equation, ln=True)
# #
# # # Save PDF to 'exports/' folder
# # os.makedirs("exports", exist_ok=True)
# # pdf.output(f"exports/problem_{theme}_{difficulty}.pdf")
# #
# # print("PDF Exported!")
#
# import sys
# from docx import Document
# import os
#
# # Get values from command-line arguments
# theme = sys.argv[1]
# difficulty = sys.argv[2]
# question = sys.argv[3]
# equation = sys.argv[4]
#
# # Create a new Document
# doc = Document()
#
# # Add the theme and difficulty as the title
# doc.add_heading(f"Theme: {theme}, Difficulty: {difficulty}", level=1)
#
# # Add the question section
# doc.add_heading("QUESTION:", level=2)
# doc.add_paragraph(question)
#
# # Add the equation section
# doc.add_heading("Equation:", level=2)
# doc.add_paragraph(equation)
#
# # Save the document to 'exports/' folder
# os.makedirs("exports", exist_ok=True)
# doc.save(f"exports/problem_{theme}_{difficulty}.docx")
#
# print("DOCX Exported!")

import sys
import os

# Get values from command-line arguments
theme = sys.argv[1]
difficulty = sys.argv[2]
question = sys.argv[3]
equation = sys.argv[4]

# Create the content for the text file
content = f"Theme: {theme}, Difficulty: {difficulty}\n\n"
content += "QUESTION:\n"
content += f"{question}\n\n"
content += f"Equation:\n{equation}\n"

# Save to a text file in the 'exports/' folder
os.makedirs("exports", exist_ok=True)
file_path = f"exports/problem_{theme}_{difficulty}.txt"

with open(file_path, "w") as file:
    file.write(content)

print("TXT Exported!")
