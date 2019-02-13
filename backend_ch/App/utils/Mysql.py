# -*- coding: utf-8 -*-
import pymysql
import time
import re


class LightMysql:
    _dbconfig = None
    _cursor = None
    _connect = None
    _error_code = ''  # error_code from pymysql
                 
    TIMEOUT_DEADLINE = 30  # quit connect if beyond 30S
    TIMEOUT_THREAD = 10  # threadhold of one connect
    TIMEOUT_TOTAL = 0  # total time the connects have waste

    def __init__(self, dbconfig):
        try:
            self._dbconfig = dbconfig
            self.get_dbconfig(dbconfig)
            self._connect = pymysql.connect(
                host=self._dbconfig['host'],
                port=self._dbconfig['port'],
                user=self._dbconfig['user'],
                passwd=self._dbconfig['passwd'],
                db=self._dbconfig['db'],
                use_unicode=True,
                cursorclass=pymysql.cursors.DictCursor,
                charset=self._dbconfig['charset'],
                connect_timeout=self.TIMEOUT_THREAD)
        except pymysql.Error as e:
            self._error_code = e.args[0]
            error_msg = "%s --- %s" % (
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), type(e).__name__
            ), e.args[0], e.args[1]
                    
            # reconnect if not reach TIMEOUT_DEADLINE.
            if self.TIMEOUT_TOTAL < self.TIMEOUT_DEADLINE:
                interval = 0
                self.TIMEOUT_TOTAL += (interval + self.TIMEOUT_THREAD)
                time.sleep(interval)
                # return self.__init__(dbconfig)
            raise Exception(error_msg)
                                                                                        
        self._cursor = self._connect.cursor(pymysql.cursors.DictCursor)

    def get_dbconfig(self, dbconfig):
        flag = True
        if type(dbconfig) is not dict:
            flag = False
        else:
            for key in ['host', 'port', 'user', 'passwd', 'db']:
                if key not in dbconfig.keys():
                    flag = False
            if key not in dbconfig.keys():
                self._dbconfig['charset'] = 'utf8mb4'
                                                                                    
        if not flag:
            raise Exception('Dbconfig Error')
        return flag

    def query(self, sql, ret_type='all'):
        #print(sql)
        try:
            self._cursor.execute("SET NAMES utf8mb4")
            self._cursor.execute(sql)
            if ret_type == 'all':
                return self.rows2array(self._cursor.fetchall())
            elif ret_type == 'one':
                return self._cursor.fetchone()
            elif ret_type == 'count':
                return self._cursor.rowcount
        except pymysql.Error as e:
            self._error_code = e.args[0]
            print(e)
            return False

    def dml(self, sql):
        # update or delete or insert
        # print(sql)
        try:
            self._cursor.execute("SET NAMES utf8mb4")
            self._cursor.execute(sql)
            self._connect.commit()
            stype = self.dml_type(sql)
            if stype == 'insert':
                return self._connect.insert_id()
            else:
                return True
        except pymysql.Error as e:
            self._error_code = e.args[0]
            print(e)
            return False

    def dml_type(self, sql):
        re_dml = re.compile('^(?P<dml>\w+)\s+', re.I)
        m = re_dml.match(sql)
        if m:
            if m.group("dml").lower() == 'delete':
                return 'delete'
            elif m.group("dml").lower() == 'update':
                return 'update'
            elif m.group("dml").lower() == 'insert':
                return 'insert'
        return False


    def rows2array(self, data):
        '''transfer tuple to array.'''
        result = []
        for da in data:
            if type(da) is not dict:
                raise Exception('Format Error: data is not a dict.')
            result.append(da)
        return result

    def __del__(self):
        '''free source.'''
        try:
            self._cursor.close()
            self._connect.close()
        except:
            pass

    def close(self):
        self.__del__()


class Spider:
    _db = None

    def __init__(self, dbconfig):
        self._db = LightMysql(dbconfig)

    def close(self):
        self._db.close()

    def __load_database(self, table, fields, where, string=None, ret_type="all"):
        sql_select = "SELECT %s FROM %s " % (",".join(["`%s`" % v for v in fields]), table)
        strwhere = ""
        if type(where) is dict:
            arr = []
            for k, v in where.items():
                if type(v) is list:
                    arr.append("%s in (%s)" % (k, ','.join(["'%s'" % x for x in v])))
                else:
                    arr.append("%s = '%s'" % (k, v))
            if len(arr):
                strwhere = "where %s" % " AND ".join(arr)
        elif type(where) is str and len(where):
            strwhere = "where %s" % where
        if string:
            if strwhere:
                strwhere = "%s AND %s" % (strwhere, string)
            else:
                strwhere = "where %s" % string

        if strwhere:
            sql_select += strwhere

        return self._db.query(sql_select, ret_type)

    def __insert_database(self, table, param):
        if not len(param):
            return False
        field = param[0].keys()
        row = []
        for r in param:
            arr = []
            for f in field:
                if f not in r.keys():
                    return False
                arr.append("'%s'" % r[f])
            row.append("(%s)" % ",".join(arr))
        sql_insert = "INSERT INTO %s (%s) VALUES %s" % (table, ",".join(["`%s`" % v for v in field]), ",".join(row))
        return self._db.dml(sql_insert)

    def __update_database(self, table, id_key, param):
        if type(param) is not dict:
            return False

        arr = []
        for k, v in param.items():
            arr.append("%s = '%s'" % (k, v))
        if not len(arr):
            return False

        where = ""
        if type(id_key) is list:
            where = "where id in (%s)" % ','.join(['%d' % d for d in id_key])
        else:
            where = "where id=%s" % id_key
        sql_update = "update %s set %s %s" % (table, ",".join(arr), where)

        return self._db.dml(sql_update)

    # pf_task
    def load_task(self, fields, where, string=None):
        return self.__load_database("pf_task", fields, where, string)

    def update_task(self, tid, param):
        return self.__update_database("pf_task", tid, param)

    # pf_real_identity
    def load_real_identity(self, fields, where, string=None):
        return self.__load_database("pf_real_identity", fields, where, string)

    def insert_real_identity(self, param):
        return self.__insert_database("pf_real_identity", param)

    def update_real_identity(self, rid, param):
        return self.__update_database("pf_real_identity", rid, param)

    # twitter
    def load_twi_task(self, fields, where, string=None):
        return self.__load_database("pf_twi_task", fields, where, string)

    def load_twi_dynamic(self, fields, where, string=None):
        return self.__load_database("pf_twi_dynamic", fields, where, string)

    def insert_twi_task(self, param):
        return self.__insert_database("pf_twi_task", param)

    def update_twi_task(self, tid, param):
        return self.__update_database("pf_twi_task", tid, param)

    def load_twi_comment(self, fields, where, string=None):
        return self.__load_database("pf_twi_comment", fields, where, string)

    def update_twi_comment(self, cid, param):
        return self.__update_database("pf_twi_comment", cid, param)

    def load_twi_person(self, fields, where, string=None):
        return self.__load_database("pf_twi_person", fields, where, string)

    # facebook
    def load_fac_comment(self, fields, where, string=None):
        return self.__load_database("pf_fac_comment", fields, where, string)

    def update_fac_comment(self, cid, param):
        return self.__update_database("pf_fac_comment", cid, param)

    def load_fac_person(self, fields, where, string=None):
        return self.__load_database("pf_fac_person", fields, where, string)

    def load_fac_task(self, fields, where, string=None):
        return self.__load_database("pf_fac_task", fields, where, string)

    def load_fac_dynamic(self, fields, where, string=None):
        return self.__load_database("pf_fac_dynamic", fields, where, string)

    def insert_fac_task(self, param):
        return self.__insert_database("pf_fac_task", param)

    def update_fac_task(self, tid, param):
        return self.__update_database("pf_fac_task", tid, param)

    # instagram
    def load_ins_comment(self, fields, where, string=None):
        return self.__load_database("pf_ins_comment", fields, where, string)

    def update_ins_comment(self, cid, param):
        return self.__update_database("pf_ins_comment", cid, param)

    def load_ins_person(self, fields, where, string=None):
        return self.__load_database("pf_ins_person", fields, where, string)

    def load_ins_task(self, fields, where, string=None):
        return self.__load_database("pf_ins_task", fields, where, string)

    def load_ins_dynamic(self, fields, where, string=None):
        return self.__load_database("pf_ins_dynamic", fields, where, string)

    def insert_ins_task(self, param):
        return self.__insert_database("pf_ins_task", param)

    def update_ins_task(self, tid, param):
        return self.__update_database("pf_ins_task", tid, param)

    # virtual
    def load_virtual_identity(self, fields, where, string=None):
        return self.__load_database("pf_virtual_identity", fields, where, string)

    def find_virtual_identity(self, fields, where, string=None):
        return self.__load_database("pf_virtual_identity", fields, where, string, "one")

    def insert_virtual_identity(self, param):
        return self.__insert_database("pf_virtual_identity", param)

    def find_virtual_from_dynamic(self, dyid, platform):
        sql_select = "select i.id, i.url from pf_%s_dynamic d, pf_virtual_identity i where d.vid=i.id and d.id=%s" % (
            platform.lower(),
            dyid)
        return self._db.query(sql_select, 'one')

    def get_max_vid(self):
        sql_select = "select max(id) as maxid from pf_virtual_identity"
        ret = self._db.query(sql_select, 'one')
        return ret['maxid']

    # platform
    def load_platform(self, fields, where, string=None):
        return self.__load_database("pf_platform", fields, where, string)

    # news
    def load_news_stat(self, rids):
        sql = "select r.rid as rid, m.media as media, count(*) as cnt from pf_news_rela r,pf_news_media m where r.url = m.url and r.rid in (%s) group by r.rid,m.media" % ','.join(rids)
        return self._db.query(sql)

    def insert_news_task(self, param):
        return self.__insert_database("pf_news_task", param)

    def load_news_task(self, fields, where, string=None):
        return self.__load_database("pf_news_task", fields, where, string)

    def escape_string(self, string):
        return pymysql.escape_string(string)