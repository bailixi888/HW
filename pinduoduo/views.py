from django.forms import model_to_dict
from django.shortcuts import render, redirect
from pinduoduo.models import User
from pinduoduo.models import Sys_user
import os
# Create your views here.
#查询用户信息
def queryUsers(request):
    # 到数据库查询用户信息
    us = User.objects.all()
    # 将数据发送到页面
    context = {"ls":us}
    return render(request, "user.html", context)

def openAdd(request):
    return render(request, "userAdd.html")


def saveUser(request):
    company_name = request.GET.get('company_name')
    rds_public = request.GET.get('rds_public')
    rds_inet = request.GET.get('rds_inet')
    rds_pass = request.GET.get('rds_pass')
    collector_inet_ip = request.GET.get('collector_inet_ip')
    collector_public_ip = request.GET.get('collector_public_ip')
    cloud_inet_ip = request.GET.get('cloud_inet_ip')
    cloud_public_ip = request.GET.get('cloud_public_ip')
    cloud_key = request.GET.get('cloud_key')
    auu_key = request.GET.get('auu_key')
    dfg_key = request.GET.get('dfg_key')
    baidu_ak = request.GET.get('baidu_ak')
    baidu_serviceid = request.GET.get('baidu_serviceid')
    ptname = request.GET.get('ptname')
    aesencode = request.GET.get('aesencode')

    User.objects.create(company_name=company_name, rds_public=rds_public,rds_inet=rds_inet,rds_pass=rds_pass,collector_inet_ip=collector_inet_ip,collector_public_ip=collector_public_ip,cloud_inet_ip=cloud_inet_ip,cloud_public_ip=cloud_public_ip,cloud_key=cloud_key,auu_key=auu_key,dfg_key=dfg_key,baidu_ak=baidu_ak,baidu_serviceid=baidu_serviceid,ptname=ptname,aesencode=aesencode)
    return redirect("/queryUsers")

def deleteUser(request):
    id = request.GET.get('id')
    User.objects.filter(id=id).delete()

    return redirect("/queryUsers")



def editUser(request):
    id = request.GET.get('id')
    thisuser = User.objects.filter(id=id).first()

    context = {"user":thisuser}
    print(id)

    return render(request, "editUser.html",context)


def updateUser(request):
    id = request.GET.get('id')
    company_name = request.GET.get('company_name')
    rds_public = request.GET.get('rds_public')
    rds_inet = request.GET.get('rds_inet')
    rds_pass = request.GET.get('rds_pass')
    collector_inet_ip = request.GET.get('collector_inet_ip')
    collector_public_ip = request.GET.get('collector_public_ip')
    cloud_inet_ip = request.GET.get('cloud_inet_ip')
    cloud_public_ip = request.GET.get('cloud_public_ip')
    cloud_key = request.GET.get('cloud_key')
    auu_key = request.GET.get('auu_key')
    dfg_key = request.GET.get('dfg_key')
    baidu_ak = request.GET.get('baidu_ak')
    baidu_serviceid = request.GET.get('baidu_serviceid')
    ptname = request.GET.get('ptname')
    aesencode = request.GET.get('aesencode')
    print(rds_pass)
    User.objects.filter(id=id).update(company_name=company_name, rds_public=rds_public,rds_inet=rds_inet,rds_pass=rds_pass,collector_inet_ip=collector_inet_ip,collector_public_ip=collector_public_ip,cloud_inet_ip=cloud_inet_ip,cloud_public_ip=cloud_public_ip,cloud_key=cloud_key,auu_key=auu_key,dfg_key=dfg_key,baidu_ak=baidu_ak,baidu_serviceid=baidu_serviceid,ptname=ptname,aesencode=aesencode)

    return redirect("/queryUsers")

def login(request):
        err_msg=''
        username = request.GET.get('username')
        pwd = request.GET.get('passwd')
        alluser = Sys_user.objects.all()
        for user in alluser:
            if username == user.username and pwd == user.password and user.is_delete ==0:

                print("登录成功")
                print('user=' + username, 'pwd=' + pwd)
                return redirect("/queryUsers")

        # err_msg = "账号或密码错误"
        return render(request, "login.html")

def sureinfo(request):
        id = request.GET.get('id')
        thisuseruu = User.objects.filter(id=id).first()
        contexts = {"user": thisuseruu}
        # os.system('sh /data/mk.sh "rds_pass"')
        return render(request, "sure.html", contexts)

def devops(request):
        id = request.GET.get('id')
        company_name = request.GET.get('company_name')
        rds_public = request.GET.get('rds_public')
        rds_inet = request.GET.get('rds_inet')
        rds_pass = request.GET.get('rds_pass')
        collector_inet_ip = request.GET.get('collector_inet_ip')
        collector_public_ip = request.GET.get('collector_public_ip')
        cloud_inet_ip = request.GET.get('cloud_inet_ip')
        cloud_public_ip = request.GET.get('cloud_public_ip')
        cloud_key = request.GET.get('cloud_key')
        auu_key = request.GET.get('auu_key')
        dfg_key = request.GET.get('dfg_key')
        baidu_ak = request.GET.get('baidu_ak')
        baidu_serviceid = request.GET.get('baidu_serviceid')
        ptname = request.GET.get('ptname')
        aesencode = request.GET.get('aesencode')
        os.system('sh /data/mk.sh "rds_pass"')
        print(os.system('sh /data/mk.sh "rds_pass"'))
        print(rds_pass)
        return redirect("/queryUsers")