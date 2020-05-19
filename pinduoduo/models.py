from django.db import models

# Create your models here.
class User(models.Model):

    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    rds_public = models.CharField(max_length=100)
    rds_inet = models.CharField(max_length=100)
    rds_pass = models.CharField(max_length=100)
    collector_inet_ip = models.CharField(max_length=100)
    collector_public_ip = models.CharField(max_length=100)
    cloud_inet_ip = models.CharField(max_length=100)
    cloud_public_ip = models.CharField(max_length=100)
    cloud_key = models.CharField(max_length=100)
    auu_key = models.CharField(max_length=100)
    dfg_key = models.CharField(max_length=100)
    baidu_ak = models.CharField(max_length=100)
    baidu_serviceid = models.CharField(max_length=100)
    ptname = models.CharField(max_length=100)
    aesencode = models.CharField(max_length=100)

class Sys_user(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    is_delete = models.BooleanField(default=False)