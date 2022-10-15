import requests
from bs4 import BeautifulSoup
import re
import csv
import sys
from os.path import exists
from tabulate import tabulate



def main():
    if not load_content("https://docs.python.org/3/tutorial/index.html"):
        sys.exit("Something went wrong. Try again later.")
    
    l = len(sys.argv)

    if l != 2:
        sys.exit("Usage: python project.py search-keyword")
    
    results = search_content(sys.argv[1].strip().lower())
    if not results:
        sys.exit("Sorry, We couldn't find anything. Try using a different keyword.")
    
    print(tabulate(results, headers="keys", tablefmt='grid'))


def search_content(topic=None):
    try:
        csvfile = open('./pyhon.csv')
    except:
        return None
    
    results = []
    reader = csv.DictReader(csvfile)
    for row in reader:
        if topic in row["title"].lower() or topic in row["link"].lower():
            results.append(row)
        
    csvfile.close()

    if results == []:
        return None
    else:
        return results



def load_content(url):
    try:
        page = requests.get(url)
    except:
        return False
    
    if page.ok:
        if exists("./pyhon.csv"):
            return True
        soup = BeautifulSoup(page.content, "html.parser")
        data = parse_content(soup)
        if write_content(data):
            return True
            
    return False


def write_content(data):
    try:
        csvfile = open('pyhon.csv', 'w')
    except:
        return False
    else:
        fieldnames = ['number', 'title', 'link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)
        csvfile.close()
        return True
    


def parse_content(soup):
    data = []
    links = soup.find_all('div', class_="toctree-wrapper")
    for link in links:
        topics = link.ul.find_all('li')
        for topic in topics:
            number, title = parse_topic(topic.a.text)
            if number and title:
                data.append({
                    "number": number,
                    "title": title,
                    "link": f"https://docs.python.org/3/tutorial/{topic.a.get('href')}"
                })
    
    return data


def parse_topic(topic):
    if matches := re.match(r"^(.+\.\s)(.*)$", topic):
        return matches.group(1).strip(), matches.group(2).strip()
    else:
        return (None, None)


if __name__ == "__main__":
    main()