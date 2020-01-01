import random

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','{','}','[',']','=','+','-',
         '_','/','.',';',':','?','<','>','\'','|','\\']

passwordlength = int(input("Enter desired length of password: "))
num_letters = int(input("Enter the amount of characters you wish to include: "))


password = ""
        
symbolsornot = input("Would you like to include special characters in your password? Answer Y or N: ")
if symbolsornot == "Y":        
    num_numbers = int(input("Enter the amount of numbers you wish to include: "))
    num_symbols = passwordlength - (num_letters + num_numbers)
    while num_symbols != 0:
        password = password + random.choice(symbols)
        num_symbols -= 1
if symbolsornot == "N":
    num_numbers = passwordlength - num_letters
            
while passwordlength != len(password):
    while num_letters != 0:
        password = password + random.choice(alphabet)
        num_letters -= 1
    while num_numbers != 0:
        password = password + random.choice(numbers)
        num_numbers -= 1



password_list=list(password)
random.shuffle(password_list)
password="".join(password_list)
print("Your generated password is:" + password)