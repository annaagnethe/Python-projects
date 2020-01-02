import random

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
words=['tomato','abroad','accept','action','actual','author','avenue','attend','beauty','barely','before','belief','battle','beyond','center','casual','chosen',
         'castle','choose','circle','closed','client','credit','degree','deputy','danger','decade','desire','direct','domain','driven','detail','double','easily','editor','emerge','effect','enginge','equity','excess','expect','fabric','fairly','factor','figure','flight','follow','fought','friend','future','golden','growth','handle','happen','health','honest','impact','indeed','import','intend','junior','latest','launch','league','leader','legacy','living','mainly','margin','matter','memory','minute','modern','moment','modest','museum','mutual','nation','nearly','notice','object','origin','output','palace','permit','phrase','plenty','please','profit','rather','rarely','rating','recent','relate','regard','relief','remove','result','retail','rescue','review','ruling','sample','safety','screen','search','settle','senior','signed','silten','slight','source','status','square','struck','submit','summer','supply','switch','tenant','though','treaty','twelve','twenty','united','update','unique','unlike','valley','varied','volume','visual','vision','wealth','weekly','winner','winter','wonder','writer','within','yellow']

passwordlength = int(input("Enter desired length of password: "))
num_numbers = int(input("Enter the amount of numbers you wish to include: "))

password = ""

wordornot = input("Would you like to include a six-letter word in your password? Answer Y or N: ")
if wordornot == "Y":        
    num_letters = passwordlength - num_numbers - 6
    num_words = passwordlength - (num_letters + num_numbers)
    while num_words >= 6:
        password = password + random.choice(words)
        num_words -= 6
if wordornot == "N":
    num_letters = passwordlength - num_numbers    
            
while passwordlength != len(password):
    while num_numbers != 0:
        password = password + random.choice(numbers)
        num_numbers -= 1
    while num_letters != 0:
        password = password + random.choice(alphabet)
        num_letters -= 1
    

password_list=list(password)
password="".join(password_list)
print("Your generated password is:" + password)