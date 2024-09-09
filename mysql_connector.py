# coding: utf-8
# Project：Mysql2Neo4j
# File：mysql_connector.py
# Author：will
# Date ：2024/9/6 11:30
# IDE：PyCharm
import mysql.connector

class MySQLConnector:
    def __init__(self, config):
        self.config = config
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = mysql.connector.connect(**self.config)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def get_tables(self, database_name):
        query = "SELECT table_name, table_comment FROM information_schema.tables WHERE table_schema = %s;"
        self.cursor.execute(query, (database_name,))
        return self.cursor.fetchall()

    def get_columns(self, table_name):
        self.cursor.execute(f"SHOW FULL COLUMNS FROM {table_name}")
        return self.cursor.fetchall()

    def get_foreign_keys(self, table_name):
        self.cursor.execute(f"""
            SELECT column_name, referenced_table_name, referenced_column_name
            FROM information_schema.KEY_COLUMN_USAGE
            WHERE TABLE_NAME = '{table_name}' AND REFERENCED_TABLE_NAME IS NOT NULL
        """)
        return self.cursor.fetchall()
