from django.db import models

# Create your models here.
class Hotel(models.Model):
    hname=models.CharField(max_length=80)
    cname=models.CharField(max_length=80)
    cno=models.IntegerField()
    cin=models.DateTimeField()
    cout=models.DateTimeField()
    
    def __str__(self):
        return self.hname
    class Meta:
        # verbose_name="Hotel Name"
        verbose_name_plural="Hotel Name"