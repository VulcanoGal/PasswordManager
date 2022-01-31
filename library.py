import mysql.connector
def createUser(a, b, c, d):
    if a and b and c and d is not None:
        PMDB = mysql.connector.connect(host = 'localhost', database= 'sys',  user=c, password=d, port=33060)
        PMcursor = PMDB.cursor()
        PMcursor.execute("CREATE USER '"a"'@'localhost' IDENTIFIED BY '"b"';")
        PMcursor.execute("GRANT ALL PRIVILEGES ON * . * TO '"a"'@'localhost';")
        PMDB.close()
        PMcursor.close()



