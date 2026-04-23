import mysql.connector


# it it use to create db connection
def connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Actowiz",
        database="mydb"
    )

    cur = conn.cursor()

    return conn,cur 

# it create databse table 
def create_db():
    conn,cur = connection()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS cars(
                c_id INT AUTO_INCREMENT PRIMARY KEY,
                car_type VARCHAR(255),
                car_name VARCHAR(255),
                subtitle VARCHAR(255),
                capacity VARCHAR(255),
                delers JSON,
                fule VARCHAR(255),
                color VARCHAR(255),
                images JSON,
                price INT,
                price_unit VARCHAR(255),
                vehicle_data JSON,
                equipment JSON,
                finance JSON
            )

    """)

    conn.commit()
    conn.close()


# it insert 100 rows at the time
def insert_data(data):
    query = """INSERT INTO kia(car_type,car_name,subtitle,capacity,delers,fule,color,images,price,price_unit,vehicle_data,equipment,finance) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    conn,cur = connection()

    cur.executemany(query,data)
    print(f'100 row was add!')
    conn.commit()
    conn.close()

