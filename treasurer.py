import mysql.connector as ms
d=input("enter database:-  ")     #club
cn=ms.connect(host='localhost',username="root",passwd='',database=d)
if cn.is_connected():
    print("\t\t          🙏CONNECTION ESTABLISHED SUCCESSFULLY🙏")
    cr=cn.cursor()
def dis():
    cr.execute("select * from staff") 
    for i in cr:
        print(i)
def dis1():
    cr.execute("select ename,salary from staff")
    for i in cr:
        print(i)
    print("The total salary of the staff is:- ")
    cr.execute("select sum(salary) from staff")
    for i in cr:
        print(i)

def exp():
     cr.execute("select sum(salary) from staff")
     for i in cr:
         print("The Total salary of the staff is:-",i[0],"/month")
         c=int(i[0])
     v=5000
     print("The total electricity bill is",v,"rupees/Month")  
     x=c+v
     print("The total investment per month is:-",x,"rupees")
   
def inc():
    from kharcha import g
    print("THE TOTAL INCOME IS:", g)
def profit():
        cr.execute("select sum(salary) from staff")
        for i in cr:
            c=int(i[0])
        v=5000
        
        x=c+v
        from kharcha import g
        Y=g-x
        print("\t\t\t TOTAL PROFIT MADE IS",Y,"rupees")

print("PRESS Y TO CONTINUE")
Y=input("\t\t   ")
while True:
    print("\t\t\t    WELCOME TO TREASURER's PORTAL")
    print("\t\t\t    ************************************")
    print("\t\t1:Display all records")
    print("\t\t----------------------------------")
    print("\t\t2:Total Salary of staff")
    print("\t\t------------------------------------")
    print("\t\t3:Total Expenditure")
    print("\t\t---------------------------------")
    print("\t\t4:Total Income")
    print("\t\t-------------------------") 
    print("\t\t5:Total Profits")
    print("\t\t------------------------") 
    print("\t\t6:Exit from the program")
    print("\t\t---------------------------------------")
    choice=int(input("ENTER YOUR CHOICE:- "))
    if choice==1:
        print("You have choosen to display all  records")
        print("==================================")
        print(dis())               
        print("PRESS Y TO CONTINUE")
        Y=input("\t\t   ")
        if Y=='y'or Y =='Y':
            pass
        else:
            print("Wrong Key Entered")
            break

    elif choice==2:
        print("You have choosen to display the total salary of the staff")
        print("==============================================")
        print(dis1())               
        print("PRESS Y TO CONTINUE")
        Y=input("\t\t   ")
        if Y=='y'or Y =='Y':
            pass
        else:
            print("Wrong Key Entered")
            break

    elif choice==3:
        print("You have choosen to display the total expenditure")
        print("==========================================")
        print(exp())                  
        print("PRESS Y TO CONTINUE")
        Y=input("\t\t   ")
        if Y=='y'or Y =='Y':
            pass
        else:
            print("Wrong Key Entered")
            break

    elif choice==4:
        print("You have choosen to display the total income")
        print("=====================================")
        print(inc())                

        print("PRESS Y TO CONTINUE")
        Y=input("\t\t   ")
        if Y=='y'or Y =='Y':
            pass
        else:
            print("Wrong Key Entered")
            break
    elif choice==5:
        print("You have choosen to display the total profits")
        print("=====================================")
        print(profit())                                
        print("PRESS Y TO CONTINUE")
        Y=input("\t\t   ")
        if Y=='y'or Y =='Y':
            pass
        else:
            print("Wrong Key Entered")
            break

    elif choice==6:
        print("THANK YOU SIR !!")
        print("================")                         
        break
