import nltk,urllib,pprint
from modules import create_pdf

def get_page(page):
    print "entered get_page"
    return urllib.urlopen(page).read()

def get_next_target(page):
    print "entered get_next"
    start_link = page.find('href=')
    if start_link == -1:
        return None,0
    start_quote = page.find('"',start_link+1)
    end_quote = page.find('"',start_quote+1)
    url = page[start_quote+1:end_quote]
    return url,end_quote

def get_all_links(page):
    print "entered get_all_links"
    urls = []
    while True:
        url,end_pos = get_next_target(page)
        if url:
            urls.append(url)
            page = page[end_pos:]
        else:
            break
    return urls

def extract_page(page,i):
    print "entered extract_page"
    html = get_page(page)
    create_pdf(html)
    
def union(a,b):
    print "entered union"
    for e in b:
        if e not in a:
            a.append(e)

def get_all_pages(page):
    print "entered get_all_pages"
    i=0
    extract_page(page,i)
    links = get_all_links(get_page(page))
    for entry in links:
        i+=1
        print entry
        url = page+entry
        extract_page(entry,i)
        union(links,get_all_links(get_page(entry)))
        

def create_dir(path):
    if not os.path.isdir(path):
            os.mkdir(path)
              
url = raw_input("Enter url: ")
path = raw_input("Enter the directory path in which you want to save files: ")
if url[-1] != "/":
    url+="/"
create_dir(path)
get_all_pages(url,path)
