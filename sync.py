import mysql.connector
import psycopg2

def create_mysql_database(persons_data):

    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='lakshyam'
    )
    mysql_cursor = conn.cursor()


    mysql_cursor.execute('CREATE DATABASE IF NOT EXISTS db1')
    mysql_cursor.execute('USE db1')

    mysql_cursor.execute('DROP TABLE IF EXISTS persons')
    mysql_cursor.execute('''
        CREATE TABLE IF NOT EXISTS persons (
            id INT ,
            name VARCHAR(50),
            username VARCHAR(50),
            password VARCHAR(50),
            email VARCHAR(50)
        )
    ''')

    for person in persons_data:
        mysql_cursor.execute('INSERT INTO persons (id, name, username, password, email) VALUES (%s, %s, %s, %s, %s)',person)

    # cursor.executemany('''
    #         INSERT INTO persons (id, name, username, password, email)
    #         VALUES (%s, %s, %s, %s, %s)
    #     ''', persons_data)
    mysql_cursor.execute('SELECT * FROM persons')
    mysql_data = mysql_cursor.fetchall()
    print(mysql_data)

    conn.commit()
    mysql_cursor.close()
    conn.close()

persons_data = [
        (1, 'Faf', 'faf_dup', 'faf_sa', 'fafdup@gmail.com'),
        (2,'Virat','king_kohli','kingofcricket','kingkohli@gmail.com'),
        (3, 'Rajat', 'rajat', 'rajat_mp', 'rajatp@gmail.com'),
        (4, 'Maxwell', 'maxi', 'max_aus', 'maxig@gmail.com'),
        (5, 'Cameron', 'cam_green', 'cam_g', 'camgreen@gmail.com'),
        (6, 'Dinesh', 'dk', 'fatherofbangladesh', 'dk@gmail.com'),
        (7, 'Mahipal', 'mahipalL', 'mahi_har', 'mahipal@gmail.com'),
        (8, 'Dagar', 'm_dagar', 'm_dagar_', 'mayankd@gmail.com'),
        (9, 'Reece', 'reece', 'reece_t', 'reecetop@gmail.com')
    ]

create_mysql_database(persons_data)

def copy_to_postgres():

    mysql_connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='lakshyam',
        database='db1'
    )
    mysql_cursor = mysql_connection.cursor()


    postgres_connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='lakshyam',
        database='copy',
        port=5432
    )
    postgres_cursor = postgres_connection.cursor()


    postgres_cursor.execute('DROP TABLE IF EXISTS persons')
    postgres_cursor.execute('''
        CREATE TABLE IF NOT EXISTS persons (
            id INT,
            name VARCHAR(50),
            username VARCHAR(50),
            password VARCHAR(50),
            email VARCHAR(50)
        )
    ''')

    for person in persons_data:
        postgres_cursor.execute('''
            INSERT INTO persons (id, name, username, password, email)
            VALUES (%s, %s, %s, %s, %s)
        ''', person)

    postgres_cursor.execute('SELECT * FROM persons')
    postgres_data = postgres_cursor.fetchall()
    print(postgres_data)

    postgres_connection.commit()
    postgres_cursor.close()
    postgres_connection.close()

    mysql_cursor.close()
    mysql_connection.close()


copy_to_postgres()
