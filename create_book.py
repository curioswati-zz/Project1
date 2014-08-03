'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''Module for creating a pdf book from ebook.

This script is a web book to pdf gnerator.
It takes input from user, the url of the home page of the book.
Also the directory name, where to save the files.

It imports:
  -os module
  -webPage_to_pdf module, that is present in the project1 package.
It defines:
  -a main function
  -a create_dir function
''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

"""Required modules"""
import webPage_to_pdf, os
            
def main():              
    url = raw_input("Enter url: ")
    path = raw_input("Enter the directory path in which you want to save files: ")

    if url:
        if url[-1] != "/":
            url+="/"
        if path and not os.path.isdir(path):
            os.mkdir(path)
        else:
            path = './'
        webPage_to_pdf.main(url,path)            
    else:
        print "Please enter the url."
