from django.shortcuts import render

# Create your views here.
from cmdb import models

"""
user_list = [
    {"user": "paul", "pwd": "123"},
    {"user": "jack", "pwd": "abc"},
]
"""


def index(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        # temp = {"user": username, "pwd": password}
        # user_list.append(temp)

        """
        添加用户输入到数据库
        """
        models.UserInfo.objects.create(user=username,pwd=password)
        print(username, password)
    user_list = models.UserInfo.objects.all()
    return render(request, 'index.html', {"data": user_list})
