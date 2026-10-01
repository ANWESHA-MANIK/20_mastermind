import random
from logic import feedback


class Mastermind:
    def __init__(self):
        self.code = [str(random.randint(1, 6)) for _ in range(4)]
        self.history = []
        self.turns = 10
        self.game_over = False

    def run(self):
        print("Mastermind — enter four digits from 1 to 6.")

        while self.turns and not self.game_over:
            raw = input(f"{self.turns} turns left > ").strip()

            if raw.lower() == "q":
                self.game_over = True
                return

            if len(raw) != 4 or any(ch not in "123456" for ch in raw):
                print("Enter exactly four digits from 1 to 6.")
                continue

            guess = list(raw)
            exact, partial = feedback(self.code, guess)

            self.history.append((raw, exact, partial))
            self.turns -= 1

            print("Exact:", exact, " Partial:", partial)

            # Check win before checking whether turns are exhausted.
            if exact == 4:
                self.game_over = True
                print("Cracked the code!")
                return

            # If the final turn was used without winning, the game is lost.
            if self.turns == 0:
                self.game_over = True
                print("Out of turns! The code was", "".join(self.code))