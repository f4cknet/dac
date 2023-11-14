import pymysql

class ApiSql(object):

    def __enter__(self):
        self.conn = pymysql.connect(host="localhost",port=3306,user='dac',passwd='dac_qa_passw0rd',db='dac',charset='utf8mb4')
        self.cur = self.conn.cursor()
        return self

    def write_sql(self,sql,params):
        self.cur.execute(sql,params)
        self.conn.commit()
        return "insert success"

    def read_sql(self,sql,params):
        try:
            self.cur.execute(sql,params)
            return self.cur.fetchall()
        except Exception as e:
            return "query failed:" + str(e)

    def __exit__(self,exc_type,exc_val,exc_tb):
        self.cur.close()
        self.conn.close()

if __name__ == "__main__":
    date = "2023-11-07"
    sql = f"select repeat_traceid from result where date='{date}'"
    with ApiSql() as s:
        data = s.read_sql(sql)
    sql = f"select repeat_traceid from result where date='{date}'"
    with ApiSql() as s:
        s.read_sql(sql)

    print(data)
