from django.db import models

class brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class car(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(brand, on_delete=models.PROTECT, related_name='car')
    model = models.CharField(max_length=200)
    year = models.IntegerField()
    color = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='cars/')
    
    def __str__(self):
        return self.name
