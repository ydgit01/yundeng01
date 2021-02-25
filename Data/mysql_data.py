import Connect_mysql

class Mysql_data:
    def __init__(self):
        self.connect = Connect_mysql(host='rm-uf6d67v5vx4f3v8btfo.mysql.rds.aliyuncs.com', user='yundeng',
                 passwd='Aliyun-gw', db='foura', port=3306, charset='utf8')

    #查询租户有多少个组织
    def org_numall(self,tenant_id):
        sql = 'SELECT count(*) FROM `org_organization` WHERE `tenant_id`={tenant_id};'.format(tenant_id=tenant_id)
        num = self.connect.queryOne(sql)
        return num[0]

        # 查询租户有多少个人员
    def person_num(self,tenant_id):
        sql = 'SELECT count(*) FROM `cap_user`WHERE `tenant_id`={tenant_id};'.format(tenant_id=tenant_id)
        num = self.connect.queryOne(sql)[0]
        return num

    def log_name(self):
        sql = "SELECT `realname`FROM `org_employee` WHERE `userid`='yuedantestadmin'"
        name = self.connect.queryOne(sql)[0]
        return name

   #查询组织列表对应组织的人员数量
    def org_num(self,tenant_id,orgname):
        spl = "SELECT COUNT(*) FROM `org_emporg`WHERE `tenant_id`={tenant_id} AND `orgid`=(SELECT orgid FROM " \
               "`org_organization` WHERE `tenant_id`={tenant_id} AND orgname = '{orgname}')".format(tenant_id=tenant_id,orgname=orgname)
        num = self.connect.queryOne(spl)[0]
        return num

    # 查询所有组织的组织名称
    def org_name(self,tenant_id):
        spl = "SELECT `orgname` FROM `org_organization` WHERE `tenant_id`={tenant_id}".format(tenant_id=tenant_id)
        orgname = self.connect.queryAll(spl)
        return orgname

    # 查询所有单位的组织名称
    def com_name(self,tenant_id):
        spl = "SELECT `name` FROM `company` WHERE `tenant_id`={tenant_id} AND `is_deleted`=0".format(tenant_id=tenant_id)
        comname = self.connect.queryAll(spl)
        return comname

    # 查询不同状态的人员数量
    def emp_num(self,tenant_id,status):
        spl = "SELECT COUNT(*) FROM `cap_user`WHERE `tenant_id`={tenant_id} AND`status`={status}".format(tenant_id=tenant_id,status=status)
        empnum = self.connect.queryOne(spl)
        return empnum

    #查询不同状态人员的姓名
    def emp_name(self,tenant_id,status): #0代表停用  ，1代表启用  2，代表冻结
        spl = "SELECT `user_name` FROM `cap_user`WHERE `tenant_id`={tenant_id} AND`status`={status}".format(tenant_id=tenant_id,status=status)
        empname = self.connect.queryAll(spl)
        return empname
    #用户登录的次数
    def emp_loginlog_num(self, tenant_id, user_name):
        spl = "SELECT COUNT(*) FROM `login_log`WHERE `login_account_id`=(SELECT `operator_id`FROM `cap_user`WHERE" \
              " `tenant_id`={tenant_id} AND `user_name`= '{user_name}')".format(
            tenant_id=tenant_id, user_name=user_name)
        lognum = self.connect.queryOne(spl)[0]
        return lognum
    #功能角色的数量
    def functional_role_num(self,tenant_id):
        spl = "SELECT COUNT(*) FROM `role`WHERE `tenant_id`={tenant_id} AND `type`='FUNCTION'".format(
            tenant_id=tenant_id)
        rolenum = self.connect.queryOne(spl)[0]
        return rolenum
    #功能角色的所有名称
    def functional_role_name(self,tenant_id): #0代表停用  ，1代表启用  2，代表冻结
        spl = "SELECT `name` FROM `role`WHERE `tenant_id`={tenant_id} AND `type`='FUNCTION'".format(tenant_id=tenant_id)
        rolename = self.connect.queryAll(spl)
        return rolename
    #数据（系统）角色的人员数量
    def datas_role_num(self,tenant_id,data_name,role_name):
        spl = "SELECT COUNT(*) FROM `user_role` WHERE role_data_id=(SELECT id FROM `role_data` WHERE tenant_id={tenant_id} AND is_deleted=0 " \
              "AND data_id=(SELECT id FROM `system` WHERE `tenant_id`={tenant_id} AND `name`='{data_name}')" \
              " AND `role_id`=(SELECT id FROM `role`WHERE `tenant_id`={tenant_id} AND `name`='{role_name}'))"\
            .format(tenant_id=tenant_id,data_name=data_name,role_name=role_name)
        datarolenum = self.connect.queryOne(spl)[0]
        return datarolenum
    ##数据（微服务）角色的人员数量
    def datam_role_num(self,tenant_id,key,role_name):
        spl = "SELECT COUNT(*) FROM `user_role` WHERE role_data_id=(SELECT id FROM " \
              "`role_data`WHERE tenant_id=42 AND is_deleted=0 AND " \
              "data_id=(SELECT id FROM `microservice` WHERE `tenant_id`={tenant_id} AND `key`='{key}') " \
              "AND `role_id`=(SELECT id FROM `role`WHERE `tenant_id`={tenant_id} AND `name`='{role_name}'))"\
            .format(tenant_id=tenant_id,role_name=role_name,key=key)
        datarolenum = self.connect.queryOne(spl)[0]
        return datarolenum
    def functional_role_per_num(self,tenant_id,name):
        spl = "SELECT COUNT(*) FROM `user_role` WHERE `tenant_id`={tenant_id} AND `is_deleted`=0 " \
              "AND`role_id`=(SELECT id FROM `role`WHERE `tenant_id`={tenant_id} AND `is_deleted`=0 AND `name`='{name}')"\
            .format(tenant_id=tenant_id,name=name)
        pernum = self.connect.queryOne(spl)[0]
        return pernum

        # 查询不同状态的人员数量
    def sys_num(self, tenant_id):
        spl =  "SELECT count(*) FROM `system` WHERE `tenant_id`={tenant_id} AND `is_deleted`=0".format(
            tenant_id=tenant_id)
        sysnum = self.connect.queryOne(spl)[0]
        return sysnum

        # 查询所有人员的姓名
    def sys_name(self, tenant_id):  # 0代表停用  ，1代表启用  2，代表冻结
        spl = "SELECT `name` FROM `system` WHERE `tenant_id`={tenant_id} AND `is_deleted`=0".format(
            tenant_id=tenant_id)
        sysname = self.connect.queryAll(spl)
        return sysname

    def sys_per_num(self, tenant_id,sysname):
        spl =  "SELECT count(*) FROM `user_role` WHERE `role_data_id` IN (SELECT id FROM `role_data` WHERE `tenant_id`={tenant_id} " \
               "AND data_id = (SELECT id FROM `system` WHERE `tenant_id`={tenant_id} AND `name`='{sysname}')) AND `is_deleted`=0"\
            .format(tenant_id=tenant_id,sysname=sysname)
        pernum = self.connect.queryOne(spl)
        return pernum

    def post_num(self,tenant_id,post):
        spl = "SELECT count(*) FROM `dictionary` WHERE `is_deleted`=0 AND `tenant_id`={tenant_id} AND`type_id`=" \
              "(SELECT id FROM `dictionary_type`WHERE `is_deleted`=0 AND `tenant_id`={tenant_id} AND `name`='岗位')"\
            .format(tenant_id=tenant_id,post=post)
        postnum = self.connect.queryOne(spl)[0]
        return postnum

    def post_name(self,tenant_id,post):
        spl = "SELECT name FROM `dictionary` WHERE `is_deleted`=0 AND `tenant_id`={tenant_id} AND`type_id`=" \
              "(SELECT id FROM `dictionary_type`WHERE `is_deleted`=0 AND `tenant_id`={tenant_id} AND `name`='{post}')"\
            .format(tenant_id=tenant_id,post=post)
        postnum = self.connect.queryAll(spl)
        return postnum


if __name__ == '__main__':
    # print(Mysql_data().org_numall(42))
    # print(Mysql_data().person_num(42))
    # print(Mysql_data().org_num(42,"第一个组织"))
    # print(Mysql_data().org_name(42))
    # print(Mysql_data().com_name(42))
    # print(Mysql_data().emp_name(42,1))
    # print(Mysql_data().emp_num(42,1))
    print(Mysql_data().emp_loginlog_num(42, "第一个人员"))
    print(Mysql_data().log_name())
    # print(Mysql_data().functional_role_name(42))
    # print(Mysql_data().functional_role_num(42))
    # print(Mysql_data().datas_role_num(42,'系统04','管理员'))
    # print(Mysql_data().datam_role_num(42, 'emss_cmnfw','管理员'))
    # print(Mysql_data().functional_role_per_num(42, '普通用户'))
    # print(Mysql_data().sys_num(42))
    # print(Mysql_data().sys_name(42))
    # print(Mysql_data().sys_per_num(42,'系统04'))
    # print(Mysql_data().post_num(42,'岗位'))
    # print(Mysql_data().post_name(42, '岗位'))





