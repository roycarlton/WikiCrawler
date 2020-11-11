import urllib.request as urllib
import httplib
import re

#def close_files(a, b, c):
#    a.close()
#    b.close()
#    c.close()

def read_from_queue(file_name):
    f=open(file_name, "r")
    line = f.readline()
    f.close()
    return line

def add_to_file(file_name, data):
    f = open(file_name, "a+")
    f.write("\n" + str(data))
    f.close()

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
