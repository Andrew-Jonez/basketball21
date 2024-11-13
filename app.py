from flask import Flask, request, render_template_string

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
    my_score = request.form.get('my_score', default=0, type=int)
    opponent_score = request.form.get('opponent_score', default=0, type=int)
    message = ""
    action = request.form.get('action')
    steal = request.form.get('steal')

    if request.method == 'POST':
        if action:
            if action.lower() == "shoot":
                if score2points() == 1:
                    my_score += 2
                    message = f"You scored 2 points! Your team score is now {my_score}, Your opponents team score is {opponent_score}."
                    if my_score >= max_score:
                        return render_template_string('''
                            <p>{{ message }}</p>
                            <p>You won the game {{ my_score }} to {{ opponent_score }}!</p>
                            <a href="/play">Start a New Game</a>
                        ''', message=message, my_score=my_score, opponent_score=opponent_score)
                else:
                    message = "You missed. " + rebound()
                    if "You got the ball back!" in message:
                        return render_template_string('''
                            <p>{{ message }}</p>
                            <form method="POST">
                                <input type="hidden" name="my_score" value="{{ my_score }}">
                                <input type="hidden" name="opponent_score" value="{{ opponent_score }}">
                                <label for="action">Will you pass or shoot?</label>
                                <input type="text" id="action" name="action">
                                <button type="submit">Submit</button>
                            </form>
                        ''', message=message, my_score=my_score, opponent_score=opponent_score)

                    while True:
                        opponent_offense_result = opponent_offense()
                        message = opponent_offense_result
                        if opponent_offense_result == "Your opponent passed the ball!":
                            return render_template_string('''
                                <p>{{ message }}</p>
                                <form method="POST">
                                    <input type="hidden" name="my_score" value="{{ my_score }}">
                                    <input type="hidden" name="opponent_score" value="{{ opponent_score }}">
                                    <label for="steal">Will you go for the steal? Type yes or no:</label>
                                    <input type="text" id="steal" name="steal">
                                    <button type="submit">Submit</button>
                                </form>
                            ''', message=message, my_score=my_score, opponent_score=opponent_score)
                        elif opponent_offense_result == "Your Opponent shot the ball!":
                            if score2points() == 1:
                                opponent_score += 2
                                message = f"Your opponent scored 2 points! Your opponent's team score is now {opponent_score}, Your team score is {my_score}."
                                if opponent_score >= max_score:
                                    return render_template_string('''
                                        <p>{{ message }}</p>
                                        <p>You lost the game {{ opponent_score }} to {{ my_score }}</p>
                                        <a href="/play">Start a New Game</a>
                                    ''', message=message, my_score=my_score, opponent_score=opponent_score)
                            else:
                                message = "Your opponent missed. " + rebound()
                                if "Your Opponent rebounded the ball!" in message:
                                    continue
                                else:
                                    break

        if steal:
            if steal.lower() == "yes":
                if steal_ball():
                    message = "You stole the ball!"
                    return render_template_string('''
                        <p>{{ message }}</p>
                        <form method="POST">
                            <input type="hidden" name="my_score" value="{{ my_score }}">
                            <input type="hidden" name="opponent_score" value="{{ opponent_score }}">
                            <label for="action">Will you pass or shoot?</label>
                            <input type="text" id="action" name="action">
                            <button type="submit">Submit</button>
                        </form>
                    ''', message=message, my_score=my_score, opponent_score=opponent_score)
                else:
                    message = "You didn't get the steal!"

    return render_template_string('''
        <p>Your team score is {{ my_score }}, Your opponent's team score is {{ opponent_score }}. {{ message }}</p>
        <form method="POST">
            <input type="hidden" name="my_score" value="{{ my_score }}">
            <input type="hidden" name="opponent_score" value="{{ opponent_score }}">
            <label for="action">Will you pass or shoot?</label>
            <input type="text" id="action" name="action">
            <button type="submit">Submit</button>
        </form>
    ''', my_score=my_score, opponent_score=opponent_score, message=message)

if __name__ == "__main__":
    app.run(debug=True)
