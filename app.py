from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

atom_bot = ChatBot(
    "atom_v1a", storage_adapter="chatterbot.storage.SQLStorageAdapter")

atom_trainer = ChatterBotCorpusTrainer(atom_bot)
atom_trainer.train("chatterbot.corpus.english")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=['POST'])
def getBotResponse():
    userText = request.json['message']
    return str(atom_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
