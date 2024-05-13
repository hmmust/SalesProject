from django.db import models

# Create your models here.

class Supplier(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,unique=True)


    def __str__(self):
        return self.name
class Product(models.Model):
    TYPE_CHOICES = [(1, "Personal Computer"), (2, "Home Electric"), (3, "Food")]
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,unique=True)
    description = models.CharField(max_length=500)
    active = models.BooleanField()
    supplier_email = models.EmailField()
    type= models.IntegerField(choices=TYPE_CHOICES)
    purchase_date = models.DateField()
    quantity = models.IntegerField()
    supplier = models.ForeignKey(Supplier , related_name="sproducts", on_delete=models.CASCADE,default=0)

    def __str__(self):
        return self.name
