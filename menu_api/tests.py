from io import BytesIO
from PIL import Image as PilImage
from django.core.files.uploadedfile import SimpleUploadedFile

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from menu.models import Dish, Allergen, Category
from restaurant_menu.settings import API_TOKEN


class DishAddTests(APITestCase):
    """Тесты для API добавления блюда в меню."""

    def setUp(self):
        test_allergen1 = Allergen.objects.create(allergen_name='Соль')
        test_allergen2 = Allergen.objects.create(allergen_name='Сахар')

        test_category = Category.objects.create(category_name='Пироги')

        image = BytesIO()
        PilImage.new('RGB', (250, 250)).save(image, 'JPEG')
        image.seek(0)
        test_image = SimpleUploadedFile('image.jpg', image.getvalue())

        self.test_dish = {
            'dish_name': 'Американский пирог',
            'image': test_image,
            'category': test_category.id,
            'allergens': [test_allergen1.id, test_allergen2.id]
        }

        self.default_data = {
            'energy': 0,
            'protein': 0,
            'fat': 0,
            'carbohydrates': 0,
            'price': 0,
            'image': 'http://testserver/media/',
        }

    def test_dish_add(self):
        self.client.credentials(HTTP_API_TOKEN=API_TOKEN)
        response = self.client.post(
            reverse('menu_api:dish_add'),
            self.test_dish,
            format='multipart',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        object_from_db = Dish.objects.get(id=response.json()['id'])
        self.test_dish.update(self.default_data)
        self.test_dish['id'] = object_from_db.id
        self.test_dish['image'] += str(object_from_db.image)
        self.assertEqual(response.json(), self.test_dish)
