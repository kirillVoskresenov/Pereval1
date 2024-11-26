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

    def patch(self, validated_data):
        user_data = validated_data.pop('user')
        coords_data = validated_data.pop('coords')
        level_data = validated_data.pop('level')
        image_data = validated_data.pop('image')

        user_instance = User.objects.update(**user_data)
        coords_instance = Coordinate.objects.update(**coords_data)
        level_instance = Level.objects.update(**level_data)
        pereval = Pereval.objects.update(**validated_data, user=user_instance, coords=coords_instance,
                                         level=level_instance)

        for img_data in image_data:
            title = img_data.pop('title')
            image_file = img_data.pop('image')
            Image.objects.update(pereval=pereval, title=title,
                                 image=image_file)
        return pereval