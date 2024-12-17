def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3): #range(3):
        #The isdecimal() method in Python checks whether all characters in a string are decimal characters. 
        # If the string contains only decimal characters (0-9), it returns True, otherwise, it returns False1.
        if not text[i].isdecimal():
            return False
    
    if text[3] != "-":
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    
    if text[7] != "-":
        return False
    for i in range(8,10):
        if not text[i].isdecimal():
            return False
    
    return True

user_input = input("Enter your phone number: ")
if isPhoneNumber(user_input):
    print(f"{user_input} is a phone number.")
else:
    print(f"{user_input} is a not phone number.")

# Moshi moshi
# 415-555-4242