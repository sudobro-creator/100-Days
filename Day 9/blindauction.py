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



#Method 2
# from art import logo
# print(logo)


# def find_highest_bidder(bidding_record):
#     highest_bid = 0
#     winner = ""
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of ${highest_bid}")


# bids = {}
# continue_bidding = True
# while continue_bidding:
#     name = input("What is your name?: ")
#     price = int(input("What is your bid?: $"))
#     bids[name] = price
#     should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#     if should_continue == "no":
#         continue_bidding = False
#         find_highest_bidder(bids)
#     elif should_continue == "yes":
#         print("\n" * 20)
