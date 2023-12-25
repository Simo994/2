from django.db import models

class Task(models.Model):
    prod = models.CharField('Название товара', max_length=100)
    name = models.CharField('Имя сотрудника', max_length=100, )
    price = models.IntegerField('Цена')
    time = models.IntegerField('Время продажи')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'