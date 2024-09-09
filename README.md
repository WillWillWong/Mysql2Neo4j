
# 关系型数据库迁移图数据工具

## 介绍

这是一个用于从MySQL数据库导入数据到Neo4j图数据库的数据迁移工具。该工具通过连接MySQL和Neo4j数据库，并将MySQL中的表数据转换为Neo4j中的图数据。

## 技术栈

- Python
- MySQL
- Neo4j

## 安装

确保安装了以下依赖库：
- `mysql-connector-python`
- `neo4j`

可以通过以下命令安装所需的库：
```pip install mysql-connector-python neo4j```
## 配置

### MySQL数据库连接配置
python
mysql_config = { 'user': 'root',
                 'password': '123456',
                 'host': '127.0.0.1',
                 'database': 'graph_test'}

### Neo4j数据库连接配置
neo4j_uri = "bolt://127.0.0.1:7687"
neo4j_user = "neo4j"
neo4j_password = "123456789"
## 运行

1. 确保MySQL和Neo4j服务正在运行。
2. 修改`mysql_config`和`neo4j_uri`中的配置信息。
3. 运行主程序：
``` python main.py```

## 贡献指南

欢迎贡献！如果您发现任何问题或有改进建议，请提交Issue或Pull Request。

## 许可证

本项目采用MIT许可证。

---

**作者**: will


