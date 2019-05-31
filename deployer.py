import json
from dataStructures import *
import psycopg2
import config
import functions

#for testing purposes
__testing__ = 2

sql_create_table = """CREATE TABLE cloudops.pingdom_checks(
    next_step_id SERIAL PRIMARY KEY,
    service VARCHAR(255),
    datacenter VARCHAR(100),
    alarmgroup VARCHAR(255),
    name VARCHAR(255),
    show_starting_relevant_to_start_time VARCHAR(255),
    show_starting_relevant_to_escalation_start_time VARCHAR(255),
    critical_at_relevant_to_start_time VARCHAR(255),
    critical_at_relevant_to_escalation_start_time VARCHAR(255),
    description VARCHAR(255),
    url VARCHAR(255),
    action_url VARCHAR(255),
    show_starting_relevant_to_last_update VARCHAR(255),
    status VARCHAR(255),
    critical_at_relevant_to_last_update VARCHAR(255)
);"""

sql_list_columns = """SELECT column_name
FROM information_schema.columns
WHERE table_schema = 'cloudops'
  AND table_name   = 'pingdom_checks';"""


#connection to postgresql server and making changes
try:
    connection = psycopg2.connect(user = config.USERNAME,
                                  password = config.PASSWORD,
                                  host = config.HOST,
                                  port = "5432",
                                  database = config.DBNAME)
    cursor = connection.cursor()
    if(connection):
        print("connection estabilished")
        # query here comes
        cursor.execute("""SELECT table_name FROM information_schema.tables
        WHERE table_schema = 'cloudops';""")
        tables = cursor.fetchall()
        if(__testing__ == 1):
            print(tables,"\n......................")
    

        if(functions.does_pingdom_checks_exists(tables)):
            print("pingdom_checks table exists.")
        else:
            print("pingdom checks table is missing...")
            try:
                cursor.execute(sql_create_table)
            except:
                print("Can NOT create new table")

            connection.commit() # <--- makes sure the change is shown in the database
        
        #data injection into pingdom_checks table
        with open('sample.json') as json_file:  
            input_data = json.load(json_file)
            if (__testing__ == 1):
                print(input_data)
            sql_insert_data = "INSERT INTO cloudops.pingdom_checks VALUES "
            for record in input_data["data"]:
                sql_insert_data += "("
                for item in record:
                    if(isinstance(item, str)):
                        sql_insert_data += "\'" + item + "\', "
                    else:
                        sql_insert_data += str(item) + ", "
                sql_insert_data = sql_insert_data[:-2] #delete last coma and space
                sql_insert_data += "), "
            sql_insert_data = sql_insert_data[:-2] #delete last coma and space
            sql_insert_data += ";"
            sql_insert_data = sql_insert_data.replace("None", "null")
            if(__testing__ == 2):
                print(sql_insert_data)
            try:
                cursor.execute(sql_insert_data)
            except(Exception, psycopg2.Error) as error:
                print("data injection error: ", error)
            else:
                connection.commit()
                print("data injection successful")
            




    
except (Exception, psycopg2.Error) as error :
    print ("PostgreSQL error happened...", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")




