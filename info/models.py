from django.db import models

class Guest(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='ФИО')
    mail = models.EmailField(max_length=255, unique=True, verbose_name='Ваша эл. почта')
    phone = models.IntegerField(unique=True, verbose_name='Номер тел.')
    CPU_vendor = models.ForeignKey('CPU_Vendors', on_delete=models.PROTECT, null=True, verbose_name='Производитель ЦП')
    GPU_vendor = models.ForeignKey('GPU_Vendors', on_delete=models.PROTECT, null=True, verbose_name='Производитель ГПУ')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    agree = models.BooleanField(default=True, verbose_name='Подтвердить условия')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['time_create', 'name']

class CPU_Vendors(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class GPU_Vendors(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
