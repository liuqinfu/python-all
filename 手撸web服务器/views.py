
from jinja2 import Template

def index():
    return 'index'


def admin():
    return 'admin'

import pymysql
def jinja2():
    connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='test', charset='utf8',
                              autocommit=True)
    cursor = connect.cursor(pymysql.cursors.DictCursor)
    sql = 'select * from user'
    rows = cursor.execute(sql)
    dicts = cursor.fetchall()

    with open('templates/html.html','r',encoding='utf-8') as f:
        html = f.read()
    template = Template(html)
    render = template.render(data=dicts)
    return render
