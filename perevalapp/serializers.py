from rest_framework import serializers
from .models import Pereval, Coordinate, Image, User, Level
from rest_framework.response import Response
from rest_framework.views import status

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'surname',
            'name',
            'patronymic',
            'email',
            'phone_number'
        )


class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = (
            'length',
            'width',
            'height'
        )


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = (
            'winter_level',
            'summer_level',
            'spring_level',
            'autumn_level'
        )


class ImageSerializer(serializers.ModelSerializer):


    class Meta:
        model = Image
        fields = (
            'title',
            'data'
        )


class PerevalSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordSerializer()
    level = LevelSerializer()
    image = ImageSerializer(many=True)
    add_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Pereval
        fields = (
            'beauty_title',
            'title',
            'other_titles',
            'connect',
            'add_time',
            'user',
            'coords',
            'level',
            'image',
            'status'
        )

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        coords_data = validated_data.pop('coords')
        level_data = validated_data.pop('level')
        image_data = validated_data.pop('image')

        user_instance = User.objects.create(**user_data)
        coords_instance = Coordinate.objects.create(**coords_data)
        level_instance = Level.objects.create(**level_data)
        pereval = Pereval.objects.create(**validated_data, user=user_instance, coords=coords_instance, level=level_instance)

        for img_data in image_data:
            title = img_data.pop('title')
            image_file = img_data.pop('image')
            Image.objects.create(pereval=pereval, title=title,
                                 image=image_file)
        return pereval


    def validate(self, data):
        if self.instance is not None:
            user_instance = self.instance.user
            user_data = data.get('user')
            if user_instance.surname == user_data.get('surname') \
                or user_instance.name == user_data.get('name') \
                or user_instance.patronymic == user_data.get('patronymic') \
                or user_instance.phone_number == user_data.get('phone_number') \
                or user_instance.email == user_data.get('email'):
                return data
            else:
                raise serializers.ValidationError({'Изменения отклонены': 'Эти поля нельзя редактировать'})

