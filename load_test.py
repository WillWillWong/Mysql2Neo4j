# coding: utf-8
# Project：Mysql2Neo4j
# File：test.py
# Author：will
# Date ：2024/8/16 15:24
# IDE：PyCharm
from main import MySQLConnector, Neo4jConnector, GraphImporter

mysql_config = {
    'user': 'root',
    'password': '123456',
    'host': '127.0.0.1',
    'database': 'graph_test'}

user = "root"
password = "123456"
host = "127.0.0.1"
database = "graph_test"
neo4j_uri = "bolt://127.0.0.1:7687"
neo4j_user = "neo4j"
neo4j_password = "123456789"

# 初始化连接器
mysql_connector = MySQLConnector(mysql_config)

neo4j_connector = Neo4jConnector(neo4j_uri, neo4j_user, neo4j_password)

# 连接数据库
mysql_connector.connect()
neo4j_connector.connect()

# 导入数据
graph_importer = GraphImporter(mysql_connector, neo4j_connector)
graph_importer.import_data()

# 断开数据库连接
mysql_connector.disconnect()
neo4j_connector.disconnect()
