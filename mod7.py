from datetime import datetime
year = 2021
month = 12
day = 26
date = datetime(year, month, day)
date_search_from = datetime(2021, 12, 10)
date_search_to = datetime(2021, 12, 31)
if date_search_from <= date <= date_search_to:
    print("date inbetween")
else:
    print("date out of range")
date_search_to = datetime(2021, 12, 1)
if date_search_from <= date <= date_search_to:
    print("date inbetween")
else:
    print("date out of range")
