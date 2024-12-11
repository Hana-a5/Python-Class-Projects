import requests
import bs4

response = requests.get("https://takhfifan.com/tehran/restaurants-cafes")
soup = bs4.BeautifulSoup(response.text, "html.parser")
restaurants = soup.find_all("p", attrs={"class": "vendor-card-box__title-text"})
rates = soup.find_all("p", attrs={"class": "rate-badge__rate-value"})

list1 = []
list2 = []

for i in restaurants:
    list1.append(i.text)
for j in rates:
    list2.append(j.text)

dic = {}
for r in range(len(restaurants)):
    dic[list2[r]] = list1[r]

best_rate = max(list2)
print("The best restaurant:",dic[best_rate])
