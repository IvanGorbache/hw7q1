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

    # List of parties whose supporters can afford a candidate
    affordable_party = list()

    
    while seats_allocated < k:
        for party in votes.keys():
            if budget_per_voter[party] * votes[party] >= candidate_price:
                affordable_party.append(party)
        if len(affordable_party) == 0:
            break
        cheapest_party = affordable_party[0]
        for party in affordable_party:
            if price_per_voter[party] <= price_per_voter[cheapest_party]:
                cheapest_party = party
        budget_per_voter[cheapest_party] -= price_per_voter[cheapest_party]
        seats_allocated += 1
        government[cheapest_party] += 1
        affordable_party.clear()

    government = dict(sorted(government.items(), key=lambda x: x[1], reverse=True))
    government[list(government.keys())[0]] += k - seats_allocated

    for party in government.keys():
        print(party, ":", government[party])
    print(sum(government.values()))


def phragmen(votes, k):
    n = sum(votes.values())
    government = {party: 0 for party in votes.keys()}
    budget_per_voter = {party: 0 for party in votes.keys()}
    candidate_price = 1
    seats_allocated = 0
    growth_rate = 1 / n

    while seats_allocated < k:
        for party in votes.keys():
            budget_per_voter[party] += growth_rate
        for party in votes.keys():
            if budget_per_voter[party] * votes[party] >= candidate_price:
                seats_allocated += 1
                government[party] += 1
                budget_per_voter[party] = 0

    government = dict(sorted(government.items(), key=lambda x: x[1], reverse=True))
    government[list(government.keys())[0]] += k - seats_allocated

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
