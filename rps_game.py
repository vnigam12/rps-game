import random
from typing import Dict, Tuple

# ----------------------------
# Game Constants / Config
# ----------------------------

# Emoji definitions for user/computer selection display
EMOJI_MAP: Dict[str, str] = {
    "r": "🪨",   # rock
    "p": "📄",   # paper
    "s": "✂️"    # scissors
}

# Map input variations to canonical choices
INPUT_MAP: Dict[str, str] = {
    "r": "r", "rock": "r",
    "p": "p", "paper": "p",
    "s": "s", "scissors": "s"
}

# Winning rules: key beats value
# rock beats scissors, paper beats rock, scissors beats paper
WINS_AGAINST: Dict[str, str] = {
    "r":"s",
    "p":"r",
    "s": "p"
}

# Allowed choices
CHOICES = tuple(EMOJI_MAP.keys())

# ----------------------------
# Helper Functions
# ----------------------------

def normalize_input(user_input: str) -> str:
    """
    :param user_input: r/p/s or rock/paper/scissors
    :return: normalized input (Raise ValueError if user input is invalid)
    """
    cleaned = user_input.strip().lower()
    if cleaned in INPUT_MAP:
        return INPUT_MAP[cleaned]
    raise ValueError("Invalid input")

def decide_winner(user_choice: str, computer_choice: str) -> str:
    """
    :param user_choice: Normalized user input
    :param computer_choice: Computer random selection
    :return: "win", "lose", or "tie"
    """
    if user_choice == computer_choice:
        return "tie"
    elif WINS_AGAINST[user_choice] == computer_choice:
        return "win"
    else:
        return "lose"

def play_round() -> Tuple[str, str, str]:
    """
    Plays one round of the game.
    :return: user_choice, computer_choice, result
    """
    computer_choice = random.choice(CHOICES)

    while True:
        try:
            user_input = input("Rock, Paper or Scissors? (r/p/s or Rock/Paper/Scissors, q to quit): ")
            if user_input.strip().lower() == "q":
                return "q", computer_choice, "quit"

            user_choice = normalize_input(user_input)
            break
        except ValueError:
            print("Invalid input. Please try again.\n")

    result = decide_winner(user_choice, computer_choice)
    return user_choice, computer_choice, result

# ----------------------------
# Main Game Loop
# ----------------------------

def main() -> None:
    print("Welcome to Rock-Paper-Scissors!")
    print("Mode: Best of 3 (first to 2 wins)\n")

    # Score tracking
    user_score = 0
    computer_score = 0
    ties = 0
    wins_needed = 2 # Best of 3 => First to 2 wins

    round_num = 1

    while user_score < wins_needed and computer_score < wins_needed:
        print(f" --- Round {round_num} --- ")

        user_choice, computer_choice, result = play_round()

        # Quit handling
        if result == "quit":
            print("Thanks for playing!")
            return

        # Show user/computer choices with emojis
        print(f"You chose: {EMOJI_MAP[user_choice]} ({user_choice})")
        print(f"Computer chose: {EMOJI_MAP[computer_choice]} ({computer_choice})")

        # Update score
        if result == "win":
            print("You win this round!\n")
            user_score += 1
        elif result == "lose":
            print("You lose this round!\n")
            computer_score += 1
        else:
            print("It's a tie!\n")
            ties += 1

        # Display scoreboard after each round
        print(f"Score:: You: {user_score} | Computer: {computer_score} | Ties: {ties}\n")
        round_num += 1

    # Final result
    print("Match Over!")
    if user_score > computer_score:
        print("You won the Best-of-3 match!")
    else:
        print("Computer won the Best-of-3 match!")
    print(f"Final Score:: You: {user_score} | Computer: {computer_score} | Ties: {ties}")

if __name__ == "__main__":
    main()