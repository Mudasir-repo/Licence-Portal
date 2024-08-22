from django.db import models

# Create your models here.
class Licence_Data(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    pdf= models.FileField(upload_to='documents')
    
    def __str__(self):
        return self.name
