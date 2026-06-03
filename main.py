user = str(input('Enter your name : '))
password = input('Enter your passowrd : ')

pas_strength = len(password)

if(1 <=  pas_strength <= 7):
    print(f'''Dear {user} password rating is 4/10 
please select a strong password
Account hack chnaces are high with this password ({password}) ''')   

elif(8 <= pas_strength <= 13):
    print(f'''Dear {user} password rating is 8/10,
You may can choose a strong password 
or continue with this password ({password}) ''')

elif(14 <= pas_strength <=20):
    print(f'''Dear {user} password rating is 10/10, 
You can continue with this password ({password}) ''')
    
else:
    print('something went wrong')

