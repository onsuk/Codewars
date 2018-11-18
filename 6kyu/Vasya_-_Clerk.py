'''
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line.
Each of them has a single 100, 50 or 25 dollars bill. An "Avengers" ticket costs 25 dollars.
Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?
Return YES, if Vasya can sell a ticket to each person and give the change with the bills he has at hand at that moment. Otherwise return NO.

Examples:
tickets([25, 25, 50]) # => YES 
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
'''


# def tickets(people):
#     change = 0
#     for bill in people:
#         if bill == 25:
#            change += 25
#         elif bill == 50:
#            change -= 25
#            if change < 0: return "NO"
#         elif bill == 100:
#           change -= 75
#           if change < 0 : return "NO"
#     if change >= 0: return "YES"


def tickets(people):
    change = []
    for bill in people:
        if bill == 25: change.append(25)
        elif bill == 50:
            if change.count(25) >= 1:
                change.remove(25)
                change.append(50)
            else: return "NO"
        elif bill == 100:
            if change.count(50) >= 1:
                if change.count(25) >= 1:
                    change.remove(25)
                    change.remove(50)
                else: return "NO"
            elif change.count(25) >= 3:
                change.remove(25)
                change.remove(25)
                change.remove(25)
            else: return "NO"
    return "YES"