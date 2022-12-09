teams = ["Team1", "Team2", "Team3", "Team4", "Team5", "Team6"]
if len(teams) % 2:
    teams.append('Day off')
n = len(teams)
matchs = []
fixtures = []
return_matchs = []
for fixture in range(1, n):
    for i in range(n/2):
        matchs.append((teams[i], teams[n - 1 - i]))
        return_matchs.append((teams[n - 1 - i], teams[i]))
    teams.insert(1, teams.pop())
    fixtures.insert(len(fixtures)/2, matchs)
    fixtures.append(return_matchs)
    matchs = []
    return_matchs = []

for fixture in fixtures:
    print (fixture)



# from datetime import datetime
# year = 2021
# month = 12
# day = 26
# date = datetime(year, month, day)
# date_search_from = datetime(2021, 12, 10)
# date_search_to = datetime(2021, 12, 31)
# if date_search_from <= date <= date_search_to:
#     print("date inbetween")
# else:
#     print("date out of range")
# date_search_to = datetime(2021, 12, 1)
# if date_search_from <= date <= date_search_to:
#     print("date inbetween")
# else:
#     print("date out of range")
