from art import logo
print(logo)

people = {}

restart = True
while restart:

    username = input("What is your name?: ")
    amount = int(input("What is your bid?: $"))
    people[username] = amount
    print(people)

    highest_bid = 0
    winner = ""
    answer = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if answer == "no":
        restart = False
    else:
        print("\n"* 100)

        for bidding in people:
            bid_amount = people[bidding]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = bidding
print(f"The winner is {winner} with a bid of {highest_bid}.")