from pymongo import MongoClient
import psycopg2


def get_postgre():
    # Parâmetros de conexão com o banco de dados
    DATABASE_USER = "root"
    DATABASE_PASS = "toor"
    DATABASE_HOST = "localhost"
    DATABASE_PORT = "5432"
    DATABASE_NAME = "ifest"

    # Construção da conexão com o banco de dados
    return psycopg2.connect(
        host=DATABASE_HOST,
        port=DATABASE_PORT,
        user=DATABASE_USER,
        password=DATABASE_PASS,
        database=DATABASE_NAME
    )


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    # CONNECTION_STRING = "mongodb://localhost:27017/"
    CONNECTION_STRING = "mongodb+srv://admin:isaAlexiaGui23@ifestdb.rgbvgml.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['iFestDB']


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Get the database
    dbname = get_database()
