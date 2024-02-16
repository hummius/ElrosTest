from django.db import models


class Country(models.Model):
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    title = models.CharField(max_length=100, unique=True, verbose_name='Имя')

    def __str__(self):
        return self.title


class Manufacturer(models.Model):
    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    title = models.CharField(max_length=100, unique=True, verbose_name='Имя')
    country = models.ForeignKey(Country, null=False, to_field="id", related_name="manufacturer",
                                on_delete=models.CASCADE, verbose_name="Страна")

    def __str__(self):
        return f"{self.title} ({self.country})"


class Automobile(models.Model):
    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    title = models.CharField(max_length=100, unique=True, verbose_name='Имя')
    manufacturer = models.ForeignKey(Manufacturer, null=False, to_field="id", related_name='automobile',
                                     on_delete=models.CASCADE, verbose_name="Производитель")
    start_year = models.PositiveSmallIntegerField(null=True, blank=True,
                                                  verbose_name='Год начала выпуска')
    end_year = models.PositiveSmallIntegerField(null=True, blank=True,
                                                verbose_name='Год окончания выпуска')

    def __str__(self):
        return f"{self.title} - {self.manufacturer.__str__()}"


class Commentaries(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    email = models.EmailField(verbose_name='Email автора')
    automobile = models.ForeignKey(Automobile, null=False, to_field="id", related_name="comment_parent_id",
                                   on_delete=models.CASCADE,verbose_name="Автомобиль")
    create_data = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    comment = models.TextField(verbose_name='Комментарий')

