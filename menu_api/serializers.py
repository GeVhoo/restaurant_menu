from rest_framework import serializers

from menu.models import Dish


class DishAddSerializer(serializers.ModelSerializer):
    """Добавление блюда в меню."""
    class Meta:
        model = Dish
        fields = '__all__'


class MenuListSerializer(serializers.ModelSerializer):
    """Список блюд из меню."""

    category = serializers.SlugRelatedField(
        slug_field='category_name', read_only=True)

    allergens = serializers.SlugRelatedField(
        slug_field='allergen_name', read_only=True, many=True)

    class Meta:
        model = Dish
        exclude = ['id', 'image']
