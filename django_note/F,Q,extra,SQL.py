F,Q,extra

class UserInfo(models.Model):
	name = models.ChartField(maxlength=50)
	age = models.IntegerField
	gu = models.ForeignKet(Group,on_delete=models.DO_NOTHING)
	
class Group(models.Model):
	title = models.ChartField(maxlength=50)
	
年龄加一
F()
UserInfo.objects.all().update(age=F('age')+1)

Q()
UserInfo.objects.filter(Q(id=1) | Q(id=2))

q1=Q()
q1.connector = 'OR'
q1.children.append((id,1))
q1.children.append((id,2))
q1.children.append((id,3))

q2=Q()
q2.connector = 'OR'
q2.children.append((id,1))
q2.children.append((id,2))
q2.children.append((id,3))

conn = Q()
conn.add(q1,'ADD')
conn.add(q2,'ADD')

extra
UserInfo.objects.extra()
a.映射
#select
#select_params=None
#select 此处 from 表
UserInfo.objects.extra(select={'n':“select count(1) from Group where id=%s”},select_param=[1,])

b.条件
#where
#params=None
#select * from 表 where 此处

c.表
#tables
#select * from 表此处
#

d.排序
#order_by = None
#select * from 表 order_by 此处

UserInfo.objects.extra(select={'n':“select count(1) from Group where id=%s”},select_param=[1,],
						where=['id<%s']),params=[4,],
						tables=['group'],
						order_by=['-id'])





原生SQL语句
from django.db import connection,connections

cursor = connection.cursor()
#cursor =connections['default'].cursor()选择数据库

cursor.execute("""select * from userinfo where id = %s""",[1])
cursor.fetchone
#cursor.fetchall


简单操作
all（）
	all().only('id','name')    取字段
	all().defer('name')	不取的字段
filter()
exclute()
distinct() 
	UserInfo.objects.distinct('gu_id') 
order_by()
order_by().reverse()
using()
	UserInfo.objects.all().using('db')从哪个数据库拿数据
