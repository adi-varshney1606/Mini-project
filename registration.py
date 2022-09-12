import mysql.connector as ms
d="club"   
n="root"    
cn=ms.connect(host='localhost',username=n,passwd='',database=d)
if cn.is_connected():
    print("\t\t          🙏CONNECTION ESTABLISHED SUCCESSFULLY🙏")
    cr=cn.cursor()
import random
try:
    Member_no=random.randint(1,1000)
    print("Your member number is:- ",Member_no) 
    print("user_name:-")
    user_nam=input("\t  ")
    print("Country:-")
    Country=input("\t  ")
    print("State:-")
    State=input("\t  ")
    print("City:-")
    City=input("\t  ")
    print("Phone_no:-")
    phone_no=input("\t  ")
    if len(phone_no)==10:
        pass
    else:
        print("invalid entry")
    print("Email_id:-")
    email_id=input("\t ")
    if len(email_id)>7 and email_id[-10:]=='@gmail.com' or email_id[-10:]=='@yahoo.com':
        pass
    else:
        print("invalid email_id ")
        print("Try Again!!")
        print("Email_id:-")
        email_id=input("\t ")
        if len(email_id)>7 and email_id[-10:]=='@gmail.com' or email_id[-10:]=='@yahoo.com':
            pass
        else:
            print("INVALID EMAIL-ID")
            
    print("Passward:-")
    print("Please keep a 7 character password")
    passwad=input("\t  ")
    if len(passwad)==7:
        pass
    else:
        print("Incorrect Passward")

    r="insert into registration values('%s','%s','%s','%s','%s','%s','%s','%s')" %(Member_no,user_nam,Country,State,City,phone_no,email_id,passwad)
    cr.execute(r)
    cn.commit()
except:
    print("This Member Number Already Exist")
    print("PLEASE TRY Again")
cn.close()
print("Thanks For Your Visit Sir/Madam")

