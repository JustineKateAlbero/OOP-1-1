import pyodbc

try:
    connection = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                 r'DBQ=C:\Users\Admin\Documents\Database1.accdb;'
    conn = pyodbc.connect(connection)

    cursor = conn.cursor()

    Table1 = (

        (10, 'Justine Kate P. Albero', 19, 'TMC Cavite','BSCPE',99)
    )

    cursor.execute('INSERT INTO Table1 VALUES (?,?,?,?,?,?)', Table1)
    conn.commit()
    print('Data Inserted')


except pyodbc.Error as e:
    print("Error in connection", e)
