from random import randint

# ASCII Art for 6-sided dice
DICE_ART = {
    1: ["+-------+",
        "|       |",
        "|   o   |",
        "|       |",
        "+-------+"],
    2: ["+-------+",
        "| o     |",
        "|       |",
        "|     o |",
        "+-------+"],
    3: ["+-------+",
        "| o     |",
        "|   o   |",
        "|     o |",
        "+-------+"],
    4: ["+-------+",
        "| o   o |",
        "|       |",
        "| o   o |",
        "+-------+"],
    5: ["+-------+",
        "| o   o |",
        "|   o   |",
        "| o   o |",
        "+-------+"],
    6: ["+-------+",
        "| o   o |",
        "| o   o |",
        "| o   o |",
        "+-------+"]
}

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("That's not a valid number. Try again.")

def roll_dice(num_dice, num_sides):
    return [randint(1, num_sides) for _ in range(num_dice)]

def display_roll(rolls, num_sides):
    print("\nDice Roll:")
    
    if num_sides == 6:
        dice_faces = [DICE_ART[roll] for roll in rolls]
        for line_num in range(5):
            print("  ".join(die[line_num] for die in dice_faces))
    else:
        result = "| " + " | ".join(str(r) for r in rolls) + " |"
        print(result)
    
    total = sum(rolls)
    print(f"Total: {total}")

    # Critical roll alert!
    if all(roll == num_sides for roll in rolls):
        print("🔥 CRITICAL ROLL! All dice rolled the maximum value! 🔥")

def main():
    print("🎲 Welcome to the Dice Rolling Game! 🎲\n")

    num_dice = get_positive_int("How many dice are you rolling? ")
    num_sides = get_positive_int("How many sides on each die? ")

    while True:
        rolls = roll_dice(num_dice, num_sides)
        display_roll(rolls, num_sides)

        roll_again = input("\nRoll again? Press Enter to roll or 'q' to quit: ").strip().lower()
        if roll_again == "q":
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()