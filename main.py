import pandas as pd
import requests
from bs4 import BeautifulSoup



Names = []
Price = []
Availability = []


url = "https://books.toscrape.com/catalogue/page-1.html"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
#print(soup)
for i in range(1,20):
    np= soup.find("li", class_="next")
    npl = np.find("a")["href"]
    #print(npl)
    cnp = "https://books.toscrape.com/catalogue/"+npl
    #print(cnp)
    url = cnp
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")

    names = soup.find_all("h3")
    #print(names)
    for i in names:
        n = i.find("a")["title"]
        Names.append(n)
        #print(len(Names))

    price = soup.find_all("p",class_="price_color")
    #print(price)
    for a in price:
        b = a.text
        Price.append(b)
        #print(len(Price))

    Available = soup.find_all("p",class_="instock availability")
    #print(Available)
    for c in Available:
        d = c.text.strip()
        Availability.append(d)
        #print(len(Availability))

df = pd.DataFrame({"Name": Names, "Price": Price, "Availability": Availability})
#print(df)
df.to_csv("Books Data.csv")
