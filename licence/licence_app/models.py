from django.db import models

# Create your models here.
class Licence_Data(models.Model):
    #ADMIN = 'ADMIN'
    #MANAGER = 'MANAGER'
    #USER = 'USER'
    #usertype = [(ADMIN,'ADMIN'), (MANAGER,'MANAGER'),(USER,'USER')]
    id = models.AutoField(primary_key=True)
    #user_type = models.CharField(max_length=10, choices=usertype, default='USER')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    pdf= models.FileField(upload_to='documents')
    
    def __str__(self):
        return self.name
