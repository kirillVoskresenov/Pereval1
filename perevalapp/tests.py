from django.test import TestCase
from rest_framework.exceptions import ValidationError
from rest_framework.test import APITestCase
from .models import Pereval, Coordinate, User, Image, Level
from .serializers import PerevalSerializer
from .. import pereval


class PointAddModelTest(TestCase):

    def setUp(self):
        self.coords = Coordinate.objects.create(length=5.80000000, width=5.40000000, height=10)
        self.user = User.objects.create(
            surname='Иванов',
            name='Иван',
            patronymic='Иванович',
            email='e@example.com',
            phone_number='89999999999'
        )
        self.image = Image.objects.create(
            title='эльбрус',
            data='http://127.0.0.1:8000/70586_GRYZeHJ.jpg'
        )
        self.level = Level.objects.create(
            winter_level='1A',
            spring_level='1A',
            summer_level='1A',
            autumn_level='1A'
        )
        self.coords = self.coords  # Инициализируем self.coords

    def test_create_point_add(self):
        pereval = Pereval.objects.create(
            beauty_title='Пик Эльбруса',
            title='Эльбрус',
            other_titles='Красота',
            connect='',
            coords=self.coords,
            user=self.user,
            level=self.level
        )

        self.assertIsInstance(pereval, Pereval)
        self.assertEqual(pereval.beauty_title, 'Пик Эльбруса')
        self.assertEqual(pereval.title, 'Эльбрус')
        self.assertEqual(pereval.other_titles, 'Красота')
        self.assertEqual(pereval.connect, '')
        self.assertEqual(pereval.user, self.user)
        self.assertEqual(pereval.coords, self.coords)
        self.assertEqual(pereval.level, self.level)
        self.assertEqual(pereval.status, Pereval.NEW)

    def test_title_unique_constraint(self):
        # Проверка уникальности поля title
        Pereval.objects.create(
            beauty_title='Пик Эльбруса',
            title='Эльбрус',
            other_titles='Красота',
            connect='',
            coords=self.coords,
            user=self.user,
            level=self.level
        )
        with self.assertRaises(Exception):
            Pereval.objects.create(
                beauty_title='Пик Эльбруса-2',
                title='Эльбрус',
                other_titles='Другое описание',
                connect='',
                coords=self.coords,
                user=self.user,
                level=self.level
            )

    def test_other_titles_unique_constraint(self):
        Pereval.objects.create(
            beauty_title='Пик Эльбруса',
            title='Эльбрус',
            other_titles='Красота',
            connect='',
            coords=self.coords,
            user=self.user,
            level=self.level
        )
        with self.assertRaises(Exception):
            Pereval.objects.create(
                beauty_title='Пик Эльбруса-3',
                title='Другой Эльбрус',
                other_titles='Красота',
                connect='',
                coords=self.coords,
                user=self.user,
                level=self.level
            )

    def test_status_choices(self):
        pereval = Pereval.objects.create(
            beauty_title='Пик Эльбруса',
            title='Эльбрус',
            other_titles='Красота',
            connect='',
            coords=self.coords,
            user=self.user,
            level=self.level
        )
        pereval.status = Pereval.ACCEPTED  # Исправлено на point
        pereval.save()
        self.assertEqual(pereval.status, Pereval.ACCEPTED)

    def test_date_auto_now_add(self):
        point = Pereval.objects.create(
            beauty_title='Пик Эльбруса',
            title='Эльбрус',
            other_titles='Красота',
            connect='',
            coords=self.coords,
            user=self.user,
            level=self.level
        )

        self.assertIsNotNone(point.date)

    def test_serializer_update_with_invalid_status(self):
        self.pereval.status = 'AC'  # Устанавливаем статус, который не разрешает обновление
        self.pereval.save()
        data = {
            'beauty_title': 'Пик Эльбруса',
            'title': 'Эльбрус',
            'other_titles': 'Красота',
            'connect': '',
            'coords': {'length': '5.80000000', 'width': '5.40000000', 'height': 10},
            'user': {'surname': 'Иванов', 'name': 'Иван', 'patronymic': 'Иванович', 'email': 'e@example.com',
                     'phone': '89999999999'},
            'level': {'winter_level': '1A', 'spring_level': '1A', 'summer_level': '1A', 'autumn_level': '1A'},
        }

        serializer = PerevalSerializer(instance=self.pereval, data=data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
