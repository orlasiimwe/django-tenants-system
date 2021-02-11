from django.db import models

class Tenant(models.Model):
    id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    company=models.CharField(max_length=20)
    temperature=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    id_no= models.CharField(blank=True,max_length=20,null=True)

    class Meta:
        ordering=['-date']

    def __str__(self):
        return self.first_name

    