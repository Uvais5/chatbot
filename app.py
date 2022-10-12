from flask import Flask, render_template, request,jsonify
import chatbot
app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/personal",methods =["POST"])
def personal():
    p = request.form["ps"]
    if p =="Personal":
        return render_template("index.html")
    else:
        return render_template("index1.html")


@app.route("/pschatbot")
def get_bot_response():
    userText = request.args.get('msg')
    if userText =="":
        return jsonify("Sorry couldn't find you query 😒")
    else:
        return  jsonify(chatbot.chatbot_response(userText))


@app.route("/datachatbot")
def get_bot_response_aboutedata():
    # userText = request.form["input"]
    userText = request.args.get('msg')
    if userText =="":
        return jsonify("Sorry couldn't find you query 😒")
    else:
        return  jsonify( chatbot.chatbot_response_about_data(userText))

if __name__ == "__main__":
    app.run(debug=True)