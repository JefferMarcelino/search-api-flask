from flask import Flask, request, jsonify
from flask import Response
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = "i_am_not_feeling_sleepy_so_i_am_coding_this"

@app.route('/search')
def mostread():
    args = request.args
    q = args.get("q")
    htmlBody = requests.get(f"https://www.google.com/search?channel=fs&client=ubuntu&q={q}&lr=lang_pt")
    soup = BeautifulSoup(htmlBody.content, "html.parser")  
    contentTextList = soup.find_all(class_="Gx5Zad xpd EtOod pkphOe")
    
    try:
        finalContent = ""

        for item in contentTextList:
            if not finalContent:
                if item.find(class_="Xdlr0d") or item.find(class_="xpc") or item.find("img"):
                    if not item.find(class_="K8tyEc"):
                        finalContent = item

        contentHead = finalContent.find(class_="kCrYT").find_all("span")

        title = contentHead[0].text

        try:
            field = contentHead[1].text
        except:
            field = ""

        try:
            link = finalContent.find(class_="BNeawe s3v9rd AP7Wnd").find("a").get("href").replace("/url?q=", "")
        except:
            link = ""

        try:
            image = finalContent.find(class_="Xdlr0d").find("a").get("href").replace("/imgres?imgurl=", "")
            final = image.index(".jpg") or image.index(".png") or image.index(".jpeg")
            calculatedFinal = final + 5
            if image[0:calculatedFinal][0:5] == "https":
                image = image[0:calculatedFinal]
            else:
                image = ""
        except:
            image = ""

        content = finalContent.find(class_="BNeawe s3v9rd AP7Wnd").text.replace("Wikipédia", "")

        return {
            "title": title,
            "field": field,
            "link": link,
            "image": image,
            "content": content
        }, 200

    except:
        return {
            'message': 'Not found'
        }, 404
