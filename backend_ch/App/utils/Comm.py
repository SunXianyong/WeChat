import sys

from App.utils import Mysql, Neo4j


'''
sysconfig = {
        'db_host': '172.16.0.121',
        'db_port': 3306,
        'db_user': 'root',
        'db_passwd': 'aithu@2018',
        'db_db': 'spider',
        'db_charset': 'utf8mb4',
        'neo_host': '172.16.0.121',
        'neo_user': 'neo4j',
        'neo_passwd': 'aithu@2018',
        }
'''
sysconfig = {
    'db_host': '47.74.134.51',
    'db_port': 3306,
    'db_user': 'root',
    'db_passwd': 'aithu@2018',
    'db_db': 'spider',
    'db_charset': 'utf8mb4',
    'neo_host': '47.74.134.51',
    'neo_user': 'neo4j',
    'neo_passwd': '123456',
}

def connect_neo():
    return Neo4j.Neo({
        'host': sysconfig['neo_host'],
        'user': sysconfig['neo_user'],
        'passwd': sysconfig['neo_passwd']
        })

def connect_mysql():
    try:
        db_light = Mysql.Spider({
        'host': sysconfig['db_host'],
        'port': int(sysconfig['db_port']),
        'user': sysconfig['db_user'],
        'passwd': sysconfig['db_passwd'],
        'db': sysconfig['db_db'],
        'charset':sysconfig['db_charset'],
        })
    except Exception as error:
        print(error)
        sys.exit(0)
    return db_light

