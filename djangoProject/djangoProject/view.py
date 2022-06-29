#encoding=gbk
import datetime

from django import views
from django.core import serializers

from django.http import HttpResponse, FileResponse, response, JsonResponse
from django.shortcuts import render
from djangoProject.tableutil import createtableutil, chulixiadd, createtablecomment
from djangoProject.util import chuli, savedatabase, getFlist


class index(views.View):
    def get(self, request):
        return render(request,'index.html')

    def post(self, request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META.get('HTTP_X_FORWARDED_FOR')
        else:
            ip = request.META.get('REMOTE_ADDR')
        type_fe = request.POST['hangye']
        zn_table = request.POST['ztablename']
        tablename = request.POST['tablename']
        data = request.POST['data']
        predata = request.POST['predata']
        datas=chuli(zn_table,tablename,type_fe,predata,data,ip)
        data_list = []
        for values in datas.values():
            data_list.append(values)
        d = {"data":data_list}
        # 3. 返回
        return JsonResponse(d)

class download(views.View):
    def get(self,request):
        filename = request.GET['hangye']
        filepath = ".\\rsql\{}.txt".format(filename)  # 文件所在位置
        file = open(filepath,'rb')
        return  FileResponse(file, as_attachment=True, filename=str(filename)+'能源.txt')

    def post(self,request):
        filename = request.POST['hangye']
        filepath = ".\\rsql\{}.txt".format(filename)  # 文件所在位置
        file = open(filepath,'rb')
        return FileResponse(file, as_attachment=True, filename=str(filename) + '能源.txt')

class save(views.View):
    def post(self,request):
        filename = request.POST['hangye']
        rdsql = request.POST['rsql']
        rsqlpath = ".\\rsql\{}.txt".format(filename)  # 文件所在位置
        with open(rsqlpath,"a+") as f:
            f.write(rdsql)
            f.write('\n')
        hsql =  request.POST['hsql']
        rsqlpath = ".\\hsql\{}.txt".format(filename)  # 文件所在位置
        with open(rsqlpath, "a+") as f:
            f.write(hsql)
            f.write('\n')
        rdata = {
            "status":200
        }
        return JsonResponse(rdata)

class look(views.View):
    def post(self,request):
        word = ''
        filename = request.POST['hangye']
        filepath = ".\\rsql\{}.txt".format(filename)  # 文件所在位置
        with open(filepath,'r') as f:
            lines = f.readlines()
            for line in lines:
                word += line
        return HttpResponse(word)
    def get(self, request):
        word = ''
        filename = request.GET['hangye']
        filepath = ".\\createtable\{}.txt".format(filename)  # 文件所在位置
        with open(filepath, 'r') as f:
            lines = f.readlines()
            for line in lines:
                word += line
        return HttpResponse(word)

class createtable(views.View):
    def post(self,request):
        tablename =  request.POST['tablename']
        ztablename = request.POST['ztablename']
        hangye = request.POST['hangye']
        data = request.POST['data']
        rdata = str(data.replace('INTEGER','int4')
              .replace('VARCHAR2(50)','varcharbyte')
              .replace('VARCHAR2(32)','varcharbyte')
              .replace('VARCHAR2(512)','varcharbyte')
              .replace('VARCHAR2(100)','varcharbyte')
              .replace('NUMBER(14,2)','numeric(14,2)')
              .replace('TIMESTAMP','timestamp(6)')
        ).split('\n')
        word =''
        commont_word = ''
        for i in range(len(rdata)-1):
          simpleone = rdata[i].split('\t')
          commont_word+=createtablecomment(tablename,simpleone)
          word+=chulixiadd(simpleone)
        sumword =createtableutil(tablename,word[0:-1])+"\n"+commont_word
        findata ={
            'data':sumword
        }
        with open('.\log_createtable\{}.txt'.format(hangye),"a+") as f:
            w = "--"+ztablename+"("+tablename+")"+" "+str(datetime.datetime.now())+"\n"+sumword+"\n\n"
            f.write(w)
        return JsonResponse(findata)

class savetable(views.View):
    def post(self, request):
        tablename = request.POST['tablename']
        ztablename = request.POST['ztablename']
        hangye = request.POST['hangye']
        data = request.POST['data']

        with open('.\createtable\{}.txt'.format(hangye),"a+") as f:
            word = "--"+ztablename+"("+tablename+")"+"\n"+data+"\n\n"
            f.write(word)
        return JsonResponse({"status":200})

class  savedatabases(views.View):
    def post(self,request):
        sql = request.POST['sql']
        data=savedatabase(str(sql))
        return JsonResponse(data)

class upload_sql(views.View):
    def post(self,request):
        # files = request.FILES.get('files',None)
        files = request.FILES.getlist('files')
        # type rsql or createtable
        type = 'rsql'
        # filename = request.FILES['files'].name
        i=0
        for fn in files:
            i+=1
            with open('.\\'+type+"\\"+fn.name,"wb+") as f:
                for chunk in fn.chunks():
                    f.write(chunk)
        return JsonResponse({"status":200})
class upload_table(views.View):
    def post(self,request):
        # files = request.FILES.get('files',None)
        files = request.FILES.getlist('filess')
        # type rsql or createtable
        type = 'createtable'
        # filename = request.FILES['files'].name
        i=0
        for fn in files:
            i+=1
            with open('.\\'+type+"\\"+fn.name,"wb+") as f:
                for chunk in fn.chunks():
                    f.write(chunk)
        return JsonResponse({"status":200})
class look_info(views.View):
    def get(self,request):
        sqlpath = '.\\rsql'
        tablepath = '.\\createtable'
        rsqllist = getFlist(sqlpath)
        tablelist = getFlist(tablepath)
        data = {
            "rsqllist":rsqllist,
            "tablelist":tablelist
        }
        return JsonResponse(data)



