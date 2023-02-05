import json

from flask import Flask
import mysql.connector
from app.models.mysql_connect import MySQL_connect


app = Flask(__name__)

mydb = MySQL_connect(
    host="mysql", 
    user="root", 
    password="123456", 
    database="ProductManagement"
).mysql_connector()

@app.route("/")
def root():
    return json.dumps({"Hello": "Welcome to my API :>"})

@app.route("/products")
def get_products():
    conn = mydb.cursor()
    conn.execute("select * from tblProduct")
    row_headers = [x[0] for x in conn.description]
    products = conn.fetchall()
    json_data = []
    for product in products:
        json_data.append(dict(zip(row_headers, product)))
    conn.close()
    return json.dumps(json_data)

@app.route("/product/<id>")
def get_product_by_id(id):
    conn = mydb.cursor()
    conn.execute("select * from tblProduct where pro_id = {}".format(id))
    product = conn.fetchone()
    conn.close()
    return json.dumps({"product": product})


