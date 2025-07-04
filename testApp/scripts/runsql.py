from django.db import connection

def run():
    file_path = "/Users/adityaanand/Desktop/Desktop/orm_drf/testApp/scripts/test.sql"
    with open(file_path, "r") as file:
        sql = file.read()

    with connection.cursor() as cursor:
        cursor.execute(sql)
        if sql.strip().lower().startswith("select"):
            rows = cursor.fetchall()
            for row in rows:
                print(row)

    print("✅ SQL executed successfully.")