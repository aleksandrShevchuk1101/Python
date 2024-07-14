

import sqlite3

DB_NAME = 'sqlite_db.db'


# # Read records
with sqlite3.connect(DB_NAME) as sql_conn:
    sql_request = "Select * from courses WHERE reviews_qty > 0"
    sql_records = sql_conn.execute(sql_request)
    # for record in sql_records:
    #     id, title, qty, rev = record
    #     print(id, title)
    courses = sql_records.fetchall()
    print(courses)




# Write multiple records

# courses = [
#     (500,'Python course', 100, 30),
#     (234,'Java course', 100, 20),
#     (567,'Node.ja course', 100, 70)
# ]

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?,?,?,?)"

#     for course in courses:
#         sqlite_conn.execute(sql_request, course)

#     sqlite_conn.commit()


# Insert one record to the table
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?,?,?,?)"
#     sqlite_conn.execute(sql_request, (251,'Python course', 100, 30))
#     sqlite_conn.commit()



# Create DB table
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = """ CREATE TABLE IF NOT EXISTS courses(
#         id integer PRIMARY KEY,
#         title text NOT NULL,
#         student_qty integer,
#         reviews_qty integer
#     ); """    
#     sqlite_conn.execute(sql_request)


# Create DB if is absent

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     print(sqlite_conn)
#     print(type(sqlite_conn))