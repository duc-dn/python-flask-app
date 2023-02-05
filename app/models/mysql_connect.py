import mysql.connector


class MySQL_connect:
    def __init__(self, host: str, user: str, password: str, database: str) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def mysql_connector(self):
        try:
            mydb = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except Exception as ex:
            print("Failed to connect to mysql")

        return mydb

    