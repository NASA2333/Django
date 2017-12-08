from django.contrib import admin
from .models import BlogArticles

# Register your models here.

class BlogArticlesAdmin(admin.ModelAdmin):
	list_display = ("title","author_id","publish",'body')				#列表显示数据字段
	list_filter = ("publish","author_id")								#选项筛选
	search_fields = ("title","body")								#输入框筛选判断字段
	raw_id_fields = ("author_id",)
	date_hierarchy = "publish"										#时间筛选
	ordering = ["author"]										#排序条件    可以多个并行，list写法
	list_per_page = 10

admin.site.register(BlogArticles,BlogArticlesAdmin)


