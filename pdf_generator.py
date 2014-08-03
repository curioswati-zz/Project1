'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''The script is a pdf generator, as the name suggests.
It defines a function called create_pdf, that takes input
some text data and the name of output_file.
Writes the data into the output_pdf_file.''

It imports:
  -fpdf

It defines:
  -create_pdf
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

"""Required modules"""
from fpdf import FPDF

def create_pdf(data,outfile):
    print "entered create_pdf"
    
##    pdf = FPDF()
##    pdf.add_page()
##    pdf.set_font('Arial','B',16)
##    i=0
##    while True:
##        for ch in data:
##            if ch=="\n":
##                pdf.cell(40,10,"\n")
##            pdf.cell(40,10,data,'C')
##        filename = 'FILE'+str(i)+'.pdf'
##        pdf.output(filename,'F')
##        i+=1
##        break
