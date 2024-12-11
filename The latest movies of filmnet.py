import requests
import bs4

response = requests.get("https://tv.filmnet.ir/")
soup = bs4.BeautifulSoup(response.text, "html.parser")
movies = soup.find_all("h4", attrs={"class": "css-stgv2v eg0dt7k0"})

for i in movies:
    print(i.text)

