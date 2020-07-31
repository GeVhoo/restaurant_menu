from django.db import models


class Category(models.Model):
    """Категории блюд."""
    category_name = models.CharField('Категория', max_length=50)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Allergen(models.Model):
    """Аллергенты, которые может содержать блюдо."""
    allergen_name = models.CharField('Аллергент', max_length=50)

    def __str__(self):
        return self.allergen_name

    class Meta:
        verbose_name = 'Аллергент'
        verbose_name_plural = 'Аллергенты'


class Dish(models.Model):
    """Информация о блюде."""
    dish_name = models.CharField('Название', max_length=150)
    energy = models.PositiveSmallIntegerField(
        'Калорийность', default=0,
        help_text='Укажите калорийность на порцию в кКал'
    )
    protein = models.PositiveSmallIntegerField(
        'Белки', default=0,
        help_text='Укажите количество белка на порцию в граммах'
    )
    fat = models.PositiveSmallIntegerField(
        'Жиры', default=0,
        help_text='Укажите количество жиров на порцию в граммах'
    )
    carbohydrates = models.PositiveSmallIntegerField(
        'Углеводы', default=0,
        help_text='Укажите количество углеводов на порцию в граммах'
    )
    price = models.PositiveSmallIntegerField(
        'Цена', default=0, help_text='Укажите цену в рублях'
    )
    image = models.ImageField(
        'Изображение', upload_to='images/dish_images/'
    )
    allergens = models.ManyToManyField(
        Allergen, verbose_name='Аллергенты', blank=True
    )
    category = models.ForeignKey(
        Category, verbose_name='Категория',
        on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.dish_name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
