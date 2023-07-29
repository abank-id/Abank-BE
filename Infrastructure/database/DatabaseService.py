import mysql.connector


class Database:
    def __init__(self, user, password, host, port, database, ssl_ca, ssl_disabled):
        self._db = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database,
            ssl_ca=ssl_ca,
            ssl_disabled=ssl_disabled,
        )

    @property
    def db(self):
        return self._db

    def execute(self, sql, val=None):
        mycursor = self._db.cursor()
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        self._db.commit()
        return result


# user="admin7br",
# password="7br-db-password",
# host="7br-db.mysql.database.azure.com",
# port=3306,
# database="db7br",
# ssl_ca="DigiCertGlobalRootCA.crt.pem",
# ssl_disabled=False
