跨表正反项取值
class UserInfo(models.Model):
	name = models.ChartField(maxlength=50)
	age = models.IntegerField
	gu = models.ForeignKet(Group,on_delete=models.DO_NOTHING)
	
class Group(models.Model):
	title = models.ChartField(maxlength=50)
	
正取
1.	取出QuerySet对象
	q = UserInfo.objects.all().first
	q.gu.title
2.取出格式 [{:},{:},{:},{:}]
	q = UserInfo.objects.values('id','name','gu_id')
	UserInfo.objects.values('id','name','gu_id','gu__title')
	for item in q:
		item['id']
3. 取出格式 [(,),(,),(,),(,)]
	q = UserInfo.objects.values_list('id','gu_id','gu__title')
	for item in q:
		item[0]
		
反取
1.小写表_set
	v = Group.objects.all().first()
	g = v.userinfo_set.gu()
	
2.	小写表名称
	v = Group.objects.values('id','title')
	v = Group.objects.values('id','title','userinfo')
	v = Group.objects.values('id','title','userinfo__age')
	
3.	小写表名称
	v = Group.objects.values_list('id','title')
	v = Group.objects.values_list('id','title','userinfo')
	v = Group.objects.values_list('id','title','userinfo__age')