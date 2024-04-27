from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'smartphone_brand'

    def __str__(self):
        return self.name

class Madel(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, models.DO_NOTHING, null=True,)

    class Meta:
        managed = False
        db_table = 'smartphone_madel'

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    brand = models.ForeignKey(Brand, models.DO_NOTHING)
    madel = models.ForeignKey(Madel, models.DO_NOTHING)
    price = models.IntegerField()
    color = models.CharField(max_length=50)
    memory = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'smartphone_product'

    def __str__(self):
        return self.title