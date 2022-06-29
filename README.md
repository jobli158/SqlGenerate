# SqlGenerator

#### 介绍
用于生成insert脚本，根据模型生成createtable语句。根据生成结果插入相应数据库。可通过查看数据、查看表结构。确认插入是否成功！

#### 软件架构
前端：Vue+elementui
后端：django

#### 安装教程

1、 python3.6以上，django版本3.2，在后端文件夹下有requirement.txt,使用时在其目录下 cmd pip install -r requirement.txt。
2、 node用于打包Vue文件、nginx用于打包后前台页面挂起。
3、node 安装成功后在cmd下输入node -v 查看版本信息，python 安装后在cmd下使用python查看。
4、安装python,安装时勾选.path
5、进入djangoProject文件夹，点击init.bat,再点击start.bat启动后台服务
6、进入nginx文件夹找到start.bat 点击启动网页
7、网站地址：http://127.0.0.1
8、提交后在djangoProject的log_type文件夹下有生成的所有sql日志，点击保存的在type文件夹下，也可点击查看分类下载,生成kingbase sql,hlive sql,创表语句在createtable文件夹下。
9、整个文件夹放在英文目录，中文目录会出现启动错误。
10、webutil下需要解压node_moudles.zip到当前目录。



#### 使用说明
1、使用命令方式启动，前端在有node情况下，在该文件夹下cmd打开输入 npm install -g vue-cli和npm install -g @vue/cli安装vue运行环境。npm run server 启动，npm run build 打包。如用nginx启动，则需在node环境下 npm run build 打包，将生成的dist文件拷贝到nginx的Html目录，Windows环境下在nginx目录下点击nginx.exe启动，linux下在nginx目录下./nginx启动。
后端Django启动，在DjangoProject目录下python runserver 0.0.0.0:9000，Windows和linux启动命令相同。前端依赖在文件下，不需要导入。后端需要导入依赖，在djangoProject下，cmd进入输入pip install -r requirement.txt安装依赖。
2、点击启动，前端页面启动：node安装好可以在前端目录下面点击init.bat初始化环境，点击start.bat启动，点击build.bat打包,nginx目录下点击start.bat,Django后台启动:在djangoProject目录下点击start.bat.后端依赖下载：在djangoProject目录下点击init.bat。
3、目前可根据特定格式，拼接成insert语句,create table语句。支持SQl文件上传、下载、执行。
4、根据数据库的不同在后端djangoProject下的settings.py中修改数据库引擎和数据库相关基本配置。详情参考：https://blog.csdn.net/wenshuang1234/article/details/125278911。
5、前端中在webutil文件夹下修改main.vue中$http的地址，在submitsql.vue中修改对应上传action的地址,修改为自己的ip。

