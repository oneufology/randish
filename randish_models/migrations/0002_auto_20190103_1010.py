# Generated by Django 2.1.3 on 2019-01-03 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randish_models', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dishmodel',
            options={'ordering': ('dish_name',), 'verbose_name': 'Блюдо', 'verbose_name_plural': 'Блюда'},
        ),
        migrations.AlterModelOptions(
            name='ingredients',
            options={'ordering': ('ingredient_name',), 'verbose_name': 'Ингредиент', 'verbose_name_plural': 'Ингредиенты'},
        ),
        migrations.AlterField(
            model_name='dishmodel',
            name='dish_name',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='dishmodel',
            name='dish_type',
            field=models.CharField(choices=[('first_course', 'Первое блюдо'), ('snacks', 'Закуски'), ('salad', 'Салат'), ('dessert', 'Десерт')], max_length=50, verbose_name='Тип блюда'),
        ),
        migrations.AlterField(
            model_name='dishmodel',
            name='image',
            field=models.ImageField(upload_to='image', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='dishmodel',
            name='ingredients',
            field=models.ManyToManyField(to='randish_models.Ingredients', verbose_name='Ингредиенты'),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='ingredient_name',
            field=models.CharField(max_length=50, verbose_name='Ингредиент'),
        ),
    ]