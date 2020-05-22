import sqlite3

def creatdb():
    
    
    con = sqlite3.connect('Customers.db')
    print("Created database successfully!")
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print("SQLite version: {}".format(data))
    return con



def createTable(con):

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Customers")
    cur.execute("CREATE TABLE Customers(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name VARCHAR(25),Lastname VARCHAR(25), Email text, DOB text, Address VARCHAR(25));")
    print('Customers Table created')

def insertTable(con):

    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Customers(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name VARCHAR(25),Lastname VARCHAR(25), Email text, DOB text, Address VARCHAR(25));")
    Name = input("Enter Your Name: ")
    Lastname = input("Enter Your Lastname Name: ")
    Email = input("Enter Your Email: ")
    DOB = input("Enter Your DOB: ")
    Address = input("Enter Your Address: ")
    cur.execute("INSERT INTO Customers(Name, Lastname, Email, DOB, Address) VALUES (?, ?, ?, ?, ?)",(Name, Lastname, Email, DOB, Address))
    print("Record Inserted")
        

def retrieveTable(con):

    cur = con.cursor()
    con.row_factory = sqlite3.Row
    cur.execute("SELECT * FROM Customers")

    rows = cur.fetchall()
    for row in rows:
        if row == None:
            print('Please Insert Record: ')
            break
        else:
            print('ID: {0} Name: {1} Lastname: {2} Email: {3} DOB: {4} Address: {5}'.format(
                row[0], row[1], row[2], row[3], row[4], row[5]))

def updateRow(con):

    cur = con.cursor()
    con.row_factory = sqlite3.Row
    cur.execute("SELECT * FROM Customers")
    rows = cur.fetchall()
    for row in rows:
        print('ID: {0} Name: {1} Lastname: {2} Email: {3} DOB: {4} Address: {5}'.format(row[0], row[1], row[2], row[3], row[4], row[5]))

    id = input("Enter ID for Update Record: ")
    Name = input("Enter Name for Update Record: ")
    clgName = input("Enter Lastname Name for Update Record: ")
    csr = input("Enter Email for Update Record: ")
    DOB = input("Enter DOB for Update Record: ")
    Address = input('Enter Address Name For Update record: ')
    cur.execute("UPDATE Customers SET Name = ?, Lastname = ?, Email = ?, DOB = ?, Address = ?  WHERE Id = ?",(Name, clgName, csr, DOB, Address, id))
    print("Number of rows updated:",  cur.rowcount)
    if cur.rowcount == 0:
        print('Record Not Updated')
        
def deleteRow(con):
  
    cur = con.cursor()
    con.row_factory = sqlite3.Row
    cur.execute("SELECT * FROM Customers")
    rows = cur.fetchall()
    for row in rows:
        print('Table Data:', row["Id"], row["Name"], row["Lastname"], row["Email"], row["DOB"], row["Address"])

    id = input("Enter ID for Delete Record: ")
    cur.execute("DELETE FROM Customers WHERE Id =  ?", (id,))
    print("Number of rows deleted:", cur.rowcount)

        



def choice_sqlite(con):
    print("1. Create Table")
    print("2. Insert Data")
    print("3. Read Data")
    print("4. Update Data")
    print("5. Delete Data")
    print("6. Quit")

    ch = int(input("Enter Your Choice: "))
    if ch == 1:
        createTable(con)
        choice_sqlite(con)
    elif ch == 2:
        insertTable(con)
        choice_sqlite(con)
    elif ch == 3:
        retrieveTable(con)
        choice_sqlite(con)
    elif ch == 4:
        updateRow(con)
        choice_sqlite(con)
    elif ch == 5:
        deleteRow(con)
        choice_sqlite(con)
    elif ch == 6:
        exit()
        pass
    else:
        print("Please Enter Valid Input")


def choice():
    con = creatdb()
    choice_sqlite(con)


choice()
