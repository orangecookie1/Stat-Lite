#222831, 393E46, 303841, 3A4750
from flask import Flask, render_template, request, redirect
import requests
import json
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", displayName = False)

@app.route("/searchleaderboard", methods=['POST'])
def search():
    input = request.form["input"]
    response = requests.get("https://hopliteapi.isabel.gg/api/stats/royale/" + input)
    data = json.loads(response.text)
    print(type(data))
    player = data["profile"]["username"]
    rank = data["profile"]["rank"]
    gamesPlayed = data["total"]["gamesPlayed"]
    wins = data["total"]["wins"]
    kills = data["total"]["kills"]
    assists = data["total"]["assists"]
    playtime = data["total"]["playtime"]
    return render_template("search.html", username=player, rank=rank, gamesPlayed=gamesPlayed, wins=wins, kills=kills, assists=assists, playtime=playtime, displayName = True)
    #return render_template("home.html", username="No! You dummy thats not a username!", displayName = True)

@app.route("/base")
def base():
    return "You found base!!"

if __name__ == "__main__":
    app.run(debug=True)