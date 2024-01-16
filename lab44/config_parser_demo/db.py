import mysql.connector
from config_pareser import read_db_config

class DB:
    def __init__(self, user, password, db, host="localhost", port=3306):
        try:
            self.cnx = mysql.connector.connect(
                user=user,
                password=password,
                db=db,
                host=host,
                port=port
            )

        except mysql.connector.Error as e:
            print(e)
            exit()

        print('*** Connection Established ***')

if __name__=='__main__':
    db_config = read_db_config('./config.ini')
    print(db_config)
    db = DB( db_config['user'], db_config['password'], 'pyqtDemos')
