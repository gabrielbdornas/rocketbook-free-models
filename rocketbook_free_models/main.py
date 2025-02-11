from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

input_path = "input.pdf"
output_path = "output.pdf"



reader = PdfReader(input_path)
writer = PdfWriter()

for page in reader.pages:
    new_page = writer.add_blank_page(width=842, height=595)  # A4 em paisagem

    new_page.merge_page(page, (0, 0))  # Copia a página original na esquerda
    new_page.merge_page(page, (421, 0))  # Copia a página original na direita

with open(output_path, "wb") as f:
    writer.write(f)

print(f"Arquivo salvo como {output_path}")
