from flask import Flask, render_template_string
import datetime
import random

app = Flask(__name__)

# Fun facts about 2025
facts = [
    "2025 marks the 100th anniversary of the first successful human kidney transplant.",
    "The Mars 2025 mission is planned to send astronauts to the red planet!",
    "By 2025, experts predict AI will be integrated into every aspect of our daily lives.",
    "In 2025, self-driving cars are expected to be common on the roads."
]

@app.route('/')
def welcome():
    # Get the current time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Countdown to New Year 2025
    new_year = datetime.datetime(2025, 1, 1)
    time_left = new_year - datetime.datetime.now()
    countdown = str(time_left).split('.')[0]  # Format the countdown time

    # Pick a random fun fact
    fact = random.choice(facts)

    return render_template_string('''
    <html>
        <head>
            <title>Welcome to 2025!</title>
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    background: linear-gradient(135deg, #00c6ff, #0072ff);
                    background-size: 400% 400%;
                    animation: gradientAnimation 10s ease infinite;
                    color: #fff;
                    text-align: center;
                    padding-top: 50px;
                    transition: all 0.5s ease;
                }
                h1 {
                    font-size: 4em;
                    color: #ff8c00;
                    text-shadow: 3px 3px 10px rgba(255, 140, 0, 0.7);
                }
                p {
                    font-size: 1.5em;
                    color: #f1f1f1;
                    margin-top: 20px;
                }
                .highlight {
                    color: #00d1b2;
                    font-weight: bold;
                }
                .exciting {
                    font-size: 2.5em;
                    color: #ff005f;
                    text-decoration: underline;
                    animation: pulse 1.5s infinite;
                }
                .countdown {
                    font-size: 2em;
                    color: #ff00ff;
                    font-weight: bold;
                }
                .fact {
                    font-size: 1.5em;
                    color: #ffff00;
                    margin-top: 40px;
                    font-style: italic;
                }
                .greeting {
                    font-size: 2em;
                    color: #fff;
                    margin-top: 30px;
                }
                .name-input {
                    margin-top: 20px;
                    padding: 10px;
                    font-size: 1.2em;
                }
                @keyframes pulse {
                    0% { transform: scale(1); }
                    50% { transform: scale(1.1); }
                    100% { transform: scale(1); }
                }
                @keyframes gradientAnimation {
                    0% { background-position: 0% 50%; }
                    50% { background-position: 100% 50%; }
                    100% { background-position: 0% 50%; }
                }
            </style>
        </head>
        <body>
            <h1>🎉 Welcome to <span class="highlight">2025!</span> 🎉</h1>
            <p class="exciting">A New Year, A New Beginning!</p>
            <p class="countdown">Time left until 2025: {{ countdown }}</p>
            <p>Current Time: {{ current_time }}</p>
            
            <p class="fact">Fun Fact: {{ fact }}</p>

            <div class="greeting">
                <p>Enter your name for a personal greeting!</p>
                <form method="GET">
                    <input type="text" name="name" class="name-input" placeholder="Your Name" />
                    <input type="submit" value="Greet Me!" />
                </form>
            </div>

            {% if request.args.get('name') %}
            <h2>Hello, {{ request.args.get('name') }}! Glad you're here! 🎉</h2>
            {% endif %}
        </body>
    </html>
    ''', countdown=countdown, current_time=current_time, fact=fact)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
