from django.contrib import admin

# 此处加入会显示在admin页面
from .models import Question

admin.site.register(Question)
