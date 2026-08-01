from flask import Flask, jsonify, request, render_template
import json
import random

server=Flask(__name__)

msg = []
apt = 0
num = ""
messages = []
@server.route("/")
def HOME():
    global apt
    global num
    global messages
    apt = 0
    messages=[]
    num = "".join(random.sample("0123456789", 4))
    print(num)
    return render_template("index.html",message = ["🎮 Welcome to the Number Guessing Game!", "Guess the 4-digit number."], apt = apt, ended = False)



@server.route("/check", methods=["POST"])
def checking():
    global messages
    global apt
    cl = request.form["newGuess"]
    count = 0

    for i in range(4):
        if cl[i] == num[i]:
            messages.append(f"{cl[i]} is in the RIGHT position.")
            count += 1
        elif cl[i] in num:
            messages.append(f"{cl[i]} is PRESENT but in the wrong position.")

    if count == 0:
        messages.append("❌ No digits are in the correct position.")

    if count == 4:
        messages.append("\n🎉 Congratulations! You guessed the number!")
        messages.append(f"The number was: {num}")
        messages.append(f"You took {apt} attempts.")
        apt += 1
        return render_template("index.html", messages=messages, apt = apt, ended=True)



    messages.append(f"Your Guess: {cl}")
    messages.append("-------------------")
    # messages.reverse()
    apt += 1
    return render_template("index.html", messages=messages, apt = apt, ended=False)


if __name__== "__main__":
    server.run(debug=True)