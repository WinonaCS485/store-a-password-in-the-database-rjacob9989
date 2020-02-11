import pymysql.cursors
import hashlib
import base64
import uuid

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='av6352tk',
                             password='Buddha414!',
                             db='av6352tk_SaltHash',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


try:
    with connection.cursor() as cursor:
        
        user_name = input("Enter a username\n" )
        print("Username: " + user_name)

        password = input("Enter a password:\n" )
        salt = base64.urlsafe_b64encode(uuid.uuid4().bytes)
        print("Password: " + password)
        print("Salt: " + str(salt))

        pass_salt =''
        pass_salt += password
        pass_salt += str(salt)
        final_hash = hashlib.sha256(pass_salt.encode()).hexdigest()
        print("Hash and Salt: " + final_hash)


        
        #sql = "SELECT * from Students WHERE Name LIKE %s"
       
        #cursor.execute(sql)

        # get the results
        #for result in cursor:
        #    print (result)
        
      
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        # connection.commit()
        

finally:
    connection.close()
