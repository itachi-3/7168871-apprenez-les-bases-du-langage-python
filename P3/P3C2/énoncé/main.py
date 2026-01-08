from bs4 import Beautifulsoup

with open("index.html","r") as file:
  soup = beautifulsoup(file,"html.parser")

titre= soup.title.string
print(titre)

id_h2= soup.find.string(id="h1")
print(id_h2)
