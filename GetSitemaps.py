import requests
from bs4 import BeautifulSoup

s = requests.Session()
r = s.get(r"https://stackshare.io/sitemap.xml")
soup = BeautifulSoup(r.content, "html.parser")
sitemap = soup.find_all("loc")

sitemaps = []

# Generiert alle Sitemaps
for elem in sitemap:
    if "https://stackshare.io/sitemaps/stacks" in elem.text:
        sitemaps.append(elem.text)

links = []
# Generiert Linkliste aus allen Stack-Sitemaps
for index, elem in enumerate(sitemaps):
    r = s.get(elem)
    soup = BeautifulSoup(r.content, "html.parser")
    linkList = soup.find_all("loc")
    for link in linkList:
        links.append(link.text)

# Output der Links in separate File sicherheitshalber
with open("./Output.txt", "w") as f:
    f.write(";".join(links))

# Requesten der Links
for index, elem in enumerate(links):
    r = s.get(elem)
    stackName = elem.rsplit("/", 1)[1]
    company = elem.rsplit("/", 2)[1]
    with open("./"+company+"_"+stackName+".txt", "wb") as f:
        f.write(r.content)
    print(str(index))
