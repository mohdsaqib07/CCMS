from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50,default="")
    thead0=models.CharField(max_length=200,default="")
    chead0=models.TextField(max_length=5000,default="")
    thead1=models.CharField(max_length=100,default="")
    chead1=models.TextField(max_length=5000,default="")
    thead2=models.CharField(max_length=100,default="")
    chead2=models.TextField(max_length=5000,default="")
    views = models.IntegerField(default=0,editable=False)
    image = models.ImageField(null=True,upload_to='home/images')
    pub_date = models.DateTimeField(auto_now_add=True)
    pub_by = models.CharField(max_length=50)
    slug = models.SlugField(max_length=30,unique=True)
    thumbnail = models.ImageField(null=True,upload_to='home/thumbnail')

    class Meta:
        verbose_name = 'Posts'
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.slug

class Comments(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField(null=True) 
    user = models.ForeignKey(User , on_delete=models.CASCADE,editable=True)
    post = models.ForeignKey(Posts , on_delete=models.CASCADE,editable=True)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True) 
    timeStamp = models.DateTimeField(auto_now_add=True)
# Create your models here.
    class Meta:
        verbose_name_plural = 'Comments'
        verbose_name = 'Comments'
    def __str__(self) -> str:
        return self.comment[0:10] + "..." + " by " + self.user.username
