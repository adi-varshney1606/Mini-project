import mysql.connector as ms
cn=ms.connect(host='localhost',username='root',passwd='',database='club')
if cn.is_connected():
    print("\t\t          🙏CONNECTION ESTABLISHED SUCCESSFULLY🙏")
    cr=cn.cursor()

print("\t\t1:Cricket🏏 ")
print("\t\t-----------------")
print("\t\t2:Football⚽")
print("\t\t------------------")
print("\t\t3:Badminton🏸 ")
print("\t\t-----------------------")
print("\t\t4:Swimming🏊")
print("\t\t--------------------") 
print("Choose the sports you want to opt for:-  ")
ch=int(input("\t\t\t\t "))
if ch==1:
    print("Welcome to the Cricket Portal")
    print("=========================")
    print("\n\tClub Cricket Coach:- Mr.J.P.Nair")
    print("\n\t---------------------------------")
    print("\t\t\t\t\t\t\t Contact no. :- 7985554016")
    print("\t\t\t\t\t\t\t ----------------------")
    print("\t\t1:To display coach details")
    print("\t\t---------------------------------------------------")
    print("\t\t2:To Register for Cricket Sport ")
    print("\t\t---------------------------------------------------")
    print("\t\t3:To display the Cricket equipments")
    print("\t\t------------------------------------------------------------")
    print("\t\t4:To display ground details ")
    print("\t\t---------------------------------------------")
    print("\t\t5:Exit")
    print("\t\t----------")
    c=int(input("Enter your choice:- "))
    if c==1:
        print("\t\t\t COACH DETAILS")
        print("\t\t\t ==============")
        print("\t\t Name:- \t\t Mr.J.P.Nair")
        print("\t\t ----------")
        print("\t\t Age:-    \t\t 35 years")
        print("\t\t -------")
        print("\t\t Gender:-       \t Male")
        print("\t\t -------------")
        print("\t\t Contact no:-\t9839037266")
        print("\t\t ------------------")
        print("\t\t Experience:-\t 8years \n\t\t\t\t {At National Sports Acaedmy}")
        print("\t\t -------------------")
    elif c==2:
        print("user_name:-")
        user_nam=input("\t  ")
        print("Phone_no:-")
        phone_no=input("\t  ")
        if len(phone_no)==10:
            pass
        else:
            print("invalid entry")
        r="insert into cregister values('%s','%s')" %(user_nam,phone_no)
        cr.execute(r)
        cn.commit()
        cn.close()
        print("Thanks For Your Visit Sir/Madam")
    elif c==3:
        print("The cricket Equipments are:- ")
        cr.execute("select item_name from cricket")
        for i in cr:
            print("\t\t","*",i,"*")
    elif c==4:
        co=input("enter your country:- ")
        if co=='india' or co=='INDIA':
            print("The ground is:-")
            print("\t\t Chacha Nehru Park")
            print("The pitch is 'hard' . The hard tracks is lively for both batsmen and bowlers.")
        elif co=='USA' or co=='usa':
            print("The ground is:-")
            print("\t\t George Victor Park")
            print("The pitch is 'flat' .The batsman is expected to hit a awesome score.")
        elif co=='PAKISTAN' or co=='pakistan':
            print("The ground is:-")
            print("\t\t Pak Star Ground, Malir")
            print("The pitch has 'green top' . The green-top is regarded as a paradise for fast bowlers.")
        elif co=='AUSTRALIA' or co=='australia':
            print("The ground is:-")
            print("\t\t Peter Potter Park")
            print("Known as:-\n\t North West Cricket Stadium Sedgars Park.")
            print("Potchefstroom Ends:-\n\t\t Cargo Motors End, University End")
            print("Location:-   \n\t Potchefstroom, Australia")
            print("Time Zone UTC:-    \n\t +02:00")
            print("\t\t Home to:- South Africa, North West")
            print("Floodlights:-\n\t\t Yes")
        elif co=='brazil' or co=='BRAZIL':
            print("The ground is:-")
            print("\t\t Imam minar Ground, Masaro")
            print("The pitch has 'green top' . The green-top is regarded as a paradise for fast bowlers.")
        else:
            print("\t\t\t\t SORRY!! ")
            print("Sorry!! No Cricket facilities in your country")
            print("We will try to provide our sports facilities in your area.")
    
elif ch==2:
    print("Welcome to the Football Portal")
    print("==========================")
    print("\nClub Football Coach:- Mr. Abhishek Pandey")
    print("\n----------------------------------")
    print("\t\t\t\t\t\t\t Contact no. :- 6388730259")
    print("\t\t\t\t\t\t\t ---------------------")
    print("\t\t1:To display coach details")
    print("\t\t---------------------------------------------------")            
    print("\t\t2:To Register for Football Sport ")
    print("\t\t-----------------------------------------------------")
    print("\t\t3:To display the Football equipments")
    print("\t\t------------------------------------------------------------")
    print("\t\t4:To display ground details ")
    print("\t\t---------------------------------------------")
    print("\t\t5:Exit")
    print("\t\t----------")
    c=int(input("Enter your choice:- "))
    if c==1:
        print("\t\t\t COACH DETAILS")
        print("\t\t\t ==============")
        print("\t\t Name:- \t\t Mr. Abhishek Pandey")
        print("\t\t ----------")
        print("\t\t Age:-    \t\t 32 years")
        print("\t\t -------")
        print("\t\t Gender:-       \t Male")
        print("\t\t -------------")
        print("\t\t Contact no:-\t9450340297")
        print("\t\t ------------------")
        print("\t\t Experience:-\t 8years \n\t\t\t\t {At National Sports Acaedmy}")
        print("\t\t -------------------")

    elif c==2:
        print("user_name:-")
        user_nam=input("\t  ")
        print("Phone_no:-")
        phone_no=input("\t  ")
        if len(phone_no)==10:
            pass
        else:
            print("invalid entry")
        r="insert into fregister values('%s','%s')" %(user_nam,phone_no)
        cr.execute(r)
        cn.commit()
        cn.close()
        print("Thanks For Your Visit Sir/Madam")
    elif c==3:
        print("The Football Equipments are:- ")
        cr.execute("select item_name from football")
        for i in cr:
            print("\t\t",i)
    elif c==4:
        co=input("enter your country:- ")
        if co=='india' or co=='INDIA':
            print("The ground is:-")
            print("\t\t Chacha Nehru Park")
        elif co=='USA' or co=='usa':
            print("The ground is:-")
            print("\t\t George Victor Park")
            print(" ")
        elif co=='PAKISTAN' or co=='pakistan':
            print("The ground is:-")
            print("\t\t Pak Star Ground, Malir")
            print(" ")
        elif co=='AUSTRALIA' or co=='australia':
            print("The ground is:-")
            print("\t\t Peter Potter Park")
        elif co=='brazil' or co=='BRAZIL':
            print("The ground is:-")
            print("\t\t imam minar Ground, Masaro")
            print(" ")
        else:
            print("Sorry!! No Football facilities in your country")
    
elif ch==3:
    print("Welcome to the Badminton Portal")
    print("==========================")
    print("\nClub Badminton Coach:- Mr. Abhishek Pandey")
    print("\n----------------------------------")
    print("\t\t\t\t\t\t\t Contact no. :- 6388730259")
    print("\t\t\t\t\t\t\t ---------------------")
    print("\t\t1:To display coach details")
    print("\t\t--------------------------------------------")
    print("\t\t2:To Register for Badminton Sport ")
    print("\t\t-------------------------------------------")
    print("\t\t3:To display the Badminton equipments")
    print("\t\t------------------------------------------------------------")
    print("\t\t4:To display ground details ")
    print("\t\t---------------------------------------------")
    print("\t\t5:Exit")
    print("\t\t----------")
    c=int(input("Enter your choice:- "))
    if c==1:
        print("\t\t\t COACH DETAILS")
        print("\t\t\t ==============")
        print("\t\t Name:- \t\t Mr. Abhishek Pandey")
        print("\t\t ----------")
        print("\t\t Age:-    \t\t 32 years")
        print("\t\t -------")
        print("\t\t Gender:-       \t Male")
        print("\t\t -------------")
        print("\t\t Contact no:-\t9450340297")
        print("\t\t ------------------")
        print("\t\t Experience:-\t 8years \n\t\t\t\t {At National Sports Acaedmy}")
        print("\t\t -------------------")
        
    elif c==2:
        print("user_name:-")
        user_nam=input("\t  ")
        print("Phone_no:-")
        phone_no=input("\t  ")
        if len(phone_no)==10:
            pass
        else:
            print("invalid entry")
        r="insert into bregister values('%s','%s')" %(user_nam,phone_no)
        cr.execute(r)
        cn.commit()
        cn.close()
        print("Thanks For Your Visit Sir/Madam")
    elif c==3:
        print("The Badminton Equipments are:- ")
        cr.execute("select item_name from badminton")
        for i in cr:
            print("\t\t",i)
    elif c==4:
        co=input("enter your country:- ")
        if co=='india' or co=='INDIA':
            print("The ground is:-")
            print("\t\t Chacha Nehru Park")
        elif co=='USA' or co=='usa':
            print("The ground is:-")
            print("\t\t George Victor Park")
            print(" ")
        elif co=='PAKISTAN' or co=='pakistan':
            print("The ground is:-")
            print("\t\t Pak Star Ground, Malir")
            print(" ")
        elif co=='AUSTRALIA' or co=='australia':
            print("The ground is:-")
            print("\t\t Peter Potter Park")
        elif co=='brazil' or co=='BRAZIL':
            print("The ground is:-")
            print("\t\t imam minar Ground, Masaro")
            print(" ")
        else:
            print("Sorry!! No Badminton facilities in your country")

elif ch==4:
    print("Welcome to the Swiming Portal")
    print("==========================")
    print("\nClub Swiming Coach:- Mr. Abhishek Pandey")
    print("\n----------------------------------")
    print("\t\t\t\t\t\t\t Contact no. :- 6388730259")
    print("\t\t\t\t\t\t\t ---------------------")
    print("\t\t1:To display coach details")
    print("\t\t-------------------------------------------")
    print("\t\t2:To Register for Swiming Sport ")
    print("\t\t-------------------------------------------")
    print("\t\t3:To display the Swiming equipments")
    print("\t\t------------------------------------------------------------")
    print("\t\t4:To display Pool details ")
    print("\t\t---------------------------------------------")
    print("\t\t5:Exit")
    print("\t\t----------")
    c=int(input("Enter your choice:- "))
    if c==1:
        print("\t\t\t COACH DETAILS")
        print("\t\t\t ==============")
        print("\t\t Name:- \t\t Mr. Abhishek Pandey")
        print("\t\t ----------")
        print("\t\t Age:-    \t\t 32 years")
        print("\t\t -------")
        print("\t\t Gender:-       \t Male")
        print("\t\t -------------")
        print("\t\t Contact no:-\t9450340297")
        print("\t\t ------------------")
        print("\t\t Experience:-\t 8years \n\t\t\t\t{At National Sports Acaedmy}")
        print("\t\t -------------------")
          
    elif c==2:
        print("user_name:-")
        user_nam=input("\t  ")
        print("Phone_no:-")
        phone_no=input("\t  ")
        if len(phone_no)==10:
            pass
        else:
            print("invalid entry")
        r="insert into sregister values('%s','%s')" %(user_nam,phone_no)
        cr.execute(r)
        cn.commit()
        cn.close()
        print("Thanks For Your Visit Sir/Madam")
    elif c==3:
        print("The Swiming Equipments are:- ")
        cr.execute("select item_name from swiming")
        for i in cr:
            print("\t\t",i)
    elif c==4:
        co=input("enter your country:- ")
        if co=='india' or co=='INDIA':
            print("The ground is:-")
            print("\t\t Chacha Nehru Pool")
        elif co=='USA' or co=='usa':
            print("The ground is:-")
            print("\t\t George Victor Pool")
            print(" ")
        elif co=='PAKISTAN' or co=='pakistan':
            print("The ground is:-")
            print("\t\t Pak Star pool, Malir")
            print(" ")
        elif co=='AUSTRALIA' or co=='australia':
            print("The ground is:-")
            print("\t\t Peter Potter Pool")
        elif co=='brazil' or co=='BRAZIL':
            print("The ground is:-")
            print("\t\t imam minar Ground, Masaro")
            print(" ")
        else:
            print("Sorry!! No Swiming facilities in your country")
    

