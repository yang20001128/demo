from django.db import models


# Create your models here.
class Author(models.Model):
    Name = models.CharField(max_length=100, verbose_name='名称')
    gender_choices = (
        (1, '男性'),
        (2, '女性'),
        (3, '未定'),
    )
    Gender = models.IntegerField(choices=gender_choices, default=3, verbose_name='性别')
    Born_Date = models.DateField(verbose_name='出生日期')

    def __str__(self):
        return self.Name


class Book(models.Model):
    Book_Name = models.CharField(max_length=100, verbose_name='书名')
    Publish_Date = models.DateField(verbose_name='发布时间')
    Country = models.CharField(max_length=100, verbose_name='国家')
    Author = models.ForeignKey('Book', on_delete=models.CASCADE)
