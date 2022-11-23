

def print_dart():
    with open("dart.txt") as file_obj:
        dart_list = [line for line in file_obj]
    for element in dart_list:
        print(element, end="")
    print()
    

    

print_dart()