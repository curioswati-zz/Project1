from fpdf import FPDF
def create_pdf(data):
    print "Entered create_pdf"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial','B',16)
    i=0
    while True:
        for ch in data:
            if ch=="\n":
                pdf.cell(40,10,"\n")
            pdf.cell(40,10,data,'C')
        filename = 'FILE'+str(i)+'.pdf'
        pdf.output(filename,'F')
        i+=1
        break
