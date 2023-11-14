from broken_access_control.sql.basesql import ApiSql
import datetime

def insert_repeat_post(appname,path,method,params,hash,date,first_time,update_time,repeat_traceid,old_resp,new_resp):
    sql = f"insert into result(`appname`,`path`,`method`,`params`,`hash`,`date`,`first_time`,`update_time`,`repeat_traceid`,`old_resp`,`new_resp`) \
    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    with ApiSql() as s:
        s.write_sql(sql,(appname,path,method,params,hash,date,first_time,update_time,repeat_traceid,old_resp,new_resp))

def select_repeat_ByDate(date,appname):
    sql = f'select repeat_traceid,hash from result where date=%s and appname=%s'
    with ApiSql() as s:
        result = s.read_sql(sql,(date,appname))
    return result

def update_dac_result(traceid,vulnable,result_detail,hash,date):
    update_query = f"UPDATE result SET result = %s ,result_detail=%s WHERE repeat_traceid = %s and hash = %s and date = %s"
    with ApiSql() as s:
        result = s.write_sql(update_query,(vulnable,result_detail,traceid,hash,date))
    return result

def select_oldrespAndnewresp_ByTraceId(hash):
    sql = f"select old_resp,new_resp from result where hash= %s and update_time>'2023-11-13 11:26:00'"
    with ApiSql() as s:
        result = s.read_sql(sql,hash)
    return result


if __name__ == "__main__":
    # today = datetime.date.today()
    print(select_repeat_ByDate("2023-11-13"))