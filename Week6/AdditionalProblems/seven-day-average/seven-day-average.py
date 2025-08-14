import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)


    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    new_cases = {}
    previous_cases = {}

    # Iterating through the rows in the reader
    for row in reader:
        state = row["state"]
        total_cases = int(row["cases"])

        # Determine whether the state already has data stored
        if state in new_cases:
            if len(new_cases[state]) == 14:
                new_cases[state].pop(0)

            # add the new data
            daily_new = total_cases - previous_cases[state]
            new_cases[state].append(daily_new)
        # If no data is yet stored, create a key for the state
        else:
            new_cases[state] = []  # skip first day
        previous_cases[state] = total_cases

    return new_cases


# Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):

    # Iterating through the states
    for state in states:
        previous_seven = sum(new_cases[state][:7]) / 7
        current_seven = sum(new_cases[state][7:14]) / 7

        # Finding the difference
        difference = current_seven - previous_seven
        try:
            percent = (difference / previous_seven) * 100
        except ZeroDivisionError:
            print(f"{state}: Previous 7-day avg was 0, cannot compute percentage change.")
            continue

        # Convert to integers for printing
        previous_seven = int(previous_seven)
        current_seven = int(current_seven)
        percent = int(percent)

        print(f"{state} has a 7-day average of {current_seven} and ", end="")
        if percent > 0:
            print(f"an increase of {percent}%.")
        else:
            print(f"a decrease of {abs(percent)}%.")
    return


main()
