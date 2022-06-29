import datetime
import os
import random

from django.db import connection

now = str(datetime.datetime.now())

# 保存人大金仓
def save_rsql(sum_t,type_fe):
    with open('./log_type/rsql/'+str(type_fe)+'能源.txt','a+') as f:
        f.write(
            str(sum_t)+
            '\n'
        )

# 保存haddop
def save_hsql(sum_t,type_fe):
    with open('./log_type/hsql/'+str(type_fe)+'能源.txt','a+') as f:
        f.write(
            str(sum_t)+
            '\n'
        )

#保存表名到hsql文件夹和rsql文件夹
def save_info(zn_table,tablename,type_fe,ip):
    with open('./log_type/rsql/'+str(type_fe)+'能源.txt', 'a+') as f:
        f.write(
            '\n'+
            '--'+str(zn_table) +"("+str(tablename)+")"+"\t"+' '+now+'  ip:'+ip+
            '\n'
        )

    with open('./log_type/hsql/' + str(type_fe) + '能源.txt', 'a+') as f:
            f.write(
                '\n' +
                '--'+str(zn_table) + "(" + str(tablename) + ")" + "\t"+' '+now + '  ip:' + ip +
                '\n'
            )




from uuid import uuid4
uuidChars = ("a", "b", "c", "d", "e", "f",
       "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
       "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5",
       "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I",
       "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
       "W", "X", "Y", "Z")
def short_uuid():
  uuid = str(uuid4()).replace('-', '')
  result = ''
  for i in range(0,8):
    sub = uuid[i * 4: i * 4 + 4]
    x = int(sub,16)
    result += uuidChars[x % 0x3E]
  return result



def pinjie(zn_table,tablename,type_fe,pre,s,flag):
    word = ''
    pre_word = ''

    if(flag==0):
        for i in range(len(pre)):
            pre_word+=str(pre[i])
    for j in range(len(s)):
        if(j>0):
            word += str(s[j])+","
    solt = ''
    for i in range(5):
        solt +=str(random.randint(0,9))
    main_jian = "'" + str(short_uuid()+solt) + "'"
    year = s[0] +','
    jidu = '0' + ','
    mounth = '0' + ','
    h_time = 'from_unixtime(unix_timestamp(),‘yyyy-MM-dd HH:mm:ss’)'
    day = 'now'
    OPERATOR_TIME = 'now'
    DATA_FLAG = "'" + "0" + "'"
    ford = 'insert into'
    if(flag==0):
        r_word = ford+" "+'"'+str(
            tablename)+'"'+" "+"values"+"("+ main_jian + ',' + year + jidu + mounth + day + ',' +pre_word + word + OPERATOR_TIME + ',' + DATA_FLAG +");"
        h_word = ford+" "+str(
            tablename)+" "+"values"+"("+ main_jian + ',' + year + jidu + mounth + h_time + ',' +pre_word + word + h_time + ',' + DATA_FLAG +");"
    else:
        r_word = ford + " " +'"'+str(
            tablename)+'"'+ " " + "values" + "(" + main_jian + ',' + year + jidu + mounth + day + ',' + word + OPERATOR_TIME + ',' + DATA_FLAG + ");"
        h_word = ford + " " +str(
            tablename)+ " " + "values" + "(" + main_jian + ',' + year + jidu + mounth + h_time + ',' + word + h_time + ',' + DATA_FLAG + ");"
    rdsql = r_word.replace(',,',',').replace("'',",'')
    hasql = h_word.replace(',,', ',').replace("'',", '')
    save_rsql(rdsql,type_fe)
    save_hsql(hasql,type_fe)
    data_sql = {
        'rdsql':rdsql,
        'hasql':hasql
    }
    return data_sql


def chuli(zn_table,tablename,type_fe,predata,data,ip):
    flag=0
    save_info(zn_table,tablename,type_fe,ip)
    fin = data.replace('\t', ' ').replace('\n', '').replace('\r', '').split('。')
    prefin =  predata.replace('\t', ' ').replace('\n', '').replace('\r', '').split('。')
    n={}
    pre_list = pinjiepre(prefin)
    for i in range(len(fin)-1):
        s = fin[i]
        try:
            pre = pre_list[i]
        except:
            flag = 1
        n[i]=pinjie(zn_table,tablename,type_fe,pre.strip().split(' '),s.strip().split(' '),flag)
    return n

def pinjiepre(pre):
    pre_list =[]
    for i in range(len(pre)):
        pre_word = ''
        pre1 = pre[i].strip().split(' ')
        for j in range(len(pre1)):
            pre_word += "'" + str(pre1[j]) + "'" + ","
        pre_list.append(pre_word)
    return pre_list

def savedatabase(sql):
    # 真正的原生sql,
    cursor = connection.cursor()
    cursor.execute(sql)
    raw = list(cursor.fetchall())
    print(cursor.rowcount)
    title = [title[0] for title in cursor.description]
    res = []
    for item in raw:  # 3
        # res.append(dict(list(zip(title, item))))
          res.append(list(item))
    data = {
        'result':res,
        'title':title,
        'row':cursor.rowcount
    }
    return data


def getFlist(path):
    datalist = []
    for i in os.listdir(path):
        datalist.append(i)
    return datalist
