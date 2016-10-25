import psycopg2
import os


def doDB():
    DB = psycopg2.connect("dbname=tourney_practice")
    c = DB.cursor()
    query = "select pid, player_name from players1;"
    c.execute(query)
    rows = c.fetchall()
    for row in rows:
        print row
    DB.close()

# doDB()


def wtf():
    my_dir = os.getcwd()
    print my_dir
    # DB = psycopg2.connect("dbname=tourney_practice")
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    # query = "select * from players1;"
    query = "select * from players;"
    c.execute(query)
    rows = c.fetchall()
    for row in rows:
        print row

    DB.close()
    

# def show_all():
#     DB = psycopg2.connect("dbname=tourney_practice")
#     c = DB.cursor()
#     query = "select * from players1;"
#     c.execute(query)
#     rows = c.fetchall()
#     for row in rows:
#         print row

#     DB.close()
import psycopg2

psycopg2.extensions.cursor.fetchone
psycopg2.extensions.cursor.fetchall

DB = psycopg2.connect("dbname=tourney_practice")

c = DB.cursor()

c.execute("select * from players1;")

row = c.fetchall()

type(row)

row

print row

c.execute("select count(*) from players1;")

num = c.fetchall()

type(num)

DB.close()

