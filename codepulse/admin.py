from django.contrib import admin
from codepulse.models import Posts , Comments
# Register your models here.

admin.site.register((Comments))
@admin.register(Posts)
class CustomField(admin.ModelAdmin):
    fieldsets = [
        ('Basic' , {"fields": ['title','slug'],}),
        ('Content',{"fields":['thead0','chead0','thead1','chead1','thead2','chead2']}),
        ('Image Details',{"fields":['image','thumbnail'],}),
        ('Publication Details',{"fields":['pub_by'],})
    ]
    class Media:
        js = ['index.js']
