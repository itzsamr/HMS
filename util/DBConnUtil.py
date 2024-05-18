import pyodbc


class DBConnUtil:
    @staticmethod
    def get_connection():
        try:
            connection = pyodbc.connect(
                "Driver={SQL Server};"
                "Server=SAMAR\MSSQLSERVER01;"
                "Database=hospital;"
                "Trusted_Connection=yes;"
            )
            return connection
        except Exception as e:
            print("Error connecting to database:", e)
            return None
