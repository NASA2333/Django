from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class BlogArticles(models.Model):
	title = models.CharField(max_length=300)							#定义字段title属性为charField，及最大长度
	author = models.ForeignKey(User,related_name='blog_posts')			#定义规定文章与用户为一对多的关系
	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now())

	class Meta():
		ordering = ("-publish",)								#定义BlogArticles按照publish字段值倒序显示

	def __str__(self):
		return self.title

