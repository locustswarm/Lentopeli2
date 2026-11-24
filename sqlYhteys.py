import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='lentopeli_2',
    user='root',
    password='Rotting_dir?1984',
    autocommit=True
)