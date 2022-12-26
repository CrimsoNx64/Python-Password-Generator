# Password generator
# Made by crimson :)


import random
import string

repeat = 1

def start():
    site=input("Enter site for password to generate for: ")
    main(site)

def main(site):
    global repeat
    generate()
    print("")
    password=''.join(random.sample(result_overall,len(result_overall)))
    file=open(site+".txt","a")
    file.write(password)
    file.close
    print("Password generated!")
    print("Password is:",password,"and is stored in",site,".txt text file!")
    repeat=int(input("Generate another password? 1 = yes, 2 = no "))
    
    
    
def generate():
    global result_overall
    result_overall=""
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    num=["1","2","3","4","5","6","7","8","9","0"]
    for i in range (0,5):
        result_low= ''.join(random.choice(lower))
        result_up= ''.join(random.choice(upper))
        result_num= ''.join(random.choice(num))
        result_overall=result_overall + result_low + result_up + result_num


while repeat == 1:
    start()





