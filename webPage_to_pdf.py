#Problem:
#Either we can make the modules independent.
#or can reduce the redundancy in fetching of the content of the web page.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''This script is the web_page_to_pdf gnerator.
It takes input as a url.
Then converts each page into pdf.''

It imports:
  -create_pdf from pdf_generator, that is available in project1 package.
  -get_urls, that is available in project1 package.
  -urllib

It defines:
  -union
  -get_page
  -convert_page
  -main
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

"""Required modules"""
from pdf_generator import create_pdf
import get_urls,urllib

def union(a,b):
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ''This module combines two input lists.
    Checks for each entry in one list, if that does not exist in second
    list; it appends it to the second list.''
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print "entered union"
    for e in b:
        if e not in a:
            a.append(e)

def get_page(page):
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ''This module calls urlopen to collect the content of the input
    page from web.
    then returns that content to calling function.
    If any network error occurs and page is not fetched, it provides
    the user with suitable message.''
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print "entered get_page"
    try:
        return urllib.urlopen(page).read()
    except:
        print "There was some problem fetching the file."
        return None

def convert_page(url,name):
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ''This module takes input a url, and fetch the content from that.
    Then creates a pdf file from that content. Also returns the
    content for further operations''
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print "entered convert_page"
    page = get_page(url)                                              #fetching the content of the page.
    if page:
        create_pdf(page,name)                                         #generating pdf from the cotent. 
    return page
        
def main(url,dir_):
    print url

    converted = []
    page = convert_page(url,dir_+"/"+'homePage')                                          #converting the page into pdf.
    if page:
        links = get_urls.main(page)                                   #getting all the links form the page.
        if links:
            for entry in links:                                       #iterating over the links in the list of links.
                print entry
                if url not in converted:
                    converted.append(url)
                    if not entry.startswith("http"):
                        url = url+entry                               #the url of the locally referenced page.
                    else:
                        url = entry
                    page = convert_page(url,dir_+"/"+entry)           #converting the page
                    if page:                                          #if page was fetched.  
                        union(links,get_urls.main(page))              #union all new links from the page to old list of urls.
        else:
            print "There were no links on "+url
