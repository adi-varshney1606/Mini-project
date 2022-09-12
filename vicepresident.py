import mysql.connector as ms
d=input("enter database:-  ")     #club
n=input("enter username:-  ")    #root
cn=ms.connect(host='localhost',username=n,passwd='',database=d)
if cn.is_connected():
    print("\t\t          🙏CONNECTION ESTABLISHED SUCCESSFULLY🙏")
    cr=cn.cursor()
def prof():
    print("\t\t\tWELCOME TO THE INCOME PORTAL ")
    print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t\t 1.To display the investment / month")
    print("\t\t 2.To display the investment in the year 2020")
    print("\t\t 3.To display the profit in the year 2020")
    n=int(input("Enter your choice"))
    if n==1:
        cr.execute("select sum(salary) from staff")
        for i in cr:
            print("The Total salary of the staff is:-",i[0],"/month")
            c=int(i[0])
        v=5000
        print("The total electricity bill is",v,"rupees/Month")  
        x=c+v
        print("The total investment per month is:-",x,"rupees")
    elif n==2:
        import twenty
    elif n==3:
        
        cr.execute("select sum(salary) from staff")
        for i in cr:
            c=int(i[0])
        v=5000
        
        x=c+v
        from kharcha import g
        Y=g-x
        print("\t\t\t TOTAL PROFIT MADE IS",Y,"rupees")
        

def dis():
    cr.execute("select * from staff") 
    for i in cr:
        print(i)
def dis1():
    cr.execute("select * from registration") 
    for i in cr:
        print(i)
def src():
    print("1: To Search Staff Records")
    print("2: To Search Member Records")
    ch=int(input("Enter Your Choice:- "))
    if ch==1:
        no=input("ENTER THE SERIAL.NO. OF THE EMPLOYEE YOU WANT TO SEARCH:- ")
        cr.execute("select * from staff where sno={}". format(no))
        for i in cr:
            print(i)
    elif ch==2:
        no=input("ENTER THE MEMBER.NO. OF THE MEMBER YOU WANT TO SEARCH:- ")
        cr.execute("select * from registration where Member_no={}". format(no))
        for i in cr:
            print(i)

def sc():
    cr.execute("select designation,count(*) from staff group by designation") 
    for i in cr:
        print(i)
def mod():
    print("Abhi Banana baki hai")

print("PRESS Y TO CONTINUE")
Y=input("\t\t   ")
while Y=='y' or Y=='Y':
    print("\t\t\t    WELCOME TO VICE-PRESIDENT's PORTAL")
    print("\t\t\t***********************************")
    print("\t\t1:Club Profits/Losses")
    print("\t\t----------------------------------")
    print("\t\t2:Display all records of the staff")
    print("\t\t----------------------------------------------------")
    print("\t\t3:Display all records of the Members")
    print("\t\t------------------------------------------------------------")
    print("\t\t4:Search a record")
    print("\t\t-----------------------------")
    print("\t\t5:Display The Staff Count")
    print("\t\t------------------------------------------") 
    print("\t\t6:Modify The Records")
    print("\t\t------------------------------------") 
    print("\t\t7:Exit from the program")
    print("\t\t---------------------------------------")
    choice=int(input("ENTER YOUR CHOICE:- "))
    if choice==1:
        print("You have choosen to add new  records to the file")
        print("=======================================")
        print(prof())
        print("PRESS Y TO CONTINUE")
        Y=input("\t\t   ")
        if Y=='y'or Y =='Y':
            pass
        else:
            print("Wrong Key Entered")
            break

    elif choice==2:
        print("You have choosen to display all the records of the staff")
        print("=============================================")
        print(dis())                  
        print("PRESS Y TO CONTINUE")
        Y=input("\t\t   ")
        if Y=='y'or Y =='Y':
            pass
        else:
            print("Wrong Key Entered")
            break

    elif choice==3:
        print("You have choosen to display all the records of the Members")
        print("=================================================")
        print(dis1())                  
        print("PRESS Y TO CONTINUE")
        Y=input("\t\t   ")
        if Y=='y'or Y =='Y':
            pass
        else:
            print("Wrong Key Entered")
            break

    elif choice==4:
        print("You have choosen to search the record")
        print("===============================")
        print(src())                
        print("PRESS Y TO CONTINUE")
        Y=input("\t\t   ")
        if Y=='y'or Y =='Y':
            pass
        else:
            print("Wrong Key Entered")
            break

    elif choice==5:
        print("You have choosen to display the staff count")
        print("================================")
        print(sc())                
        print("PRESS Y TO CONTINUE")
        Y=input("\t\t   ")
        if Y=='y'or Y =='Y':
            pass
        else:
            print("Wrong Key Entered")
            break

    elif choice==6:
        print("You have choosen to modify the record")
        print("================================")
        print(mod())                
        print("PRESS Y TO CONTINUE")
        Y=input("\t\t   ")
        if Y=='y'or Y =='Y':
            pass
        else:
            print("Wrong Key Entered")
            break

    elif choice==7:
        print("THANK YOU SIR !!")
        print("================")                         
        break
