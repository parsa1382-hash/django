from django.contrib import admin
from .models import Question, Choice
#from .models import Blog, Author, Entry
admin.site.register(Question)
admin.site.register(Choice)

'''
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
'''
# Register your models here.
