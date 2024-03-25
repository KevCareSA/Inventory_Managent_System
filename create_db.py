import sqlite3
import os

def create_db():
    conn = sqlite3.connect(database=r'inventory.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS employee (eid INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text, gender text, contact text, dob text, doj text, pass text, address text, salary)")
    conn.commit()
    
    cursor.execute("CREATE TABLE IF NOT EXISTS supplier (invoice INTEGER PRIMARY KEY AUTOINCREMENT, name text, contact text, desc text)")
    conn.commit()
    
    cursor.execute("CREATE TABLE IF NOT EXISTS category (cid INTEGER PRIMARY KEY AUTOINCREMENT, name text)")
    conn.commit()
    
    cursor.execute("CREATE TABLE IF NOT EXISTS products (pid INTEGER PRIMARY KEY AUTOINCREMENT, Supplier text, Category text, name text, price text, qty text, status text)")
    conn.commit()

create_db()
