# Flask Basketball App

This is a simple Flask application that simulates a basketball game. The game logic is implemented in Python, and the user interface is created using HTML templates.

## Project Structure

```
basketball21
├── src
│   ├── app.py               # Entry point of the Flask application
│   ├── basketball21.py      # Game logic for the basketball game
│   └── templates
│       └── index.html       # HTML template for the main page
├── requirements.txt         # Dependencies for the project
└── README.md                # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd flask-basketball-app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```
   python src/app.py
   ```

5. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage Guidelines

- The application simulates a basketball game where users can interact with the game through the web interface.
- The game logic includes scoring, rebounds, opponent actions, and the possibility of stealing the ball.
