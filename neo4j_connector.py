# coding: utf-8
# Project：Mysql2Neo4j
# File：neo4j_connector.py
# Author：will
# Date ：2024/9/6 11:30
# IDE：PyCharm
from neo4j import GraphDatabase
from neo4j.exceptions import Neo4jError

class Neo4jConnector:
    def __init__(self, uri, user, password):
        self.uri = uri
        self.user = user
        self.password = password
        self.driver = None

    def connect(self):
        try:
            self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))
            print("Connected to Neo4j successfully.")
        except Neo4jError as e:
            print(f"Failed to connect to Neo4j: {e}")

    def disconnect(self):
        if self.driver:
            self.driver.close()
