import requests
from bs4 import BeautifulSoup
import pandas as pd


# r = requests.get("https://www.startech.com.bd/laptop-notebook")

# print("Scrapping Page: 1.....")

# soup = BeautifulSoup(r.content, "html.parser")

# # print(r)
# # print(soup)

# base_class = soup.find('div', class_ = "main-content p-items-wrap")
# items = base_class.find_all('div', class_ = "p-item")

# # print(items)

# data = []

# for product in items:
#     model = product.find('h4', class_ ="p-item-name").text.strip()
#     # print(model)
#     try:
#         price = int(product.find("span", class_ = "price-old").text.replace(",", "").strip('৳'))

#     except:
#         try:
#             base = product.find("div", class_ = "p-item-price")
#             price = int(base.find("span").text.replace(",", "").strip("৳"))

#         except:
#             base= product.find("div", class_  = "p-item-price")
#             price = int(base.find("Span").text.strip('৳'))

#     # print(price)
#     # print(type(price))

#     link = product.find('a').get('href')

#     data.append(
#         {
#             "Model": model,
#             "price": price,
#             "Link": link
#         }
#     )

data = []
page_num = 3
for i in range(1, page_num+1):
    print(f"Scrapping Page: {i}.....")
    r = requests.get(f"https://www.startech.com.bd/laptop-notebook?page={i}")

    soup = BeautifulSoup(r.content, "html.parser")

    base_class = soup.find('div', class_ = "main-content p-items-wrap")
    items = base_class.find_all('div', class_ = "p-item")

    for product in items:
        model = product.find('h4', class_ ="p-item-name").text.strip()
        # print(model)
        try:
            price = int(product.find("span", class_ = "price-old").text.replace(",", "").strip('৳'))

        except:
            try:
                base = product.find("div", class_ = "p-item-price")
                price = int(base.find("span").text.replace(",", "").strip("৳"))

            except:
                base= product.find("div", class_  = "p-item-price")
                price = int(base.find("Span").text.strip('৳'))

        link = product.find('a').get('href')

        data.append(
            {
                "Model": model,
                "price": price,
                "Link": link
            }
        )


df = pd.DataFrame(data)
df.to_csv("C:/Musfique's Folder/Python/Shongjog-Python-Course/GoodBye/startech_data.csv", index=False)

print("Task Completed!!!")