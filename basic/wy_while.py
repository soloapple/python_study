print("\tWelcome to the 'Three-Year-Old Simulator'\n")
print("This program simulates a conversation with a three-year-old child.")
print("Try to stop the madness.\n")
counter=0
while counter <= 10:
    print (counter)
    counter += 1

response = ""
while response != "Because.":
    response = input("Why?\n")
print("Oh. Okay.")
input("\n\nPress the enter key to exit.")

count = 0
while True:
    count += 1
    if count > 10:
        break
    if count == 5:
        continue
    print(count)
