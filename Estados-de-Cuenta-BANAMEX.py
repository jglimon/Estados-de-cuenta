import streamlit as st
import re
import pdfplumber
import csv
from io import BytesIO, StringIO

def extract_pdf_to_csv(pdf_file):
    # Open the PDF
    with pdfplumber.open(pdf_file) as pdf:
        text = ""
        # Read each page of the PDF
        for page in pdf.pages:
            # Extract the text from the page
            page_text = page.extract_text(layout=True)
            # Add the page text to the total text
            text += page_text if page_text else ""

        # Split the text into lines
        lines = text.split("\n")

        # Define the date and hour pattern
        date_pattern = r"\d{2} [A-Z]{3}"
        hour_pattern = "HORA"
        
        # Create a CSV in-memory file
        csv_output = StringIO()
        csvwriter = csv.writer(csv_output, delimiter=',')
        
        # Loop to process lines (this part needs the rest of your logic)
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
            
        # Convert the text data to bytes
        csv_data_bytes = csv_output.getvalue().encode("utf-8")
        
        # Create a CSV in-memory binary file and write the bytes
        csv_output_bytes = BytesIO()
        csv_output_bytes.write(csv_data_bytes)

        # Convert the text data to bytes
        csv_data_bytes = csv_output.getvalue().encode("utf-8")
        
        # Create a CSV in-memory binary file and write the bytes
        csv_output_bytes = BytesIO()
        csv_output_bytes.write(csv_data_bytes)
        
        # Reset pointer to the beginning of the in-memory file
        csv_output_bytes.seek(0)
        return csv_output_bytes

# Streamlit UI
st.title("PDF to CSV Converter")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    csv_data = extract_pdf_to_csv(uploaded_file)
    
    #st.write("CSV Data:")
    #st.write(csv_data.getvalue())

    st.download_button(label="Download CSV", data=csv_data, file_name="output.csv", mime="text/csv")
