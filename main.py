import random


def equal_shares(votes, k):
    # Calculating the total number of votes
    n = sum(votes.values())

    # A dictionary for the number of seats each party has
    government = {party: 0 for party in votes.keys()}

    # The budget each supporter of a party has for that party
    budget_per_voter = {party: (k / n) for party in votes.keys()}

    # The price of a candidate
    candidate_price = 1

    # The price each supporter of a party has to pay for a candidate
    price_per_voter = {party: candidate_price / votes[party] for party in votes.keys()}

    # The number of seats allocated thus far
    seats_allocated = 0

    while seats_allocated < k:
        # Selecting all the parties whose voters can afford a seat
        affordable_party = [party for party in votes.keys() if budget_per_voter[party] >= price_per_voter[party]]

        # Breaking the loop if no supporter can afford their party
        if len(affordable_party) == 0:
            break

        # Selecting the cheapest affordable candidate
        cheapest_party = min(affordable_party, key=lambda party: price_per_voter[party])

        # Deducting the price per voter from the budget of the voters for the party
        budget_per_voter[cheapest_party] -= price_per_voter[cheapest_party]

        # Allocating a seat for the party
        seats_allocated += 1
        government[cheapest_party] += 1

    # Giving away the remaining seats randomly
    while seats_allocated < k:
        government[random.choice(list(government.keys()))] += 1
        seats_allocated += 1

    # Ordering the parties by the number of seats
    government = dict(sorted(government.items(), key=lambda x: x[1], reverse=True))

    # Printing the results
    for party in government.keys():
        print(party, ":", government[party])
    print(sum(government.values()))


def phragmen(votes, k):
    # Calculating the total number of votes
    n = sum(votes.values())

    # A dictionary for the number of seats each party has
    government = {party: 0 for party in votes.keys()}

    # The current budget each voter for a party has
    budget_per_voter = {party: 0 for party in votes.keys()}

    # The price per candidate
    candidate_price = 1

    # The total number of seats allocated
    seats_allocated = 0

    # The amount of money each voter gets per loop.
    # I chose 1/n because it's a very small growth rate that resulted in accurate results
    growth_rate = 1 / n

    while seats_allocated < k:
        # Distributing the money among the voters
        for party in votes.keys():
            budget_per_voter[party] += growth_rate

        # Selecting all the parties whose voters can afford a seat
        affordable_party = [party for party in votes.keys() if budget_per_voter[party]*votes[party] >= candidate_price]

        # Skipping a loop if no affordable party exists
        if len(affordable_party) == 0:
            continue

        # Giving the seat to the party with the most budget that can afford a candidate
        chosen_party = max(affordable_party, key=lambda party: budget_per_voter[party])
        seats_allocated += 1
        government[chosen_party] += 1

        # Resting the budget
        budget_per_voter[chosen_party] = 0

    # Ordering the parties by the number of seats
    government = dict(sorted(government.items(), key=lambda x: x[1], reverse=True))

    # Printing the results
    for party in government.keys():
        print(party, ":", government[party])
    print(sum(government.values()))


if __name__ == '__main__':
    votes = {
        "Likud": 1115336, "Yesh Atid": 847435, "HaTzionut HaDatit": 516470, "National Unity": 432482, "Shas": 392964,
        "United Torah Judaism": 280194, "Yisrael Beiteinu": 213687, "United Arab List": 194047,
        "Hadash - Ta'al": 178735, "Labor": 175992
    }
    k = 120

    print("phragmen:")
    phragmen(votes, k)

    print("\nequal_shares:")
    equal_shares(votes, k)
