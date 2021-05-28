import mysql.connector
from mysql.connector import Error


class Employee:
    def insert(self,m,n,o):
        try:
            mydb = mysql.connector.connect(host="127.0.0.1", port=3306, user="root", passwd="", database="mydb2222")
            cursor = mydb.cursor()
            query = "insert into employee(name,address,salary) values(%s,%s,%s)"
            values = [(m,n,o)]
            cursor.executemany(query,values)
            mydb.commit()
            print("Registered succesfully!!")
        except Error as e:
            print("Error while connecting to database",e)
        finally:
            print("Finished master!!!!")
    def update(self,x,y):
        try:
            mydb = mysql.connector.connect(host="127.0.0.1", port=3306, user="root", passwd="", database="mydb2222")
            cursor = mydb.cursor()
            sql = "update employee set address=%s where name=%s"
            var = [(x,y)]
            cursor.executemany(sql,var)
            mydb.commit()
            print("Updated Succesfully!!")
        except Error as e:
            print("Error while connecting to database!!",e)
        finally:
            print("Finished Master!!!!")
    def search(self,x):
        try:
            mydb = mysql.connector.connect(host="127.0.0.1", port=3306, user="root", passwd="", database="mydb2222")
            cursor = mydb.cursor()
            sql = "select * from employee where name=%s"
            drv = [(x)]
            cursor.execute(sql,drv)
            results = cursor.fetchall()
            for x in results:
                print(x)
            print("Searched succesfully!!")
        except Error as e:
            print("Error while connecting to database!!",e)
        finally:
            print("Finished Master!!!")
    def delrect(self,y):
        try:
            mydb = mysql.connector.connect(host="127.0.0.1", port=3306, user="root", passwd="", database="mydb2222")
            cursor = mydb.cursor()
            sql = "delete from employee where name=%s"
            varia = [(y)]
            cursor.execute(sql,varia)
            mydb.commit()
            print(cursor.rowcount," Records deleted")
        except Error as e:
            print("Error while connecting to database!!",e)
        finally:
            print("Finished master!!!")
choice =''
while choice != 'q':
    print("Enter 1 to insert\t")
    print("Enter 2 to update\t")
    print("Enter 3 to Search\t")
    print("Enter 4 to delete\t")
    print("Enter q to quit\t")
    choice = input("Please enter the choices")
    if choice == '1':
        a = input("Enter Name:\t")
        b = input("Enter address:\t")
        c = input("Enter salary:\t")
        obj = Employee()
        obj.insert(a,b,c)
    elif choice == '2':
        d = input("Enter name:\t")
        e = input("Enter address:\t")
        obj = Employee()
        obj.update(d,e)
    elif choice == '3':
        f = input("Enter name:\t")
        obj = Employee()
        obj.search(f)
    elif choice == '4':
        g = input("Enter name:\t")
        obj = Employee()
        obj.delrect(g)
    elif choice == 'q':
        print("Thanks for performing the operations!!")
    else:
        print("Invalid option")




