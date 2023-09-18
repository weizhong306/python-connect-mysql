import mysql.connector
# 連線到資料庫
con = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="mydb"
)
print("資料庫連線成功")
# 建立 Cursor 物件，用來對資料庫下SQL指令
cursor = con.cursor()
# 更新資料
# cursor.execute("UPDATE product SET name='美式咖啡' WHERE id = 1")
# productName = "美式"
# productId = 1
# cursor.execute("UPDATE product SET name=%s WHERE id = %s",
#                (productName, productId))
# con.commit()

# 取得一筆資料
cursor.execute("SELECT * FROM product WHERE id = 2")
data = cursor.fetchone()
print(data)
print(data[0], data[1])

# 取得多筆資料
cursor.execute("SELECT * FROM product")
data = cursor.fetchall()
print(data)

# 逐一取得
for row in data:
    print(row[0], row[1])

# 關閉連線
con.close()
