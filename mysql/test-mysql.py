import pymysql;
con = pymysql.connect(host="127.0.0.1",port=3306,user='root',password='root',db='wjd',charset='utf8');
cursor = con.cursor(pymysql.cursors.DictCursor);
sql = 'select * from t_mobile_base_info';
cursor.execute(sql);
all_mobile_dict = cursor.fetchall()
print(all_mobile_dict)