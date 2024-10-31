from flask import Flask, request

app = Flask(__name__)

import random

max_score = 21

def score2points():
    return random.randint(0, 1)

def rebound():
    return random.choice(["You got the ball back!", "Your Opponent rebounded the ball!"])

def opponent_offense():
    return random.choice(["Your opponent passed the ball!", "Your Opponent shot the ball!"])

steal_chance = 8

def steal_ball():
    random_number = random.randint(0, 10)
    return random_number > steal_chance

@app.route('/')
def home():
    return "Welcome to the Basketball Game 21! Head to /play to start."

@app.route('/play', methods=['GET', 'POST'])
def play():
    my_score = 0
    opponent_score = 0
    if request.method == 'POST':
        shot = request.form['action']
        if shot.lower() == "shoot":
            if score2points() == 1:
                my_score += 2
                if my_score >= max_score:
                    return f"You won the game {my_score} to {opponent_score}!"
            else:
                rebound_result = rebound()
                if rebound_result == "You got the ball back!":
                    pass
                else:
                    while True:
                        opponent_offense_result = opponent_offense()
                        if opponent_offense_result == "Your opponent passed the ball!":
                            steal = request.form['steal']
                            if steal.lower() == "yes" and steal_ball():
                                break
                            else:
                                continue
                        else:
                            if score2points() == 1:
                                opponent_score += 2
                                if opponent_score >= max_score:
                                    return f"You lost the game {opponent_score} to {my_score}"
                            else:
                                rebound_result = rebound()
                                if rebound_result == "Your Opponent rebounded the ball!":
                                    continue
                                else:
                                    break
        elif shot.lower() == "pass":
            pass
    return f"Your team score is {my_score}, Your opponent's team score is {opponent_score}. Will you pass or shoot?"

if __name__ == "__main__":
    app.run(debug=True)
