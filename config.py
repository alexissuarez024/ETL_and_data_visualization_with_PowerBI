import os
from dotenv import load_dotenv

class Connection:
    def __init__(self, psycopg2):
        self.psycopg2 = psycopg2
        

    def connec(self):
        try:
            load_dotenv()
            
            config = { "host": os.getenv("HOST_AWS"),
                "database" : os.getenv("DATABASE_AWS"),
                "user" : os.getenv("USER_AWS"),
                "password" : os.getenv("PASSWORD_AWS")}
        
            connected = self.psycopg2.connect(**config)
            return connected

        except Exception as e:
            return print(e)


    def curExecute(self,sql):
        con = self.connec()
        cursorClass = con.cursor()
        response = cursorClass.execute(sql)
        con.commit()
        cursorClass.close()
        con.close()
        return response

    
    def curFetchOne(self,sql):
        con = self.connec()
        cursorClass = con.cursor()
        cursorClass.execute(sql)
        response = cursorClass.fetchone()
        con.commit()
        cursorClass.close()
        con.close()
        return response


    def curFetchAll(self,sql):
        con = self.connec()
        cursorClass = con.cursor()
        cursorClass.execute(sql)
        response = cursorClass.fetchall()
        con.commit()
        cursorClass.close()
        con.close()
        return response
