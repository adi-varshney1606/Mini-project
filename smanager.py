import mysql.connector as ms
d=input("enter database:-  ")     #club
n=input("enter username:-  ")    #root
cn=ms.connect(host='localhost',username=n,passwd='',database=d)
if cn.is_connected():
    print("\t\t          🙏CONNECTION ESTABLISHED SUCCESSFULLY🙏")
    cr=cn.cursor()
def dis():
    while True:
        print("\t Enter The Field You Want To Fetch The Records")
        print("\t\t 1.Cricket")
        print("\t\t 2.Football")
        print("\t\t 3.Badminton")
        print("\t\t 4.Exit")
        choice=int(input("\t\t Enter Your Choice:- "))
        if choice==1:
            cr.execute("select * from cricket")
            for i in cr:
                print(i)
        elif choice==2:
            cr.execute("select * from football")
            for i in cr:
                print(i)
        elif choice==3:
            cr.execute("select * from badminton")
            for i in cr:
                print(i)
        elif choice==4:
            break
def src():
    no=input("ENTER THE SERIAL.NO. OF THE ITEM YOU WANT TO SEARCH:- ")
    cr.execute("select * from sports where sno={}". format(no))
    for i in cr:
        print(i)
def stock():
    cr.execute("select item,count(*) from sports group by item") 
    for i in cr:
        print(i)
def mod():
    print("WELCOME TO THE UPDATE PORTAL")
    print("***********************************")
    print("select the sport to be updated:-")
    print("1- CRICKET ")
    print("2- FOOTBALL ")
    print("3- BADMINTON ")
    b=("Enter your choice:")
    print(b)
    d=int(input("\t\t"))
    if d==1:
        cr.execute("select * from cricket")
        for i in cr:
            print(i)
        print("What would you like to update in cricket")
        print("1-Cost")
        print("2-Quantity")
        c=int(input("Enter your choice:"))
        if c==1:
            print("Select The Item To be Updated:-")
            print("1-Bat ")
            print("2-Ball ")
            print("3-Keeper Glove ")
            print("4-Batsman Glove")
            print("5-keeper/Batsman Pads")
            print("6-Helmet ")
            print("7-Stumps ")
            print("8-Bails")
            a=int(input(" Enter your choice:-"))
            if a==1:
                cr.execute("select * from cricket where item_no=1")
                for i in cr:
                    print(i)
                print("Provide the New cost of bat")
                a=input()
                cr.execute("update cricket set item_cost={} where item_no=1".format(a))
                cr.execute("select * from cricket")
                for i in cr:
                    print(i)
            if a==2:
                cr.execute("select * from cricket where item_no=2")
                for i in cr:
                    print(i)
                print(" Provide the New cost of ball")
                a=input()
                cr.execute("update cricket set item_cost={} where item_no=2".format(a))
                cr.execute("select * from cricket")
                for i in cr:
                    print(i)
            if a==3:
                cr.execute("select * from cricket where item_no=3")
                for i in cr:
                    print(i)
                print(" Provide the New cost of Keeper Glove  ")
                a=input()
                cr.execute("update cricket set item_cost={} where item_no=3".format(a))
                cr.execute("select * from cricket")
                for i in cr:
                    print(i)
            if a==4:
                cr.execute("select * from cricket where item_no=4")
                for i in cr:
                    print(i)
                print(" Provide the New cost of Batsman Glove")
                a=input()
                cr.execute("update cricket set item_cost={} where item_no=4".format(a))
                cr.execute("select * from cricket")
                for i in cr:
                    print(i)
            if a==5:
                cr.execute("select * from cricket where item_no=5")
                for i in cr:
                    print(i)
                print(" Provide the New cost of Helmet ")
                a=input()
                cr.execute("update cricket set item_cost={} where item_no=5".format(a))
                cr.execute("select * from cricket")
                for i in cr:
                    print(i)
            if a==6:
                cr.execute("select * from cricket where item_no=6")
                for i in cr:
                    print(i)
                print(" Provide the New cost of Stumps")
                a=input()
                cr.execute("update cricket set item_cost={} where item_no=6".format(a))
                cr.execute("select * from cricket")
                for i in cr:
                    print(i)
            if a==7:
                cr.execute("select * from cricket where item_no=7")
                for i in cr:
                    print(i)
                print(" Provide the New cost of Bails ")
                a=input()
                cr.execute("update cricket set item_cost={} where item_no=7".format(a))
                cr.execute("select * from cricket")
                for i in cr:
                    print(i)
            if a==8:
                cr.execute("select * from cricket where item_no=8")
                for i in cr:
                    print(i)
                print(" Provide the New cost of ball")
                a=input()
                cr.execute("update cricket set item_cost={} where item_no=8".format(a))
                cr.execute("select * from cricket")
                for i in cr:
                    print(i)
        elif c==2:
            print("Select The Item To be Updated:-")
            print("1-Bat ")
            print("2-Ball ")
            print("3-Keeper Glove ")
            print("4-Batsman Glove")
            print("5-keeper/Batsman Pads")
            print("6-Helmet ")
            print("7-Stumps ")
            print("8-Bails")
            a=int(input(" Enter your choice:-"))
            if a==1:
                cr.execute("select * from cricket where item_no=1")
                for i in cr:
                    print(i)
                print("Provide the New quantity of bat")
                a=input()
                cr.execute("update cricket set item_stock={} where item_no=1".format(a))
                cr.execute("select * from cricket")
                for i in cr:
                    print(i)
            if a==2:
                cr.execute("select * from cricket where item_no=2")
                for i in cr:
                    print(i)
                print(" Provide the New quantity of ball")
                a=input()
                cr.execute("update cricket set item_stock={} where item_no=2".format(a))
                cr.execute("select * from cricket")
                for i in cr:
                    print(i)
            if a==3:
                cr.execute("select * from cricket where item_no=3")
                for i in cr:
                    print(i)
                print(" Provide the New quantity of Keeper Glove  ")
                a=input()
                cr.execute("update cricket set item_stock={} where item_no=3".format(a))
                cr.execute("select * from cricket")
                for i in cr:
                    print(i)
            if a==4:
                cr.execute("select * from cricket where item_no=4")
                for i in cr:
                    print(i)
                print(" Provide the New quantity of Batsman Glove")
                a=input()
                cr.execute("update cricket set item_stock={} where item_no=4".format(a))
                cr.execute("select * from cricket")
                for i in cr:
                    print(i)
            if a==5:
                cr.execute("select * from cricket where item_no=5")
                for i in cr:
                    print(i)
                print(" Provide the New quantity of Helmet ")
                a=input()
                cr.execute("update cricket set item_stock={} where item_no=5".format(a))
                cr.execute("select * from cricket")
                for i in cr:
                    print(i)
            if a==6:
                cr.execute("select * from cricket where item_no=6")
                for i in cr:
                    print(i)
                print(" Provide the New quantity of Stumps")
                a=input()
                cr.execute("update cricket set item_stock={} where item_no=6".format(a))
                cr.execute("select * from cricket")
                for i in cr:
                    print(i)
            if a==7:
                cr.execute("select * from cricket where item_no=7")
                for i in cr:
                    print(i)
                print(" Provide the New quantity of Bails ")
                a=input()
                cr.execute("update cricket set item_stock={} where item_no=7".format(a))
                cr.execute("select * from cricket")
                for i in cr:
                    print(i)
            if a==8:
                cr.execute("select * from cricket where item_no=8")
                for i in cr:
                    print(i)
                print(" Provide the New quantity of ball")
                a=input()
                cr.execute("update cricket set item_stock={} where item_no=8".format(a))
                cr.execute("select * from cricket")
                for i in cr:
                    print(i)
            
    elif d==2:
        cr.execute("select * from  football")
        for i in cr:
            print(i)
        print("What would you like to update in football")
        print("1-Cost")
        print("2-Quantity")
        c=int(input("Enter your choice:"))
        if c==1:
            print("Select The Item To be Updated:-")
            print("1- Helmet")
            print("2- Jockstrap ")
            print("3- mouth guard")
            print("4- Thigh Pad")
            print("5- knee Pad")
            print("6- Hip Pad")
            print("7- Shoulder Pads")
            print("8- Gloves")
            print("9- Cleats")
            print("10- Neck Collars")
            a=int(input(" Enter your choice:-"))
            if a==1:
                cr.execute("select * from football where item_no=1")
                for i in cr:
                    print(i)
                print("Provide the New cost of Helmet ")
                a=input()
                cr.execute("update football set item_cost={} where item_no=1".format(a))
                cr.execute("select * from football")
                for i in cr:
                    print(i)
            if a==2:
                cr.execute("select * from football where item_no=2")
                for i in cr:
                    print(i)
                print(" Provide the New cost of Jockstrap")
                a=input()
                cr.execute("update football set item_cost={} where item_no=2".format(a))
                cr.execute("select * from football")
                for i in cr:
                    print(i)
            if a==3:
                cr.execute("select * from football where item_no=3")
                for i in cr:
                    print(i)
                print(" Provide the New cost of  mouth guard ")
                a=input()
                cr.execute("update football set item_cost={} where item_no=3".format(a))
                cr.execute("select * from football")
                for i in cr:
                    print(i)
            if a==4:
                cr.execute("select * from football where item_no=4")
                for i in cr:
                    print(i)
                print(" Provide the New cost of Thigh Pad")
                a=input()
                cr.execute("update football set item_cost={} where item_no=4".format(a))
                cr.execute("select * from football")
                for i in cr:
                    print(i)
            if a==5:
                cr.execute("select * from football where item_no=5")
                for i in cr:
                    print(i)
                print(" Provide the New cost of knee Pad ")
                a=input()
                cr.execute("update football set item_cost={} where item_no=5".format(a))
                cr.execute("select * from football")
                for i in cr:
                    print(i)
            if a==6:
                cr.execute("select * from football where item_no=6")
                for i in cr:
                    print(i)
                print(" Provide the New cost of Hip Pad")
                a=input()
                cr.execute("update football set item_cost={} where item_no=6".format(a))
                cr.execute("select * from football")
                for i in cr:
                    print(i)
            if a==7:
                cr.execute("select * from football where item_no=7")
                for i in cr:
                    print(i)
                print(" Provide the New cost of Shoulder Pads ")
                a=input()
                cr.execute("update football set item_cost={} where item_no=7".format(a))
                cr.execute("select * from football")
                for i in cr:
                    print(i)
            if a==8:
                cr.execute("select * from football where item_no=8")
                for i in cr:
                    print(i)
                print(" Provide the New cost of Gloves ")
                a=input()
                cr.execute("update football set item_cost={} where item_no=8".format(a))
                cr.execute("select * from football")
                for i in cr:
                    print(i)
            if a==9:
                cr.execute("select * from football where item_no=9")
                for i in cr:
                    print(i)
                print(" Provide the New cost of Cleats")
                a=input()
                cr.execute("update football set item_cost={} where item_no=9".format(a))
                cr.execute("select * from football")
                for i in cr:
                    print(i)
            
            if a==10:
                cr.execute("select * from football where item_no=10")
                for i in cr:
                    print(i)
                print(" Provide the New cost of Neck Collars ")
                a=input()
                cr.execute("update football set item_cost={} where item_no=10".format(a))
                cr.execute("select * from football")
                for i in cr:
                    print(i)
        elif c==2:
            print("Select The Item To be Updated:-")
            print("1- Helmet")
            print("2- Jockstrap ")
            print("3- mouth guard")
            print("4- Thigh Pad")
            print("5- knee Pad")
            print("6- Hip Pad")
            print("7- Shoulder Pads")
            print("8- Gloves")
            print("9- Cleats")
            print("10- Neck Collars")
            a=int(input(" Enter your choice:-"))
            if a==1:
                cr.execute("select * from football where item_no=1")
                for i in cr:
                    print(i)
                print("Provide the New quantity of Helmet ")
                a=input()
                cr.execute("update football set item_stock={} where item_no=1".format(a))
                cr.execute("select * from football")
                for i in cr:
                    print(i)
            if a==2:
                cr.execute("select * from football where item_no=2")
                for i in cr:
                    print(i)
                print(" Provide the New quantity of Jockstrap")
                a=input()
                cr.execute("update football set item_stock={} where item_no=2".format(a))
                cr.execute("select * from football")
                for i in cr:
                    print(i)
            if a==3:
                cr.execute("select * from football where item_no=3")
                for i in cr:
                    print(i)
                print(" Provide the New quantity of  mouth guard ")
                a=input()
                cr.execute("update football set item_stock={} where item_no=3".format(a))
                cr.execute("select * from football")
                for i in cr:
                    print(i)
            if a==4:
                cr.execute("select * from football where item_no=4")
                for i in cr:
                    print(i)
                print(" Provide the New quantity of Thigh Pad")
                a=input()
                cr.execute("update football set item_stock={} where item_no=4".format(a))
                cr.execute("select * from football")
                for i in cr:
                    print(i)
            if a==5:
                cr.execute("select * from football where item_no=5")
                for i in cr:
                    print(i)
                print(" Provide the New quantity of knee Pad ")
                a=input()
                cr.execute("update football set item_stock={} where item_no=5".format(a))
                cr.execute("select * from football")
                for i in cr:
                    print(i)
            if a==6:
                cr.execute("select * from football where item_no=6")
                for i in cr:
                    print(i)
                print(" Provide the New quantity of Hip Pad")
                a=input()
                cr.execute("update football set item_stock={} where item_no=6".format(a))
                cr.execute("select * from football")
                for i in cr:
                    print(i)
            if a==7:
                cr.execute("select * from football where item_no=7")
                for i in cr:
                    print(i)
                print(" Provide the New quantity of Shoulder Pads ")
                a=input()
                cr.execute("update football set item_stock={} where item_no=7".format(a))
                cr.execute("select * from football")
                for i in cr:
                    print(i)
            if a==8:
                cr.execute("select * from football where item_no=8")
                for i in cr:
                    print(i)
                print(" Provide the New quantity of Gloves ")
                a=input()
                cr.execute("update football set item_stock={} where item_no=8".format(a))
                cr.execute("select * from football")
                for i in cr:
                    print(i)
            if a==9:
                cr.execute("select * from football where item_no=9")
                for i in cr:
                    print(i)
                print(" Provide the New quantity of Cleats")
                a=input()
                cr.execute("update football set item_stock={} where item_no=9".format(a))
                cr.execute("select * from football")
                for i in cr:
                    print(i)
            
            if a==10:
                cr.execute("select * from football where item_no=10")
                for i in cr:
                    print(i)
                print(" Provide the New quantity of Neck Collars ")
                a=input()
                cr.execute("update football set item_stock={} where item_no=10".format(a))
                cr.execute("select * from football")
                for i in cr:
                    print(i)

    elif d==3:
        cr.execute("select * from badminton")
        for i in cr:
            print(i)
        print("What would you like to update in  badminton")
        print("1-Cost")
        print("2-Quantity")
        c=int(input("Enter your choice:"))
        if c==1:
            print("Select The Item To be Updated:-")
            print("1- Badminton Racket ")
            print("2- Shuttlecock")
            print("3- Badminton shoes")
            print("4- Badminton Attire")
            print("5- Badminton net")
            a=int(input(" Enter your choice:-"))
            if a==1:
                cr.execute("select * from  badminton where item_no=1")
                for i in cr:
                    print(i)
                print("Provide the New cost of Badminton Racket")
                a=input()
                cr.execute("update  badminton set item_cost={} where item_no=1".format(a))
                cr.execute("select * from  badminton")
                for i in cr:
                    print(i)
            if a==2:
                cr.execute("select * from  badminton where item_no=2")
                for i in cr:
                    print(i)
                print(" Provide the New cost of Shuttlecock")
                a=input()
                cr.execute("update  badminton set item_cost={} where item_no=2".format(a))
                cr.execute("select * from  badminton")
                for i in cr:
                    print(i)
            if a==3:
                cr.execute("select * from  badminton where item_no=3")
                for i in cr:
                    print(i)
                print(" Provide the New cost of Badminton shoes  ")
                a=input()
                cr.execute("update  badminton set item_cost={} where item_no=3".format(a))
                cr.execute("select * from  badminton")
                for i in cr:
                    print(i)
            if a==4:
                cr.execute("select * from  badminton where item_no=4")
                for i in cr:
                    print(i)
                print(" Provide the New cost of Badminton Attire ")
                a=input()
                cr.execute("update  badminton set item_cost={} where item_no=4".format(a))
                cr.execute("select * from  badminton")
                for i in cr:
                    print(i)
            if a==5:
                cr.execute("select * from  badminton where item_no=5")
                for i in cr:
                    print(i)
                print(" Provide the New cost of Badminton net ")
                a=input()
                cr.execute("update  badminton set item_cost={} where item_no=5".format(a))
                cr.execute("select * from  badminton")
                for i in cr:
                    print(i)
            
        elif c==2:
            print("Select The Item To be Updated:-")
            print("1- Badminton Racket ")
            print("2- Shuttlecock")
            print("3- Badminton shoes")
            print("4- Badminton Attire")
            print("5- Badminton net")
            a=int(input(" Enter your choice:-"))
            if a==1:
                cr.execute("select * from  badminton where item_no=1")
                for i in cr:
                    print(i)
                print("Provide the New quantity of Badminton Racket")
                a=input()
                cr.execute("update  badminton set item_stock={} where item_no=1".format(a))
                cr.execute("select * from  badminton")
                for i in cr:
                    print(i)
            if a==2:
                cr.execute("select * from  badminton where item_no=2")
                for i in cr:
                    print(i)
                print(" Provide the New quantity of Shuttlecock")
                a=input()
                cr.execute("update  badminton set item_stock={} where item_no=2".format(a))
                cr.execute("select * from  badminton")
                for i in cr:
                    print(i)
            if a==3:
                cr.execute("select * from  badminton where item_no=3")
                for i in cr:
                    print(i)
                print(" Provide the New quantity of Badminton shoes  ")
                a=input()
                cr.execute("update  badminton set item_stock={} where item_no=3".format(a))
                cr.execute("select * from  badminton")
                for i in cr:
                    print(i)
            if a==4:
                cr.execute("select * from  badminton where item_no=4")
                for i in cr:
                    print(i)
                print(" Provide the New quantity of Badminton Attire ")
                a=input()
                cr.execute("update  badminton set item_stock={} where item_no=4".format(a))
                cr.execute("select * from  badminton")
                for i in cr:
                    print(i)
            if a==5:
                cr.execute("select * from  badminton where item_no=5")
                for i in cr:
                    print(i)
                print(" Provide the New quantity of Badminton net ")
                a=input()
                cr.execute("update  badminton set item_stock={} where item_no=5".format(a))
                cr.execute("select * from  badminton")
                for i in cr:
                    print(i)
            
        
print("PRESS Y TO CONTINUE")
Y=input("\t\t   ")
while Y=='y' or Y=='Y':
    print("\t\t\t    WELCOME TO SPORTS MANAGER's PORTAL")
    print("\t\t\t*********************************************")
    print("\t\t1:Display all records")
    print("\t\t----------------------------------")
    print("\t\t2:Search a record")
    print("\t\t-----------------------------")
    print("\t\t3:Check The Stock")
    print("\t\t------------------------------------------") 
    print("\t\t4:Modify The stock")
    print("\t\t------------------------------------") 
    print("\t\t5:Exit from the program")
    print("\t\t---------------------------------------")
    choice=int(input("ENTER YOUR CHOICE:- "))
    if choice==1:
        print("You have choosen to display the records")
        print("=======================================")
        print(dis())               
        print("PRESS Y TO CONTINUE")
        Y=input("\t\t   ")
        if Y=='y'or Y =='Y':
            pass
        else:
            print("Wrong Key Entered")
            break

    elif choice==2:
        print("You have choosen to search the record")
        print("==================================")
        print(src())                  
        print("PRESS Y TO CONTINUE")
        Y=input("\t\t   ")
        if Y=='y'or Y =='Y':
            pass
        else:
            print("Wrong Key Entered")
            break

    elif choice==3:
        print("You have choosen to check the stock")
        print("===============================")
        print(stock())                
        print("PRESS Y TO CONTINUE")
        Y=input("\t\t   ")
        if Y=='y'or Y =='Y':
            pass
        else:
            print("Wrong Key Entered")
            break

    elif choice==4:
        print("You have choosen to modify the records")
        print("=================================")
        print(mod())
        cn.commit()
        print("PRESS Y TO CONTINUE")
        Y=input("\t\t   ")
        if Y=='y'or Y =='Y':
            pass
        else:
            print("Wrong Key Entered")
            break

    elif choice==5:
        print("THANK YOU SIR !!")
        print("================")                         
        break
