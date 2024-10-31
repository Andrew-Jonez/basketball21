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
    if request.method == 'POST':
        action = request.form['action']
        steal = request.form.get('steal', '')
        # Your game logic here, modify variables my_score and opponent_score accordingly
        # For the sake of example, assume these values:
        my_score = 0
        opponent_score = 0

        # Returning updated scores as an example; you'll need to include the actual game logic
        return render_template_string('''
            <p>Your team score is {{ my_score }}, Your opponent's team score is {{ opponent_score }}.</p>
            <form method="POST">
                <label for="action">Will you pass or shoot?</label>
                <input type="text" id="action" name="action">
                <button type="submit">Submit</button>
                <br>
                <label for="steal">Will you go for the steal? Type yes or no:</label>
                <input type="text" id="steal" name="steal">
            </form>
        ''', my_score=my_score, opponent_score=opponent_score)

    return render_template_string('''
        <p>Your team score is 0, Your opponent's team score is 0. Will you pass or shoot?</p>
        <form method="POST">
            <label for="action">Will you pass or shoot?</label>
            <input type="text" id="action" name="action">
            <button type="submit">Submit</button>
        </form>
    ''')

if __name__ == "__main__":
    app.run(debug=True)
