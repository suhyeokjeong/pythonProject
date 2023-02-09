import cx_Oracle

con = cx_Oracle.connect("madang", "madang", "127.0.0.1:1521", encoding="UTF-8")
cursor = con.cursor()
cursor.execute("select * from customer")
# out_data = cursor.fetchone()
out_data = cursor.fetchall()

for data in out_data:
    print(data)


# print(out_data)
con.close()