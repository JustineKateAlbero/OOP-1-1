import pyodbc

try:
    connection = pyodbc.connect(
        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\Admin\Documents\Database1.accdb;')
    print('Database is Connected')

    user_id = 10
    Fullname = "Kate"
    Age = 19
    Course = "BSCPE"
    Address = "Cavite"
    Grades = 100

    database = connection.cursor()
    database.execute('UPDATE Table1 SET Fullname=?, Age=?, Course=?, Address=?, Grades=? WHERE id=?',
                     (Fullname, Age, Course, Address, Grades, user_id))
    connection.commit()

    print("Record is ADDED")


except pyodbc.Error:
    print('Database is NOT connected')
