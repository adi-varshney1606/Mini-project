import mysql.connector as ms
d=input("enter database:-  ")     #club
n='root'
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

def src():
    no=input("ENTER THE SERIAL NO. OF THE EMPLOYEE YOU WANT TO SEARCH:- ")
    cr.execute("select * from staff where sno={}". format(no))
    for i in cr:
        print()
        print("Name Of The Employee Is","\t\t\t\t",                       i[1])
        print()
        print("Designation Of The Employee Is","\t\t\t\t" ,               i[2])
        print()
        print("Joining Date Of The Employee Is","\t\t\t\t",             i[3])
        print()
        print("Monthly Salary Of The Employee Is","\t\t\t\t",             i[4])
        print()
        print("Contact Of The Employee Is","\t\t\t\t",             i[5])
        print()
def sc():
    def repeat():
        cr.execute("select designation,count(*) from staff group by designation") 
        print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
        for i in cr:
            n=0
            a=1
            print("‖",i[n],"►",i[a]," ")
            print("◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊")
            n=n+1
            a=a+1
    repeat()
print("PRESS Y TO PROCEED ")
Y=input("\t\t")
while Y=='y' or Y=='Y':
    print("\t\t\t    WELCOME TO PRESIDENT's PORTAL")
    print("\t\t\t***********************************")
    print("\t\t1:Club Profits/Losses")
    print("\t\t----------------------------------")
    print("\t\t2:Display all records")
    print("\t\t----------------------------------")
    print("\t\t3:Search a record")
    print("\t\t-----------------------------")
    print("\t\t4:Display The Staff Count")
    print("\t\t------------------------------------------") 
    print("\t\t5:Exit from the program")
    print("\t\t---------------------------------------")
    choice=int(input("ENTER YOUR CHOICE:- "))
    if choice==1:
        print("You have choosen to calculate the income")
        print("========================================")
        print(prof())
        print("PRESS Y TO CONTINUE")
        Y=input("\t\t   ")
        if Y=='y'or Y =='Y':
            pass
        else:
            print("Wrong Key Entered")
            break
        
    elif choice==2:
        print("You have choosen to display all the records")
        print("====================================")
        print(dis())                  
        print("PRESS Y TO CONTINUE")
        Y=input("\t\t   ")
        if Y=='y'or Y =='Y':
            pass
        else:
            print("Wrong Key Entered")
            break

    elif choice==3:
        print("You have choosen to search the record")
        print("================================")
        print(src())                
        print("PRESS Y TO CONTINUE")
        Y=input("\t\t   ")
        if Y=='y'or Y =='Y':
            pass
        else:
            print("Wrong Key Entered")
            break

    elif choice==4:
        print("You have choosen to display the staff count")
        print("====================================")
        print(sc())                
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
