from rest_framework import serializers
from .models import Pereval, Coordinate, Image, User, Level


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
            'image'
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
        user = validated_data.pop('user')
        coords = validated_data.pop('coords')
        level = validated_data.pop('level')
        image = validated_data.pop('image')

        user_instance = User.objects.create(**user)
        coords_instance = Coordinate.objects.create(**coords)
        level_instance = Level.objects.create(**level)
        pereval = Pereval.objects.create(**validated_data, user=user_instance, coords=coords_instance, level=level_instance)


        for i in image:
            image = i.pop('image')
            title = i.pop('title')
            Image.objects.create(title=title, image=image, pereval=pereval)
        return pereval



    def validate(self, data):
        if self.instance is not None:
            if self.instance.status != 'NW':
                raise serializers.ValidationError(
                    f'Отказ! Причина: статус {self.instance.get_status_display()}'
                )
            user = self.instance.user
            user_data = data.get('user', {})
            user_fields = [
                user.surname != user_data.get('surname'),
                user.name != user_data.get('name'),
                user.patronymic != user_data.get('patronymic'),
                user.email != user_data.get('email'),
                user.phone_number != user_data.get('phone_number'),
            ]
            if any(user_fields):
                raise serializers.ValidationError(
                    f'Отклонено! Нельзя менять данные пользователя'
                )
        return data
