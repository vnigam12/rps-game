# 🪨📄✂️ Rock Paper Scissors (Python)

A fun and beginner-friendly Rock-Paper-Scissors game built in Python with emojis and a **Best-of-3 mode** (first to 2 wins).

This project demonstrates Python fundamentals such as:
- loops and conditionals
- dictionaries and mappings
- functions and modular code
- input validation
- basic unit testing

## 🚀 Features

- Best-of-3 match mode (first to 2 wins)
- Emoji-based display for choices
- Accepts inputs: `r/p/s` or `rock/paper/scissors`
- Scoreboard tracking (wins/losses/ties)
- Quit anytime using `q`
- Unit tests included

## 🛠️ Requirements
- Python 3.9+

Note: No external libraries required.

## ▶️ How to Run
```bash
git clone https://github.com/<your-username>/rock-paper-scissors.git
cd rock-paper-scissors
python rps_game.py
```

## 🎮 Example Gameplay
```bash
Welcome to Rock-Paper-Scissors!
Mode: Best of 3 (first to 2 wins)

--- Round 1 ---
Rock, Paper or Scissors? (r/p/s or word, q to quit): rock
You chose: 🪨 (r)
Computer chose: ✂️ (s)
You win this round!

Score:: You: 1 | Computer: 0 | Ties: 0
```

## 🧪 Run Tests
```bash
python -m unittest discover tests
```

## 📌 Future Enhancements
- Best-of-5 / Best-of-7 modes
- Game history (round-by-round log)
- Persistent scoreboard across sessions
- GUI or web version

📜 License
```text
MIT License
```
