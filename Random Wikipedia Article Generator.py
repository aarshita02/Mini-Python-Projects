import requests
# Requests is a simple, yet elegant HTTP library.
from bs4 import BeautifulSoup
# Beautiful Soup is a library that makes it easy to scrape information from web pages.
# It sits atop an HTML or XML parser,providing Python idioms for iterating, searching, and modifying the parse tree.
import webbrowser

while True:
    url = requests.get('https://en.wikipedia.org/wiki/Special:Random')
    soup = BeautifulSoup(url.content, "html.parser")
    # url.content accepts the raw content
    # html.parser is the way of telling BeautifulSoup that it is an HTML document, others include XML etc

    title = soup.find(class_="firstHeading").text
    # When you check the source code of any wikipedia page you'll notice the heading is placed in this class

    print(f"{title} \nDo you want to view it? (Y/N)")
    ans = input("").lower()
    if ans == "y":
        url = f"https://en.wikipedia.org/wiki/{title}"
        webbrowser.open(url)
        break
    elif ans == "n":
        print("Try again!")
        continue
    else:
        print("Wrong choice!")
        break
