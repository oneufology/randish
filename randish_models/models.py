from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Ingredients(models.Model):
    ingredient_name = models.CharField(max_length=50, verbose_name = "Ингредиент" )

    def __str__(self):
        return self.ingredient_name

    class Meta:
        ordering = ('ingredient_name', )
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"



class DishModel(models.Model):
    TYPE_CHOICE = (
        ('Салаты', "Салаты"),
        ('Закуски', "Закуски"),
        ('Первые блюда', "Первые блюда"),
        ('Основные блюда', "Основные блюда"),
        ('Гарниры', "Гарниры"),
        ('Соусы и подливы', "Соусы и подливы"),
        ('Десерты', "Десерты"),
        ('Выпечка', "Выпечка"),
        ('Напитки', "Напитки"),
        ('Консервирование', "Консервирование"),
    )

    dish_name = models.CharField(max_length=50, verbose_name = "Название") #Name
    dish_type = models.CharField(max_length=50, choices=TYPE_CHOICE, verbose_name = "Тип блюда") #Type
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media', verbose_name = "Картинка")
    ingredients = models.ManyToManyField(Ingredients, verbose_name = "Ингредиенты")

    def __str__(self):
        return self.dish_name

    class Meta:
        ordering = ('dish_name', )
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"