from flask import Flask, request, render_template
from melody import converse

app = Flask(__name__)

conversations = {}

@app.route("/converse")
def chat():
    name = request.args["name"]
    answer = request.args.get("answer", None)
    reset = request.args.get("reset", None)

    if not reset and name in conversations:
        conversation = conversations[name]
        if answer:
            statement = conversation.send(answer)
        else:
            statement = next(conversation)
    else:
        conversation = converse()
        conversations[name] = conversation
        statement = next(conversation)

    return statement


@app.route("/")
def index():
    return render_template("index.html")

