import pyodbc
DBfile = r"C:\Users\asus\Desktop\角磨机维修文件\物资管理数据库.accdb"  # 数据库文件
import pyodbc
import pandas as pd


 
# Connection function to use for access
def Connection():
    MDB = r'C:\Users\asus\Desktop\角磨机维修文件\物资管理数据库.accdb'
    DRV = '{Microsoft Access Driver(*.mdb,*.accdb)}'
    return pyodbc.connect('DRIVER={};DBQ={}'.format(DRV,MDB))
 
 
def get_milk_data():
    conn = Connection()
    cursor = conn.cursor()
    sqlstring = 'select * from milk'
    milk = list(cursor.execute(sqlstring))
    id, milk, date, farm = zip(*milk)
    milk = pd.DataFrame([id, milk, date, farm]).transpose()
    milk.to_hdf('milk.hdf', key='milk_all')
db=Connection()
print(db)
