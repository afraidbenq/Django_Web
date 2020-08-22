##Django 
前段后端不分离（耦合度高，适合纯网页的应用！）

##Django REST framework
前段后端分离（耦合度低，前端通过访问接口来对数据进行增删改查）
>[为什么要前后端分离](https://blog.csdn.net/sod5211314/article/details/80601724?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-5.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-5.nonecase)


##常用命令
查询当前django版本
```
$ python -m django --version
```

CMD当前路径下创建项目
```
$ django-admin startproject project_name
```

启动开发用服务器(默认8000端口)
```
$ python manage.py runserver
```

公开处刑
```
settings.py文件中DEBUG代码
DEBUG = False
ALLOWED_HOSTS = ["*"]
$ python manage.py runserver 0.0.0.0:8000
```

创建应用
```
$ python manage.py startapp app_name
```








