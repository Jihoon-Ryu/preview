import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app=Flask("Previewer")

URL="""How to invite HTML input value(URL) into a Python constant?"""

req= requests.get(URL)

soup=BeautifulSoup(req.text, "html.parser")

@app.route("/")
def home():
 title = soup.find("meta", {"property":"og:title"})["content"]
 descript = soup.find("meta", {"property":"og:description"})["content"]
 image_src = soup.find("meta", {"property":"og:image"})["content"]   
 return render_template ("index.html", title=title, descript=descript, image_src=image_src)



app.run(host="0.0.0.0")