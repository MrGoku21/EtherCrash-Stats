from bs4 import BeautifulSoup
import re
import requests
import time

id = input("Username: ")
print("\n")

page = requests.get(f'https://www.ethercrash.io/user/{id}')
soup = BeautifulSoup(page.text, 'html.parser')
i = soup.find('div', id_="container")

for i in soup():
    games = soup.select('h4', class_="mb-0 card-title")[1].get_text()
    rank = soup.select('h4', class_="mb-0 card-title")[2].get_text()
    profit = soup.select('h4', class_="mb-0 card-title")[3].get_text()
    net = soup.select('h4', class_="mb-0 card-title")[4].get_text()


print(f"{id}\n\nGames: {games}\n\nRank: {rank}\n\nGross Profit: {profit}\n\nNet Profit {net}")

