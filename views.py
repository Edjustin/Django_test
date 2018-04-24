from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from account.models import User


# def index(request):
#     return render(request, 'index.html')


def login(request):
    # 请求获取数据
    username = request.GET.get('username')
    password = request.GET.get('password')
    # User.objects.create(username=username,password=password)
    try:
        user = User.objects.get(username=username, password=password)  # == select * from T_qq where username='xiaoming'
        if user:
            if user.password == password:
                return HttpResponse('登录成功')
            else:
                return HttpResponse('密码错误')
        else:
            return HttpResponse('账号不存在')
    except:
        return HttpResponse('网络异常')
    #     return render(request, 'login.html')


def register(request):
    # 获取客服端端通过get请求发送过来的数据
    username = request.GET.get('username')
    password = request.GET.get('password')
    # result = '注册失败'
    try:
        user = User.objects.filter(username=username)
        if user:
            return HttpResponse ('用户已存在')
        else:
            User.objects.create(username=username, password=password)
            return HttpResponse('注册成功')
    except:
        return HttpResponse('账号不存在')
