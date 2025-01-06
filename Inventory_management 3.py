import mysql.connector as myconn
from tabulate import tabulate
conn=myconn.connect(host='localhost', user='root', passwd='123456')
curr=conn.cursor()
curr.execute('create database if not exists CS_Project;')
curr.execute('use CS_Project;')

#Creating Stock Table
curr.execute('create table if not exists stock (Product_no int(5) not null, voucher_no int(10) not null, Dealer_name varchar(50), Voucher_date Date not null, Type varchar(20) not null, Sub_type varchar(20), Rate int(10) not null, Tax int(5) not null, Net_amount int(10) not null, Quantity int(10) not null, primary key (product_no,voucher_no))')
#Creating Condemnation Table
curr.execute('create table if not exists condemnation (Product_no int(5), voucher_no int(10), Dealer_name varchar(50), Type varchar(20) not null, Sub_type varchar(20), Quantity int(5), Condemn_date date)')
#Creating Issue Table
curr.execute('create table if not exists issue (Product_no int(5), voucher_no int(10), Type varchar(20) not null, Sub_type varchar(20), Teacher_name varchar(30), Quantity int(4) not null, Issue_date date not null, Return_date date)')


def add_stocks():                                                                             #Add values to stock table
    n=int(input("Enter number of entries:"))
    for i in range(n):
        Pr_no=input("Enter Product number: ")
        Vo_no=input("Enter Voucher number: ")
        D_name=input("Enter Dealer name:")
        Vo_date=input("Enter Voucher date (in YYYY-MM-DD): ")
        Type=input("Enter component\'s type: ")
        Sub_type=input("Enter component\'s sub type (if any): ")
        Rate=input("Enter price of component (in rs): ")
        Tax= input("Enter tax applied on component (in rs): ")
        Net=input("Enter Net amount (in rs): ")
        Qty=input("Enter quantity of component ordered: ")
        Tuple=(Pr_no,Vo_no,D_name,Vo_date,Type,Sub_type,Rate,Tax,Net,Qty)
        curr.execute("insert into stock values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",Tuple)
        conn.commit()
    print("The provided values have been added to the STOCK table")

def add_issue():                                                                      #Add values to issue table
    n=int(input("Enter number of entries:"))
    for i in range(n):
        Pr_no=input("Enter Product number: ")
        Vo_no=input("Enter Voucher number: ")
        Type=input("Enter component\'s type: ")
        Sub_type=input("Enter component\'s sub type (if any): ")
        teach_name=input("Enter teacher's name whom you want to issue: ")
        Qty=input("Enter quantity of component issued: ")
        issue_date=input("Enter issue date (in YYYY-MM-DD): ")
        return_date=input("Enter return date (in YYYY-MM-DD): ")
        Tuple=(Pr_no,Vo_no,Type,Sub_type,teach_name,Qty,issue_date,return_date)
        curr.execute("insert into issue values (%s,%s,%s,%s,%s,%s,%s,%s)",Tuple)
        conn.commit()
    print("The provided values have been added to the ISSUE table")    

def add_condemn():                                                                      #Add values to condemn table
    n=int(input("Enter number of entries:"))
    for i in range(n):
        Pr_no=input("Enter Product number: ")
        Vo_no=input("Enter Voucher number: ")
        D_name=input("Enter Dealer name:")
        Type=input("Enter component\'s type: ")
        Sub_type=input("Enter component\'s sub type (if any): ")
        Qty=input("Enter quantity of component ordered: ")
        Co_date=input("Enter Voucher date (in YYYY-MM-DD): ")
        Tuple=(Pr_no,Vo_no,D_name,Type,Sub_type,Qty,Co_date)
        curr.execute("insert into condemnation values (%s,%s,%s,%s,%s,%s,%s)",Tuple)
        conn.commit()
    print("The provided values have been added to the CONDEMNATION table")    

def update_stocks():                                                                      #Update Stock Table
    choose=input("Enter product number of component whose entries you want to update: ")
    print("Fields in Stock table are:\n1. Product_no\n2. voucher_no\n3.Dealer_name\n4. Voucher_date\n5. Type\n6. Sub_type\n7. Rate\n8. Tax\n9. Net Amount\n10. Quantity\n")
    field=int(input("Enter field number whose value you want to update: "))

    if field==1:                                                                                #To Update Product number
        pr=input("Enter new product number: ")
        curr.execute("update stock set Product_no=%s where product_no=%s",(pr,choose))
        conn.commit()
        print("Product number of the component has been updated.")

    elif field==2:                                                                             #To Update Voucher number
        vr=input("Enter new voucher number: ")
        curr.execute("update stock set voucher_no=%s where product_no=%s",(vr,choose))
        conn.commit()
        print("Voucher number of the component has been updated.")

    elif field==3:                                                                             #To Update Type
        tr=input("Enter new Dealer\'s  name: ")
        curr.execute("update stock set Dealer_name=%s where product_no=%s",(t,choose))
        conn.commit()
        print("Dealer's name has been updated.")    

    elif field==4:                                                                             #To Update Voucher date
        vd=input("Enter new voucher_date (in YYYY-MM-DD): ")
        curr.execute("update stock set voucher_date=%s where product_no=%s",(vd,choose))
        conn.commit()
        print("Voucher date of the component has been updated.")

    elif field==5:                                                                              #To Update Type
        t=input("Enter new type of component: ")
        curr.execute("update stock set type=%s where product_no=%s",(t,choose))
        conn.commit()
        print("Type of the component has been updated.")

    elif field==6:                                                                              #To Update Sub_type
        st=input("Enter new sub_type of component: ")
        curr.execute("update stock set type=%s where product_no=%s",(st,choose))
        conn.commit()
        print("Sub_Type of the component has been updated.")

    elif field==7:                                                                              #To Update Rate
        ra=input("Enter new rate of component: ")
        curr.execute("update stock set rate=%s where product_no=%s",(ra,choose))
        conn.commit()
        print("Rate of the component has been updated.")

    elif field==8:                                                                              #To Update Tax
        vd=input("Enter new tax of component: ")
        curr.execute("update stock set tax=%s where product_no=%s",(vd,choose))
        conn.commit()
        print("Tax of the component has been updated.")

    elif field==9:
        v=input("Enter new net amount of component: ")                  #To Update Net_amount
        curr.execute("update stock set net_amount=%s where product_no=%s",(v,choose))

    elif field==10:                                                                             #To Update Quantity
        vd=input("Enter new quantity of component: ")
        curr.execute("update stock set qty=%s where product_no=%s",(vd,choose))
        conn.commit()
        print("Quantity of the component has been updated.")


def update_condemn():                                                                 #Update Condemnation Table
    choose=input("Enter product number of component whose entries you want to update: ")
    print("Fields in Stock table are:\n1. Product_no\n2. voucher_no\n3. Dealer_name\n4. Type\n5. Sub_type\n6. Quantity\n7. Condemn_date\n")
    field=int(input("Enter field number whose value you want to update: "))

    if field==1:                                                                                #To Update Product number
        pr=int(input("Enter new product number: "))
        curr.execute("update condemnation set Product_no=%s where product_no=%s",(pr,choose))
        conn.commit()
        print("Product number of the component has been updated.")

    elif field==2:                                                                             #To Update Voucher number
        vr=int(input("Enter new voucher number: "))
        curr.execute("update condemnation set voucher_no=%s where product_no=%s",(vr,choose))
        conn.commit()
        print("Voucher number of the component has been updated.")

    elif field==3:                                                                             #To Update Type
        tr=input("Enter new Dealer\'s  name: ")
        curr.execute("update condemnation set Dealer_name=%s where product_no=%s",(t,choose))
        conn.commit()
        print("Dealer's name has been updated.")    

    elif field==4:                                                                              #To Update Type
        t=input("Enter new type of component: ")
        curr.execute("update condemnation set type=%s where product_no=%s",(t,choose))
        conn.commit()
        print("Type of the component has been updated.")

    elif field==5:                                                                              #To Update Sub_type
        st=input("Enter new sub_type of component: ")
        curr.execute("update condemnation set type=%s where product_no=%s",(st,choose))
        conn.commit()
        print("Sub_Type of the component has been updated.")

    elif field==6:                                                                             #To Update Quantity
        vd=int(input("Enter new quantity of component: "))
        curr.execute("update condemnation set qty=%s where product_no=%s",(vd,choose))
        conn.commit()
        print("Quantity of the component has been updated.")

    elif field==7:                                                                             #To Update Voucher date
        vd=int(input("Enter new condemn_date (in YYYY-MM-DD): "))
        curr.execute("update condemnation set condemn_date=%s where product_no=%s",(vd,choose))
        conn.commit()
        print("Voucher date of the component has been updated.")


def update_issue():                                                                        #Update Issue Table
    choose=input("Enter product number of component whose entries you want to update: ")
    print("Fields in Issue table are:\n1. Product_no\n2. voucher_no\n3. Type\n4. Sub_type\n5. Teacher_name\n6. Quantity\n7. Issue_date\n8. Return_date\n")
    field=int(input("Enter field number whose value you want to update: "))

    if field==1:                                                                                #To Update Product number
        pr=int(input("Enter new product number: "))
        curr.execute("update stock set Product_no=%s where product_no=%s",(pr,choose))
        conn.commit()
        print("Product number of the component has been updated.")

    elif field==2:                                                                             #To Update Voucher number
        vr=int(input("Enter new voucher number: "))
        curr.execute("update issue set voucher_no=%s where product_no=%s",(vr,choose))
        conn.commit()
        print("Voucher number of the component has been updated.")

    elif field==3:                                                                              #To Update Type
        t=input("Enter new type of component: ")
        curr.execute("update issue set type=%s where product_no=%s",(t,choose))
        conn.commit()
        print("Type of the component has been updated.")

    elif field==4:                                                                              #To Update Sub_type
        st=input("Enter new sub_type of component: ")
        curr.execute("update issue set type=%s where product_no=%s",(st,choose))
        conn.commit()
        print("Sub_Type of the component has been updated.")

    elif field==5:                                                                             #To Update Teacher's name
        tr=input("Enter new Teacher\'s  name: ")
        curr.execute("update issue set teacher_name=%s where product_no=%s",(t,choose))
        conn.commit()
        print("Teacher's name has been updated.")  

    elif field==6:                                                                             #To Update Quantity
        vd=int(input("Enter new quantity of component: "))
        curr.execute("update issue set qty=%s where product_no=%s",(vd,choose))
        conn.commit()
        print("Quantity of the component has been updated.")

    elif field==7:                                                                             #To Update Condemn date
        vd=int(input("Enter new condemn_date (in YYYY-MM-DD): "))
        curr.execute("update issue set condemn_date=%s where product_no=%s",(vd,choose))
        conn.commit()
        print("Condemn date of the component has been updated.")
        
  
def options(pie):                                                                                #NIkhil ka DImaag--1
        print("1. For One Entry \n 2. For Number of entries \n 3. For all entries\n")
        wish=int(input("Enter your choice:"))
        if wish==1:
            a=curr.fetchone()
            b=[]
            b.append(a)
            print(tabulate(b,headers=pie,tablefmt='psql'))
        elif wish==2:
            n=int(input("Enter number of entries you want to fetch: "))
            tup=curr.fetchmany(n)
            print(tabulate(tup,headers=pie,tablefmt='psql'))
        elif wish==3:
            tup=curr.fetchall()
            print(tabulate(tup,headers=pie,tablefmt='psql'))

stockc=['Product_no','voucher_no','Dealer_name','Voucher_date','Type','Sub_type','Rate','Tax','Net amount','Quantity']    
def search_stocks():                                                                        #Search Stocks
    print("Fields in Stock table are:\n1. Product_no\n2. voucher_no\n3.Dealer_name\n4. Voucher_date\n5. Type\n6. Sub_type\n7. Rate\n8. Tax\n9. Quantity\n")
    choose=int(input("Enter field number using which you want to search data: "))

    if choose==1:                                                                            #To search from Product number
        pr=int(input("Enter product number of component whose details you want to search: "))
        curr.execute("select * from stock where product_no=%s",(pr,))
        a=curr.fetchall()
        print(tabulate(a,headers=['Product_no','voucher_no','Dealer_name','Voucher_date','Type','Sub_type','Rate','Tax','Net amount','Quantity'],tablefmt='psql'))

    elif choose==2:                                                                         #To search from Voucher number
        pr=int(input("Enter voucher number of component whose details you want to search: "))
        curr.execute("select * from stock where voucher_no=%s",(pr,))
        a=curr.fetchone()
        b=[]
        b.append(a)
        print(tabulate(b,headers=['Product_no','voucher_no','Dealer_name','Voucher_date','Type','Sub_type','Rate','Tax','Net amount','Quantity'],tablefmt='psql'))

    elif choose==3:                                                                         #To search from Dealer name
        pr=input("Enter dealer name whose details you want to search: ")
        curr.execute("select * from stock where dealer_name=%s",(pr,))
        options(stockc)

    elif choose==4:                                                                         #To search from Voucher_Date
        pr=input("Enter Voucher date of product(s) you want to search (in YYYY-MM-DD format): ")
        curr.execute("select * from stock where voucher_date=%s",(pr,))
        options(stockc)

    elif choose==5:                                                                         #To search from Type
        pr=input("Enter type of product whose details you want to search: ")
        curr.execute("select * from stock where type=%s",(pr,))
        options(stockc)

    elif choose==6:                                                                         #To search from sub type
        pr=input("Enter sub_type of product whose details you want to search: ")
        curr.execute("select * from stock where sub_type=%s",(pr,))
        options(stockc)
        
    elif choose==7:                                                                         #To search from rate
        pr=input("Enter rate of product whose details you want to search: ")
        curr.execute("select * from stock where rate=%s",(pr,))
        options(stockc)

    elif choose==8:
        pr=input("Enter tax of product whose details you want to search: ")
        curr.execute("select * from stock where tax=%s",(pr,))
        options(stockc)

    elif choose==9:
        pr=input("Enter Quantity of product whose details you want to search: ")
        curr.execute("select * from stock where qty=%s",(pr,))
        options(stockc)


condemnc=['Product_no','Voucher_no','Dealer_name','Type','Sub_type','Quantity','Condemn_date']    
def search_condemn():
    print("Fields in Stock table are:\n1. Product_no\n2. voucher_no\n3. Dealer_name\n4. Type\n5. Sub_type\n6. Quantity\n7. Condemn_date\n")
    choose=int(input("Enter field number using which you want to search data: "))

    if choose==1:                                                                            #To search from Product number
        pr=int(input("Enter product number of component whose details you want to search: "))
        curr.execute("select * from condemnation where product_no=%s",(pr,))
        a=curr.fetchone()
        b=[]
        b.append(a)
        print(tabulate(b,headers=['Product_no','Voucher_no','Dealer_name','Type','Sub_type','Quantity','Condemn_date']  ,tablefmt='psql'))

    elif choose==2:                                                                         #To search from Voucher number
        pr=int(input("Enter voucher number of component whose details you want to search: "))
        curr.execute("select * from condemnation where voucher_no=%s",(pr,))
        a=curr.fetchone()
        b=[]
        b.append(a)
        print(tabulate(b,headers=['Product_no','Voucher_no','Dealer_name','Type','Sub_type','Quantity','Condemn_date'],tablefmt='psql'))

    elif choose==3:                                                                         #To search from Dealer name
        pr=input("Enter dealer name whose details you want to search: ")
        curr.execute("select * from condemnation where dealer_name=%s",(pr,))
        options(condemnc)

    elif choose==4:                                                                         #To search from Type
        pr=input("Enter type of product whose details you want to search: ")
        curr.execute("select * from condemnation where type=%s",(pr,))
        options(condemnc)

    elif choose==5:                                                                          #To search from Sub_type
        pr=input("Enter sub_type of product whose details you want to search: ")
        curr.execute("select * from condemnation where sub_type=%s",(pr,))
        options(condemnc)
        
    elif choose==6:                                                                         #To search from Quantity
        pr=int(input("Enter Quantity of product whose details you want to search: "))
        curr.execute("select * from condemnation where qty=%s",(pr,))
        options(condemnc)

    elif choose==7:                                                                         #To search from Condemn_Date
        pr=input("Enter Condemn date of product(s) you want to search (in YYYY-MM-DD format): ")
        curr.execute("select * from condemnation where condemn_date=%s",(pr,))
        options(condemnc)    

issuec=['Product_no','voucher_no','Type','Sub_type','Teacher_name','Quantity','Issue_date','Return_date']
def search_issue():
    print("Fields in Issue table are:\n1. Product_no\n2. voucher_no\n3. Type\n4. Sub_type\n5. Teacher_name\n6. Quantity\n7. Issue_date\n8. Return_date\n")
    choose=int(input("Enter field number using which you want to search data: "))

    if choose==1:                                                                            #To search from Product number
        pr=int(input("Enter product number of component whose details you want to search: "))
        curr.execute("select * from issue where product_no=%s",(pr,))
        a=curr.fetchone()
        b=[]
        b.append(a)
        print(tabulate(b,headers=['Product_no','voucher_no','Type','Sub_type','Teacher_name','Quantity','Issue_date','Return_date'],tablefmt='psql'))

    elif choose==2:                                                                         #To search from Voucher number
        pr=int(input("Enter voucher number of component whose details you want to search: "))
        curr.execute("select * from issue where voucher_no=%s",(pr,))
        a=curr.fetchone()
        b=[]
        b.append(a)
        print(tabulate(b,headers=['Product_no','voucher_no','Type','Sub_type','Teacher_name','Quantity','Issue_date','Return_date'],tablefmt='psql'))

    elif choose==3:                                                                         #To search from Type
        pr=input("Enter type of product whose details you want to search: ")
        curr.execute("select * from issue where type=%s",(pr,))
        options(issuec)

    elif choose==4:                                                                        #To search from sub type  
        pr=input("Enter sub_type of product whose details you want to search: ")
        curr.execute("select * from issue where sub_type=%s",(pr,))
        options(issuec)

    elif choose==5:                                                                         #To search from Teacher name
        pr=input("Enter Teacher\'s name whose details you want to search: ")
        curr.execute("select * from issue where teacher_name=%s",(pr,))
        options(issuec)

    elif choose==6:                                                                     
        pr=input("Enter Quantity of product whose details you want to search: ")
        curr.execute("select * from issue where qty=%s",(pr,))
        options(issuec)    
        
    elif choose==7:                                                                         #To search from Issue_Date
        pr=input("Enter issue date of product(s) you want to search (in YYYY-MM-DD format): ")
        curr.execute("select * from issue where issue_date=%s",(pr,))
        options(issuec)

    elif choose==7:                                                                         #To search from Return_Date
        pr=input("Enter return date of product(s) you want to search (in YYYY-MM-DD format): ")
        curr.execute("select * from issue where return_date=%s",(pr,))
        options(issuec)


def del_issue():
    print("Fields in Issue table are:\n1. Product_no\n2. voucher_no\n3. Type\n4. Sub_type\n5. Teacher_name\n6. Quantity\n7. Issue_date\n8. Return_date\n")
    choose=int(input("Enter field number using which you want to delete data: "))

    if choose==1:
        pr=input("Enter product number whose data you want to delete: ")
        curr.execute("delete from issue where product_no=%s",(pr,))
        conn.commit()
        print("The data has been deleted")

    elif choose==2:
        pr=int(input("Enter voucher number whose data you want to delete: "))
        curr.execute("delete from issue where voucher_no=%s",(pr,))
        conn.commit()
        print("The data has been deleted")

    elif choose==3:
        pr=input("Enter type of component whose data you want to delete: ")
        curr.execute("delete from issue where type=%s",(pr,))
        conn.commit()
        print("The data has been deleted")

    elif choose==4:
        pr=input("Enter sub type of component whose data you want to delete: ")
        curr.execute("delete from issue where sub_type=%s",(pr,))
        conn.commit()
        print("The data has been deleted")

    elif choose==5:
        pr=input("Enter teacher's name whose data you want to delete: ")
        curr.execute("delete from issue where teacher_name=%s",(pr,))
        conn.commit()
        print("The data has been deleted")

    elif choose==6:
        pr=int(input("Enter quantity whose data you want to delete: "))
        curr.execute("delete from issue where qty=%s",(pr,))
        conn.commit()
        print("The data has been deleted")

    elif choose==7:
        pr=input("Enter issue date whose data you want to delete (in YYYY-MM-DD): ")
        curr.execute("delete from issue where issue_date=%s",(pr,))
        conn.commit()
        print("The data has been deleted")
        
    elif choose==8:
        pr=input("Enter return date whose data you want to delete (in YYYY-MM-DD): ")
        curr.execute("delete from issue where return_date=%s",(pr,))
        conn.commit()
        print("The data has been deleted")


def display_stock():
    curr.execute("select * from stock")
    a=curr.fetchall()
    print(tabulate(a,headers=['Product_no','voucher_no','Dealer_name','Voucher_date','Type','Sub_type','Rate','Tax','Net amount','Quantity'],tablefmt='psql'))


def display_condemn():
    curr.execute("select * from condemnation")
    a=curr.fetchall()
    print(tabulate(a,headers=['Product_no','Voucher_no','Dealer_name','Type','Sub_type','Quantity','Condemn_date'],tablefmt='psql'))    


def display_issue():
    curr.execute("select * from issue")
    a=curr.fetchall()
    print(tabulate(a,headers=issuec,tablefmt='psql'))    

print("----------------------------------------------------INVENTORY MANAGEMENT----------------------------------------------------".center(100))
y="n"

while y=="n":
    print("\n\n-----------------MAIN MENU-----------------")
    print("\n1 for Stocks \t\t 2 for Condemnation \t\t 3 for issue \t\t 4 to end")
    u=int(input ("Enter the table number you wish to use: "))
    i=0
    while i==0:
        if u==1:
            print("\n--------------------------------------------------------- STOCK TABLE ---------------------------------------------------------")
            print("1 for Inserting Data into the Stock table.\n2 for Updating the Data in Stock table.\n3 for Searching or Displaying data of Stock table.\n4 to display whole table \n5 to go back")
            q=int(input("Enter your choice: "))
            if q==1:
                add_stocks()
            elif q==2:
               update_stocks()
            elif q==3:
                search_stocks()
            elif q==4:
                display_stock()
            else:
                i=i+1
        elif u==2:
            print("\n--------------------------------------------------------- CONDEMNATION TABLE ---------------------------------------------------------")
            print("1 for Inserting Data into the Condemnation table.\n2 for Updating the Data in Condemnation table.\n3 for Searching or Displaying data of Condemnation table.\n4 to display whole condemnation table\n5 to go back")
            q=int(input("Enter your choice: "))
            if q==1:
                add_condemn()
            elif q==2:
                update_condemn()
            elif q==3:
                search_condemn()
            elif q==4:
                display_condemn()
            else:
                i=i+1
        elif u==3:
            print("\n--------------------------------------------------------- ISSUE TABLE ---------------------------------------------------------")
            print("1 for Inserting Data into the Issue table.\n2 for Updating the Data in Issue table.\n3 for Searching or Displaying data of Issue table.\n4 to display whole issue table.\n5 for deleting data from Issue table.\n6 to go back ")
            q=int(input("Enter your choice: "))
            if q==1:
                add_issue()
            elif q==2:
                update_issue()
            elif q==3:
                search_issue()
            elif q==4:
                display_issue()
            elif q==5:
                del_issue()
            else:
               i=i+1

        elif u==4:
            y=input("Do you really wish to end the program (y or n): ")
            i=i+1
