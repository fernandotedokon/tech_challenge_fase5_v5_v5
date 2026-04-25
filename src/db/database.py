import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        host="postgresDb",
        database="fraud_db",
        user="fraud",
        password="fraud"
    )
