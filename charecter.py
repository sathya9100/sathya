#Take input from the user
char=input("Enter a single charecter :")
#check if the input is a single charecter
if len(char)!=1:
      print("Please enter only one charecter!")
else:
    #check if the charecter is a digit
    if char.isdigit():
          print(f"'{char}' is a digit.")
    #check if the chareter is a lowercase letter
    elif char.islower():
          print(f"'{char}'is a lowercase charecter.")
    #check if the charecter is an uppercase letter
    elif char.isupper():
          print(f"'{char}'is an uppercase charecter.")
    #if none of the above,it is a special charecter
    else:
          print("'{char}'is a special charecter.")
