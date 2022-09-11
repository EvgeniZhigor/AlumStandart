from django.db import models


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ваше имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Форма обратной связи"
        verbose_name_plural = "Формы обратной связи"


class Window(models.Model):
    name = models.CharField('Название',max_length=250)
    description = models.TextField('Описание')
    feature = models.TextField('Характеристики')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Окно'
        verbose_name_plural = 'Окна'


class Door(models.Model):
    name = models.CharField('Название',max_length=250)
    description = models.TextField('Описание')
    feature = models.TextField('Характеристики')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Дверь'
        verbose_name_plural = 'Двери'


class Fire_door(models.Model):
    name = models.CharField('Название',max_length=250)
    description = models.TextField('Описание')
    feature = models.TextField('Характеристики')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Противопожарная дверь'
        verbose_name_plural = 'Противопожарные двери'


class Dym_door(models.Model):
    name = models.CharField('Название',max_length=250)
    description = models.TextField('Описание')
    feature = models.TextField('Характеристики')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Дымонепроницаемая дверь'
        verbose_name_plural = 'Дымонепрониаемые двери'


class Patio(models.Model):
    name = models.CharField('Название',max_length=250)
    description = models.TextField('Описание')
    feature = models.TextField('Характеристики')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Наклонно-сдвижная система'
        verbose_name_plural = 'Наклонно-сдвижные системы'


class Sl(models.Model):
    name = models.CharField('Название',max_length=250)
    description = models.TextField('Описание')
    feature = models.TextField('Характеристики')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Подъёмно-сдвижная система'
        verbose_name_plural = 'Подъёмно-сдвижные системы'


class Fasad(models.Model):
    name = models.CharField('Название',max_length=250)
    description = models.TextField('Описание')
    feature = models.TextField('Характеристики')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Остекление фасада'
        verbose_name_plural = 'Остекление фасадов'


class Ms(models.Model):
    name = models.CharField('Название',max_length=250)
    description = models.TextField('Описание')
    feature = models.TextField('Характеристики')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Москитная сетка'
        verbose_name_plural = 'Москитные сетки'


class Windowsill(models.Model):
    name = models.CharField('Название',max_length=250)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Подоконник'
        verbose_name_plural = 'Подоконники'


class Otliv(models.Model):
    name = models.CharField('Название',max_length=250)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Отлив'
        verbose_name_plural = 'Отливы'