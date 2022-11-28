import time

def print_frontpage():
    with open("dart.txt") as file_obj:
        dart =  [line.replace("\n", "") for line in file_obj]
    for i, line in enumerate(dart):
        if i < 16:
            time.sleep(0)
            print(line)
        elif i >= 16 and i < 29:
            time.sleep(0)
            print(line)
        else:
            time.sleep(0)
            print(line)
    input("Please press enter")