import pyodbc, time
cnxn = pyodbc.connect('Driver = {SQL Server};DSN=SQL-2024-AdventureWorks;DATABASE=TSQL;UID=sa;PWD=SQLPa55w.rdSQL')
 
cursor = cnxn.cursor()
cursor.execute('SELECT * FROM Sales.Orders')
 
for row in cursor:
    #print('row = %r' % (row,))
    print((row,))
    time.sleep(2)