import requests
import bs4
from colorama import Fore

response = requests.get("https://karnameh.com/car-price")
soup = bs4.BeautifulSoup(response.text, "html.parser")
cars = soup.find_all("p", attrs={"class": "MuiTypography-root MuiTypography-body1 muirtl-iy5bpq"})
prices = soup.find_all("p", attrs={"class": "MuiTypography-root MuiTypography-body1 muirtl-22intj"})

list1 = []
list2 = []

for i in cars:
    list1.append(i.text)
for j in prices:
    list2.append(j.text)

for r in range(len(cars)):
    print(list1[r], 6*" ", Fore.CYAN, list2[r], Fore.RESET)
