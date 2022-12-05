import csv
import os



_location_ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def open_file():
    with open(os.path.join(_location_,'associations.csv')) as csv_file:
        a_list = []
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 1
        for row in csv_reader:
            #print(row)
            a_list.append(row)
            print(a_list)
            
            


open_file()
#print(lol)