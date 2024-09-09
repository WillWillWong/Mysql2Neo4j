# coding: utf-8
# Project：Mysql2Neo4j
# File：graph_importer.py
# Author：will
# Date ：2024/9/6 11:30
# IDE：PyCharm
from neo4j import GraphDatabase

class GraphImporter:
    def __init__(self, mysql_connector, neo4j_connector):
        self.mysql_connector = mysql_connector
        self.neo4j_connector = neo4j_connector

    def import_data(self):
        tables = self.mysql_connector.get_tables(self.mysql_connector.config['database'])
        if self.neo4j_connector.driver:
            with self.neo4j_connector.driver.session() as session:
                session.run("MATCH (n) DETACH DELETE n")

        with self.neo4j_connector.driver.session() as session:
            for (table_name, table_comment) in tables:
                session.run("CREATE (t:table {name: $table_name,table_comment: $table_comment})", table_name=table_name, table_comment=table_comment)

                columns = self.mysql_connector.get_columns(table_name)
                for column in columns:
                    col_name, col_type, _, _, _, _, _, _, col_comment = column
                    session.run("""
                        MATCH (t:table {name: $table_name})
                        CREATE (c:column {name: $col_name, dataType: $col_type, description: $col_comment})
                        CREATE (t)-[:has_column]->(c)
                    """, table_name=table_name, col_name=col_name, col_type=col_type, col_comment=col_comment)

                foreign_keys = self.mysql_connector.get_foreign_keys(table_name)
                for fk in foreign_keys:
                    fk_column, ref_table, ref_column = fk
                    session.run("""
                        MATCH (t1:table {name: $table_name}), (t2:table {name: $ref_table})
                        CREATE (t1)-[:foreign_key {from: $fk_column, to: $ref_column}]->(t2)
                    """, table_name=table_name, ref_table=ref_table, fk_column=fk_column, ref_column=ref_column)
