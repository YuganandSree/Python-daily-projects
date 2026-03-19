# TODO-1: Ask the user for input
import art
print(art.logo)

def compare_fun(bidding_dict):
    winning_bid = 0
    winner = ""
    for bidder in bidding_dict:
        bidding_amount = bidding_dict[bidder]
        if bidding_amount > winning_bid:
            winning_bid = bidding_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${winning_bid}.")

bidding_dict = {}
continue_bidding = True
while continue_bidding:
    name = input("Please enter your name: ")
    price = int(input("Please enter your bid: "))
    # TODO-2: Save data into dictionary {name: price}

    bidding_dict[name] = price

    # TODO-3: Whether if new bids need to be added

    new_bids = input("Are there any new bids enter 'yes' else enter 'no' to complete the bidding: ").lower()

    if new_bids == "no":
        continue_bidding = False
        compare_fun(bidding_dict)
    elif new_bids == "yes":
        print("\n" *100)


# TODO-4: Compare bids in dictionary
