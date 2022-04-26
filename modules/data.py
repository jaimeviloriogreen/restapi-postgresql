from helpers.database import connection
from modules.strings import stringWithComa

#? Return all data
def getAllData(values, table):
    try:
        fields = stringWithComa(values)
        cur = connection.cursor()
        cur.execute(f"SELECT {fields} FROM {table}")
        return cur.fetchall()
    except Exception as e:
        return f"Error: {e}"
    
    cur.close()
    connection.close()

#? Return One data    
def getOneData(values, table, name = None):
    if name:
        try:
            cur = connection.cursor()
            fields = stringWithComa(values)
            cur.execute(f"SELECT {fields} FROM {table} WHERE name = %s;", (name.title(),))
            return cur.fetchone()
        except Exception as e:
            return f"Error: {e}"
    cur.close()
    connection.close()

#? Delete data      
def deleteData(table, name = None):
    if name:
        try:
            cur = connection.cursor()
            cur.execute(f"DELETE FROM {table} WHERE name = %s;", (name.title(),))
            connection.commit()
            
            return cur.rowcount
        except Exception as e:
            return f"Error: {e}"
    
    cur.close()
    connection.close()

#? Insert data 
def insertData(table, name, price, qty):
    if name:
        try:
            cur = connection.cursor()
            cur.execute(f"INSERT INTO {table}(name, price, qty) VALUES(%s, %s, %s)", (name, price, qty))
            connection.commit()
            return cur.rowcount
        except Exception as e:
            return f"Error: {e}"
    
    cur.close()
    connection.close()
        
        
