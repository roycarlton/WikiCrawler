import urllib.request as urllib
import httplib
import re

def url_exists(url):
    connection = httplib.HTTPConnection(url)
    connection.request("HEAD", "")
    if connection.getresponse().status == 200:
        return True
    else:
        return False

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
    return 'https://en.wikipedia.org/wiki/' in link

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

    

#    response = urllib.urlopen('https://en.wikipedia.org/wiki/Wikipedia')
#    html = response.read()
#    html = remove_space(html)
#    print(html)
