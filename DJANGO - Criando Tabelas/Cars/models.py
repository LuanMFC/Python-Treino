from django.db import models

class Cars(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200, null=False)
    