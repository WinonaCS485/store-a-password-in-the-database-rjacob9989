import pymysql.cursors
import hashlib, uuid

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
        salt = uuid.uuid4().hex
        print("Password: " + password)
        print(salt)

        print("Password with Salt:" + password + salt)
        pws = "" + password + salt 
        #pwse = pws.encode
        final_hash = hashlib.sha256(pws.encode()).hexdigest()
        print("Hash and Salt: " + final_hash)

        sql_in = """INSERT INTO Hash (UserName, Salt, Hash) VALUES (%s,%s,%s)"""
        insert_tuple = (user_name, salt, final_hash)
        cursor.execute(sql_in, insert_tuple)
       
        #cursor.execute(sql)

        # get the results
        #for result in cursor:
        #    print (result)
        
      
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        connection.commit()

        #get password from database

        user_name = input("Enter a username\n" )
        print("Username: " + user_name)

        password2 = input("Enter a password:\n" )

        sql_out = "SELECT * FROM Hash WHERE UserName = %s"
              
        cursor.execute(sql_out, user_name)

        for result in cursor:
             username_r = result['UserName']
             salt_r = result['Salt']
             hash_r = result['Hash']
             print("Password Entered: " + password2)
             print("Salt from DB: " + salt_r)
             

             pass2_salt_r = "" + password2 + salt_r
             print("Password+salt: " + pass2_salt_r)
             check_hash = hashlib.sha256(pass2_salt_r.encode()).hexdigest()

             print("Check Hash: " + check_hash )
             if (check_hash == hash_r):
                 print("\nAccess Granted: Password Accepted\n")
        print ("Username DB: " + str(username_r))
        print("Salt DB: " + str(salt_r))
        print("Hash_DB: " + str(hash_r))








        

finally:
    connection.close()
