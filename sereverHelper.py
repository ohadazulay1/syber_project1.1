
class ServerHelper:
    def signUp(self, newData, DB_cursor, DB_connection, STARTING_SCORE):
            splited_data = newData.split(",")
            username = splited_data[0]
            password = splited_data[1]

            DB_cursor.execute("SELECT * FROM users WHERE username=?", (username,))

            rows = DB_cursor.fetchall()
            if not rows:
                DB_cursor.execute("INSERT INTO users VALUES(?,?,?);", (username,password,STARTING_SCORE))
                DB_connection.commit()
                return True
            else:
                return False


    def login(self, newData, DB_cursor, DB_connection,):
        splited_data = newData.split(",")
        username = splited_data[0]
        password = splited_data[1]
        DB_cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        rows = DB_cursor.fetchall()
        if not rows:
            return False
        DB_cursor.execute("SELECT * FROM users WHERE password=?", (password,))

        rows = DB_cursor.fetchall()
        if not rows:
            return False
        return True