import requests
from sys import argv
from bs4 import BeautifulSoup


def clean_url(url):
    if not url.endswith("/"):
        url = url + "/"

    if url.startswith("/"):
        url = url[1:]

    return url

def is_absolute(url):
    if url.startswith("http://") or url.startswith("https://"):
        return True
    else:
        return False

def get_urls(parent_url):
    parent_url = clean_url(parent_url)

    r = requests.get(parent_url)
    soup = BeautifulSoup(r.text, features="html.parser")

    child_urls = []
    for a in soup.find_all("a", href=True):
        child_url = clean_url(a["href"])
        if not is_absolute(child_url):
            child_url = parent_url + child_url
        child_urls.append(child_url)
    
    return child_urls


def search_url(depth,url):
    try:
        r = requests.get(url)
        if r.status_code not in [200, 302]:
            print("BAD LINK - {}".format(url))
            return
    except:
        print("BAD LINK - {}".format(url))
        return
    if depth > 0:
        child_urls = get_urls(url)
        for child in child_urls:
            search_url(depth-1,child)
 

if __name__ == "__main__":
    if len(argv) == 2:
        url = argv[1]
        search_url(0, url)
    elif len(argv) == 3:
        depth = argv[1]
        url = argv[2]
        if depth.startswith("-"):
            try:
                depth = int(depth[1:])
            except:
                print("Invalid value for search depth")
                exit(1)
            search_url(depth, url)
        else:
            print("Usage: find-dead-links <URL>")
            print("Usage: find-dead-links -<search depth> <URL>")
    else:
        print("Usage: find-dead-links <URL>")
        print("Usage: find-dead-links -<search depth> <URL>")

