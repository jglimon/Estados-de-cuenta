import re
import pdfplumber
import csv

# Ruta al archivo PDF
pdf_path = "File_Path.pdf"

# Abrir el archivo PDF
with pdfplumber.open(pdf_path) as pdf:
    text = ""
    # Leer cada página del PDF
    for page in pdf.pages:
        # Extraer el texto de la página
        page_text = page.extract_text(layout=True)
        # Agregar el texto de la página al texto total
        text += page_text

# Divide el texto en líneas
lines = text.split("\n")

# Define el patrón de fecha y hora
date_pattern = r"\d{2} [A-Z]{3}"
hour_pattern = "HORA"

# Abrir el archivo output.csv para escritura
with open("File_Path.csv", 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)

    for line in lines:
        # Si la línea contiene el patrón de fecha o el patrón de hora
        if re.search(date_pattern, line) or hour_pattern in line:
            # Reemplaza los números con delimitadores antes y después
            line = re.sub(r",", "", line)
            line = re.sub(r" {9,10}", ",", line)
            #line = re.sub(r", {2}", ",,", line)

            # Split the line using commas as the delimiter
            row = line.split(",")

            # Write the row to the CSV file
            csvwriter.writerow(row)

# Imprimir el contenido del CSV en la Terminal
#with open("File_Path.csv", 'r', encoding='utf-8') as csvfile:
#    csv_content = csvfile.read()
#    print(csv_content)