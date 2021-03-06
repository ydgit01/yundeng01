import pymysql
# 打开数据库连接
class Connect_mysql():
    def __init__(self,host='rm-uf6d67v5vx4f3v8btfo.mysql.rds.aliyuncs.com', user='yundeng',
                 passwd='Aliyun-gw', db='foura', port=3306, charset='utf8',
                 creator=pymysql, cursorclass=pymysql.cursors.DictCursor, maxconnect=5):
        self.user = user
        self.passwd = passwd
        self.db = db
        self.host = host
        self.port = port
        self.charset = charset
        self.creator = creator
        self.cursorclass = cursorclass
        self.maxconnect = maxconnect
        self.db = pymysql.connect(self.host, self.user, self.passwd, self.db, self.port, charset='utf8')

    def queryOne(self,spl):
        cursor = self.db.cursor()
        cursor.execute(spl)
        res = cursor.fetchone()
        cursor.close()
        self.db.close()
        return res


    def queryAll(self,spl):
        cursor = self.db.cursor()
        cursor.execute(spl)
        res = cursor.fetchall()
        cursor.close()
        self.db.close()
        return res

    def resultRow(self, n, sql):
        if n == 1:
            row = self.queryOne(sql)
            #         print "row=",row
            return row
        elif n == 2:
            rows = self.queryAll(sql)
            #         print "rows=",rows
            return rows
        elif n == 3:
            try:
                self.cursor = self.db.cursor()
                self.cursor.execute(sql)
                return self.cursor
            except BaseException as msg:
                print(msg)
            finally:
                self.cursor.close()
                self.db.close()




