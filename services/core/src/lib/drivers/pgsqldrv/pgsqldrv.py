import psycopg2


def create_conn(host, port, db_name, user, password):
    return psycopg2.connect(
        host=host,
        port=port,
        dbname=db_name,
        user=user,
        password=password)
