import pymysql.cursors
import hashlib
import uuid

def connection_db():
    connection = pymysql.connect(host='mrbartucz.com',
                                     user='av6352tk',
                                     password='Buddha414!',
                                     db='av6352tk_SaltHash',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
    return connection

        
def set_password():
    connection = connection_db()
    print("\nSet Username and Password:\n")
    try:
        with connection.cursor() as cursor:

            user_name = input("\nEnter a username: ")
            print("Username: " + user_name + "\n")

            password = input("Enter a password: ")
            salt = uuid.uuid4().hex
            print("Password: " + password)
            print("\n\nSalt: " + salt)
            print("Password with Salt: " + password + salt)
            pws = "" + password + salt
            #pwse = pws.encode
            final_hash = hashlib.sha256(pws.encode()).hexdigest()
            print("Hash: " + final_hash)
            sql_in = """INSERT INTO Hash (UserName, Salt, Hash) VALUES (%s,%s,%s)"""
            insert_tuple = (user_name, salt, final_hash)
            cursor.execute(sql_in, insert_tuple)
            connection.commit()

    finally:
        connection.close()

    return


def get_password():
    connection = connection_db()
    print("\nGet Username and Salt/Hash:\n")
    try:
        with connection.cursor() as cursor:
            # get password from database

            user_name = input("\n\nEnter a username:")
            print("Username: " + user_name)

            password2 = input("\nEnter a password:")
            print("Password Entered: " + password2)
            sql_out = "SELECT * FROM Hash WHERE UserName = %s"

            cursor.execute(sql_out, user_name)

            for result in cursor:
                username_r = result['UserName']
                salt_r = result['Salt']
                hash_r = result['Hash']

                print("\nSalt from DB: " + salt_r)

                pass2_salt_r = "" + password2 + salt_r
                print("Password+salt: " + pass2_salt_r)
                check_hash = hashlib.sha256(pass2_salt_r.encode()).hexdigest()

                print("Check Hash: " + check_hash)
                if (check_hash == hash_r):
                    print("\n*********************************")
                    print("Access Granted: Password Accepted")
                    print("*********************************")
                else:
                    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("Access Denied: Password Incorrect")
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("\n\nUsername from DB: " + str(username_r))
            print("Salt from DB: " + str(salt_r))
            print("Hash from DB: " + str(hash_r) + "\n")

    finally:
        connection.close()

    return


def main():
    set_password()
    get_password()
    return


if __name__ == '__main__':  # for not executing main() when imported
    main()
