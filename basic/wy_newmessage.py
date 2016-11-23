message=input("input message")
new_msg=""
VOWELS="aeiou"

print()
for letter in message:
    if letter.lower() in VOWELS:
        new_msg += letter
        print("new msg:", new_msg)
        
print("new msg", new_msg)
