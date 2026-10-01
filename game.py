import random
from logic import feedback

DIFFICULTIES = {
    "easy": (4, 4, 12),
    "medium": (4, 6, 10),
    "hard": (5, 8, 8)
}

class Mastermind:
    def __init__(self):
        self.history = []
        self.game_over = False

        self.choose_difficulty()

    def choose_difficulty(self):
        print("Choose difficulty:")
        print("1. Easy   - 4 symbols, digits 1-4, 12 turns")
        print("2. Medium - 4 symbols, digits 1-6, 10 turns")
        print("3. Hard   - 5 symbols, digits 1-8, 8 turns")

        while True:
            choice = input("Enter choice (1-3): ").strip()

            if choice == "1":
                difficulty = "easy"
                break
            elif choice == "2":
                difficulty = "medium"
                break
            elif choice == "3":
                difficulty = "hard"
                break
            else:
                print("Enter 1, 2, or 3.")

        self.difficulty = difficulty
        self.code_length, self.max_symbol, self.turns = DIFFICULTIES[difficulty]

        self.code = [
            str(random.randint(1, self.max_symbol))
            for _ in range(self.code_length)
        ]

    def run(self):
        print(
            f"Mastermind — enter {self.code_length} digits "
            f"from 1 to {self.max_symbol}."
        )

        while self.turns and not self.game_over:
            raw = input(f"{self.turns} turns left > ").strip()

            if raw.lower() == "q":
                self.game_over = True
                return

            if (
                len(raw) != self.code_length
                or any(
                    ch not in "123456789"[:self.max_symbol]
                    for ch in raw
                )
            ):
                print(
                    f"Enter exactly {self.code_length} digits "
                    f"from 1 to {self.max_symbol}."
                )
                continue

            guess = list(raw)
            exact, partial = feedback(self.code, guess)

            self.history.append((raw, exact, partial))
            self.turns -= 1

            print("Exact:", exact, " Partial:", partial)

            # Check win before checking whether turns are exhausted.
            if exact == self.code_length:
                self.game_over = True
                print("Cracked the code!")
                return

            # If the final turn was used without winning, the game is lost.
            if self.turns == 0:
                self.game_over = True
                print("Out of turns! The code was", "".join(self.code))