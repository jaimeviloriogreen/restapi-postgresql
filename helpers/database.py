import psycopg2
from settings.set import dataConnection

connection = psycopg2.connect(
    dbname=dataConnection['dbname'],
    user=dataConnection['user'],
    port=dataConnection['port'],
    password=dataConnection['password'],
    host=dataConnection['host']
)
