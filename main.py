# PİZZA ORDER PRİCE CALCULATOR

print("Please place your order : ")
extra_cheese = input('Do you want extra cheese? "YES" or "NO" ')
drink = input('Do you want drink? "YES" or "NO" ')
size = input('What size pizza do you want? "S", "M" or "L" ')

account = 0
if size =="S":
    account += 20
elif size == "M" :
    account += 25
else:
    account += 30
if extra_cheese == "YES" :
    if size ==  "S" :
        account += 2
    else:
        account += 3
if drink == "YES" :
    account += 2
print(f"Total account : {account} TL.")
