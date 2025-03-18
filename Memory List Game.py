import random

"""
~~~~~~Memory List Game~~~~~~
1. Create the truth list. for loop 0 through N_PAIRS twice
2. Shuffle it. random.shuffle(truth)
3. Create a displayed list. Probably using if hidden:
4. Get a valid index from user. (0 <= valid <= len(truth))
5. Check correct. Mark correct guesses as not_hidden. Otherwise, tell correct values and 
    do not update. Cannot enter same index twice.
6. Play multiple turns. Call clear_terminal between turns.
"""
NUM_PAIRS = 3
truth = []
display = []


def main():
    # Setup.
    truth_list()  # Build a list of pairs with a number of pairs equal to NUM_PAIRS
    random.shuffle(truth)  # Shuffle the list so we can play.
    display_list()  # Make a "blank" list full of '*'
    index = len(display) + 1  # Set variables so the while loops later will have a predetermined condition.
    count = 1
    print(display)  # Displays our "face down" cards.

    # Play game with unknown number of turns.
    while display != truth:
        count, index1 = get_valid_index(count, index)
        count, index2 = get_valid_index(count, index)
        while index1 == index2:
            print("You cannot choose the same number twice. Try again.")
            count, index2 = get_valid_index(count, index)

        print("Value at index", index1, "is", truth[index1])  # show the user what value is in the indices they chose.
        print("Value at index", index2, "is", truth[index2])

        check_matching(index1, index2)

    print("Congratulations! You won!")


def check_matching(index1, index2):
    if truth[index1] == truth[index2]:  # Check to see if the flipped cards match.
        update_display(index1, index2)
        print("Match!")
        input("Press enter to continue... ")  # accepts any input to get a pause before wiping screen.
        clear_terminal()
        print(display)
    else:  # If they don't match, tell the user.
        print("No match. Try again.")
        input("Press enter to continue... ")  # accepts any input to get a pause before wiping screen.
        clear_terminal()  # reset the terminal with current display and all prior lines removed.
        print(display)


def get_valid_index(count, index):
    while index not in range(len(display)):  # Get first input and throw errors until a valid index is entered.
        try:
            if is_odd(count):
                index = int(input("Enter first index: "))
            else:
                index = int(input("Enter second index: "))

            while display[index] != '*':  # custom case where input is valid but has already been matched.
                print("This number has already been matched. Try again.")
                if is_odd(count):
                    index = int(input("Enter first index: "))
                else:
                    index = int(input("Enter second index: "))

        except IndexError:
            print("Invalid index. Try again.")
        except ValueError:
            print("Not a number. Try again.")
    count += 1  # once we get a valid input.

    return count, index


def is_odd(n):
    if n % 2 != 0:
        return True


def update_display(first_index, second_index):
    display[first_index] = truth[first_index]
    display[second_index] = truth[second_index]


def display_list():
    for i in range(2 * NUM_PAIRS):
        display.append('*')


def truth_list():
    for i in range(NUM_PAIRS):
        truth.append(i)
        truth.append(i)


def clear_terminal():
    for i in range(20):
        print('\n')


if __name__ == '__main__':
    main()