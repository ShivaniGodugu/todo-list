import random


def roll_dice(num_dice):
    results = []
    for _ in range(num_dice):
        result = random.randint(1, 6)  # Simulate rolling a 6-sided die
        results.append(result)
    return results


def main():
    while True:
        try:
            num_dice_input = input("Enter the number of dice to roll (or 'q' to quit): ")
            if num_dice_input.lower() == 'q':
                print("Thanks for playing.")
                break

            num_dice = int(num_dice_input)
            if num_dice <= 0:
                raise ValueError("The number of dice must be a positive integer.")

            results = roll_dice(num_dice)
            print(f"Results from rolling {num_dice} dice: {results}")

        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer or 'q' to quit.")


if __name__ == "__main__":
    main()
