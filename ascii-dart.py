import time

def get_dart_list():
    with open("dart.txt") as file_obj:
        return [line.replace("\n", "") for line in file_obj]
    
dart = get_dart_list()
for i, line in enumerate(dart):
    if i < 16:
        time.sleep(0.1)
        print(line)
    elif i >= 16 and i < 29:
        time.sleep(0.3)
        print(line)
    else:
        time.sleep(0.05)
        print(line)

input("Press enter")
print()
print()
print()
print("JEEEEBOOOOYYYYYY")