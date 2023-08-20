from flask import Flask, render_template, request
import PyPDF2

app = Flask(__name__)

def extract_data_from_pdf(pdf_path, sub_centre_name):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""

        header = "CoveredS.No. Name Of District Name Of Block Name Of CHC/BPHC Name Of Sub-Centre  ID No.of ASHA Name Of ASHA Husband's Name Name Of Village"

        for page_num in range(len(reader.pages)):
            page_text = reader.pages[page_num].extract_text()
            page_text = page_text.replace(header, "")
            text += page_text

        results = []
        lines = text.split('\n')
        for line in lines:
            if sub_centre_name in line:
                columns = line.split()
                if sub_centre_name in columns:
                    sub_centre_index = columns.index(sub_centre_name)
                    for i in range(sub_centre_index + 1, len(columns)):
                        if columns[i].isdigit():
                            id_no = columns[i]
                            name_of_asha = ' '.join(columns[i+1:])
                            results.append((id_no, name_of_asha))
                            break
        return results

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        sub_centre_name = request.form['sub_centre_name']
        pdf_path = r"C:\Users\DELL\Desktop\Compiled_Balrampur_first_page.pdf"
        results = extract_data_from_pdf(pdf_path, sub_centre_name)
    return render_template('index2.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
