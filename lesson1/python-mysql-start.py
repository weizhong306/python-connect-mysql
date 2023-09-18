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
# 將變數資料帶入到SQL指令裡面
productId = 6
productName = "奶綠"
cursor = con.cursor()
cursor.execute("INSERT INTO product(id, name) VALUES(%s, %s)",
               (productId, productName))
con.commit()  # 確定執行
# 關閉資料庫連線
con.close()
