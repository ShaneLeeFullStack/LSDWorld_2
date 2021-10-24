import pyodbc

server = 'lsdworld-server.database.windows.net'
database = 'lsdworld_database'
username = 'azureuser'
password = '{gHostbat9&}'
driver = '{ODBC Driver 17 for SQL Server}'



# with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
#    with conn.cursor() as cursor:
#        cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
#        #cursor.execute("SELECT * FROM SalesLT.Address")
#
#        row = cursor.fetchone()
#        while row:
#            print (str(row[0]) + " " + str(row[1]))
#            row = cursor.fetchone()


#        cursor.execute("DROP TABLE TEXT_ANALYSIS")
#        cursor.execute("DROP TABLE SUBSTANCE_TABLE")
#        cursor.execute("DROP TABLE TRIP_REPORTS")
#        cursor.execute("DROP TABLE USER_PROFILE")
#        cursor.execute("CREATE TABLE USER_PROFILE ("
#                       "user_id INTEGER PRIMARY KEY,"
#                       "name VARCHAR(40),"
#                       "gender_identity varchar,"
#                       "phone_number varchar,"
#                       "email varchar ,"
#                       "city varchar ,"
#                       "tripsitter INTEGER ,"
#                       "safety_contact_name varchar ,"
#                       "safety_contact_phone_number varchar )")
#        cursor.execute("CREATE TABLE TRIP_REPORTS ("
#                       "trip_report_id INTEGER PRIMARY KEY NOT NULL,"
#                       "date VARCHAR(255),"
#                       "user_id INTEGER,"
#                       "title varchar(255),"
#                       "substance_id int NOT NULL,"
#                       "report_content varchar(255),"
#                       "is_showing INTEGER)")
                       #"FOREIGN KEY (is_showing) REFERENCES TRIP_REPORTS(trip_report_id)"
                       #"FOREIGN KEY (user_id) REFERENCES USER_PROFILE(user_id))")

#        cursor.execute("CREATE TABLE SUBSTANCE_TABLE ("
#                       "substance_id int primary key,"
#                       "substance_name varchar(255),"
#                       "category varchar(255))")

#        cursor.execute("CREATE TABLE TEXT_ANALYSIS ("
#                       "text_trip_report_id int PRIMARY KEY,"
#                       "user_profile_id int,"
#                       "tags varchar(255) ) ")
#                      # "FOREIGN KEY (trip_report_id) REFERENCES TRIP_REPORTS(trip_report_id),")
#                      # "FOREIGN KEY (user_profile_id) REFERENCES USER_PROFILE(user_id))")

 #       cursor.execute("INSERT INTO TRIP_REPORTS ("
 #                 "trip_report_id,"
 #                  "user_id,"
 #                  "title,"
 #                  "substance_id,"
 #                  "report_content)"
 #                  "VALUES(9,9, 'my first trip report', 0, 'sample report content' )")
 #       cursor.close()
 #       conn.close()