# define constants
CENT = 1
NICKEL = 5
DIME = 10
QUARTER = 25


def main():
    # allow user to input the change owed
    change = -1
    while change < 0:
        try:
            change = int(float(input("Change: ")) * 100)
        except ValueError:
            continue
    coins_given(change)

# define the function to calculate how many coins are returned


def coins_given(change):
    coins = 0
    # continues in the loop until there is no change left
    while change > 0:
        if change >= QUARTER:
            coins += 1
            change -= QUARTER
        elif change >= DIME:
            coins += 1
            change -= DIME
        elif change >= NICKEL:
            coins += 1
            change -= NICKEL
        elif change >= CENT:
            coins += 1
            change -= CENT

    print(coins)


# call the main function
main()
