import random
import array
print("\t\t\t\t\t\t\t\t**********WELCOME**********\n")
print("\t\t\t\t********YOU CAN CHECK THE STRENGTH OF YOUR PASSWORD AND GENERATE STRONG PASSWORD*******\n")
choice=0
while (choice!=4):
    print("Press 1 to genetare password \nPress 2 to check strength of password \nPress 3 to exit\n")
    choice=int(input("Enter your choice:"))
    if (choice==1):
        max=int(input("\nEnter the maximum length of password:"))
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
        upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
        symblos= ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']

        passwd= numbers+ lower_case + upper_case+ symblos

        rand_digit = random.choice(numbers)
        rand_upper = random.choice(upper_case)
        rand_lower = random.choice(lower_case)
        rand_symbol = random.choice(symblos)

        temp_passwd = rand_digit + rand_upper + rand_lower + rand_symbol
        for x in range(max- 4):
            temp_passwd = temp_passwd + random.choice(passwd)
            passwd_list= array.array('u', temp_passwd)
            random.shuffle(passwd_list)
        password = ""
        for x in passwd_list:
            password = password + x
        print("\nSuggested password:",password)
        print("\n\n\t\t\t\t\t\t\t*********************************************")
    if(choice==2):
        l, u, p, d = 0, 0, 0, 0
        pwd= input("\nEnter password:")
        if (len(pwd) >= 8):
            for i in pwd:
                if (i.islower()):
                    l+=1
                if (i.isupper()):
                    u+=1
                if (i.isdigit()):
                    d+=1
                if(i=='@' or i=='#'or i=='$'or i=='%'or i=='='or i==':'or i=='?'or i=='.'or i=='/'or i=='|'or i=='~'or i=='>'or i=='*'or i=='('or i==')'or i=='<'):
                    p+=1
        if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(pwd)):
            print("\nStrong Password")
        else:
            print("\nWeak Password")
        print("\n\n\t\t\t\t\t\t\t*********************************************")
    if(choice==3):
        break
    
    


