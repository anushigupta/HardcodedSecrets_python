import psycopg2
 

conn_string = "host='123.12.31.2' dbname='mydb' user='admin' password='12345'"
 
# use connect function to establish the connection
conn = psycopg2.connect(conn_string)
