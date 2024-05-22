from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
	objects = None
	name = models.CharField(max_length=100, verbose_name='Наименование')
	description = models.TextField(verbose_name='Описание')

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

class Product(models.Model):
	objects = None
	name = models.CharField(max_length=100, verbose_name='Наименование')
	description = models.TextField(verbose_name='Описание')
	image = models.ImageField(upload_to='catalog/', verbose_name='Изображение', **NULLABLE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)   # ссылается на категорию(один ко многим)
	price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за покупку')
	created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
	updated_at = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

	def __str__(self):
		return f'{self.name} \n {self.description}'
