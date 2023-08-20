import PyPDF2

def extract_data_from_pdf(pdf_path, sub_centre_name):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""

        header = "CoveredS.No. Name Of District Name Of Block Name Of CHC/BPHC Name Of Sub-Centre  ID No.of ASHA Name Of ASHA Husband's Name Name Of Village"

        for page_num in range(len(reader.pages)):
            page_text = reader.pages[page_num].extract_text()
            page_text = page_text.replace(header, "")
            text += page_text

        print("Extracted Text from PDF:")
        print("----------------------------")
        print(text)
        print("----------------------------")

        lines = text.split('\n')
        for line in lines:
            if sub_centre_name in line:
                columns = line.split()
                sub_centre_index = columns.index(sub_centre_name)
                
                # Search for the ID No. of ASHA (first numeric value after sub-centre name)
                for i in range(sub_centre_index + 1, len(columns)):
                    if columns[i].isdigit():
                        id_no = columns[i]
                        name_of_asha = ' '.join(columns[i+1:])
                        return id_no, name_of_asha
        return None, None

# Call the function
pdf_path = r"C:\Users\DELL\Desktop\Compiled_Balrampur_first_page.pdf"  # Replace with the path to your PDF file
sub_centre_name = "Shrinagar"  # Replace with the name of the sub-centre you want to search for
id_no, name_of_asha = extract_data_from_pdf(pdf_path, sub_centre_name)

print("ID No. of ASHA:", id_no)
print("Name Of ASHA:", name_of_asha)
