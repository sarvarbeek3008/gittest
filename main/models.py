from django.db import models


# Create your models here.

class Category(models.Model):
    name_uz = models.CharField(max_length=120)
    name_ru = models.CharField(max_length=120)

    class Meta:
        verbose_name="Kategoriyalar"

    def __str__(self):
        return self.name_uz


class Product(models.Model):
    category=models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
    name_uz=models.CharField(max_length=150)
    name_ru=models.CharField(max_length=150)
    text_uz=models.TextField()
    img=models.ImageField(upload_to="images/")
    price=models.PositiveIntegerField()

    class Meta:
        verbose_name="Mahsulotlar"

    def __str__(self):
        return self.name_uz

