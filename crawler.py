import urllib.request as urllib
import re

#def close_files(a, b, c):
#    a.close()
#    b.close()
#    c.close()

def read_from_queue(file_name):
    f=open(file_name, "r")
    line = f.readline()
    while "h" not in line:
        line = f.readline()
    f.close()
    return line

def add_to_file(file, data):
    f.write("\n" + str(data))

#For removing top item from queue after it has been searched and added
def delete_top_line(file_name):
    #This method adapted from reddit user novel_yet_trivial's comment at:
    #https://www.reddit.com/r/learnpython/comments/3xuych/least_resource_intensive_way_to_delete_first_line/
    #Acessed on 11/11/2020 at 15:31
    f = open(file_name, "r+")
    f.readline()
    data = f.read()
    f.seek(0)
    f.write(data)
    f.truncate()
    f.close()

# def url_exists(url):
#     connection = httplib.HTTPConnection(url)
#     connection.request("HEAD", "")
#     if connection.getresponse().status == 200:
#         return True
#     else:
#         return False

#Check url exists and get webpage
def get_page(url):
    #Code adapted from StackOverflow user adem-Öztaş at:
    #https://stackoverflow.com/questions/16778435/python-check-if-website-exists
    #Accessed on 11/11/2020 at 16:28
    try:
        response = urllib.urlopen(url)
    except urllib.HTTPError:
        print("HTTPError")
        return ""
    except urllib.URLError:
        print("URLError")
        return ""
    html = str(response.read())
    html = remove_space(html)
    return html

def remove_space(string):
    return string.replace(" ", "")

#Use the location of a "href" to return the proceeding link
def find_link(page, start_loc):
    char = ""
    while char != '"' and char != "'":
        start_loc+=1
        char = page[start_loc]
    start_loc+=1
    end_loc = start_loc + 1
    char = ""
    while char != '"' and char != "'":
        end_loc += 1
        char = page[end_loc]
    return page[start_loc:end_loc]


def is_wiki_link(link):
    return link[:30] == 'https://en.wikipedia.org/wiki/'

#Remove first part of link to leave just the title
def get_link_title(url):
    return url[30:]

#Given a web page, return a list of all the wikipedia links found in it
def find_wiki_links(page):
    links = []
    hrefs = [m.start() for m in re.finditer('href', page)]
    for href in hrefs:
        link = find_link(page, href)
        if is_wiki_link(link):
            links.append(link)
    return links


if __name__ == "__main__":

    pages_name = "pages.txt"
    url_queue_name = "urlQueue.txt"

    while True:
        #Get next url
        current_url = read_from_queue(url_queue_name)
        #Download the html
        html = get_page(current_url)
        if html != "":
            #Scan for wiki links and add to urlQueue.txt
            links = find_wiki_links(html)
            f = open(url_queue_name, "a+")
            for link in links:
                add_to_file(f, link)
            f.close()
            #Add current page to pages.txt since it has been searched
            f = open(pages_name, "a+")
            add_to_file(f, get_link_title(current_url))
            f.close()
        #Remove current url from urlQueue.txt
        delete_top_line(url_queue_name)
