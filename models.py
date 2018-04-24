from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    # 允许为NULL为空
    username = models.CharField(max_length=32, null=True)
    password = models.CharField(max_length=32)
    sex = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    create_date = models.DateField(auto_now_add=True)
    last_time = models.DateTimeField(auto_now=True)

    # class Meta:
    #     # 基类
    #     abstract = True
    #     # 更改表名
    #     db_table = 'T-qq'
    #     # 默认是升序  加个-表示降序  ?随机排序
    #     ordering = ['create_date']
    #     verbose_name = '用户'
    #     verbose_name_plural = '用户列表'
    #     # 创建索引
    #     indexes = ['username']





