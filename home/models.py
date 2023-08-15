from django.db import models

class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,null=True,editable=False)
    email=models.EmailField(max_length=25,null=True)
    number=models.CharField(max_length=13,null=True)
    concern=models.TextField(max_length=5000,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name="Contact"
        verbose_name_plural="Contact"

    def __str__(self):
        return self.name




# Create your models here.
