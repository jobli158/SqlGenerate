# coding=gbk
def createtableutil(tablenames,s):
    ford = 'CREATE TABLE'
    tablename = "\"" + tablenames + "\""
    finall = ford + " " + tablename + " " + "(" + s + ");"
    return finall

def chulixiadd(s):
    isprimary = ''
    isnull = 'null'
    if (str(s[3]) == '是'):
        isprimary = 'primary key'
    if (str(s[4]) == '否'):
        isnull = 'not null'
    if (str(s[0])=='DATA_FLAG'):
        data = "default '0'"
        word = "\"" + s[0] + "\"" + "  " + s[2] + " " + isprimary + " " + isnull+" "+data+"\n"
    else:
        word = "\"" + s[0] + "\"" + "  " + s[2] + " " + isprimary + " " + isnull+","+"\n"
    return word

def createtablecomment(tablenames,s):
    comment_column = "\"" + s[0] + "\""
    comment_value = "'" + s[1] + "'"
    comment_word = comment_column + " " + "IS" + " " + comment_value + ";" + "\n"
    comment_ford = "COMMENT ON COLUMN "
    comment_table = "\"" + tablenames + "\""
    comment_finall = comment_ford + " " + comment_table + "."+comment_word
    return comment_finall



