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


    def validate(self, data):
        if self.instance is not None:
            user_instance = self.instance.user
            user_data = data.get('user', {})
            
            if any([
                user_instance.surname == user_data.get('surname'),
                user_instance.name == user_data.get('name'),
                user_instance.patronymic == user_data.get('patronymic'),
                user_instance.phone_number == user_data.get('phone_number'),
                user_instance.email == user_data.get('email')
            ]):
                raise serializers.ValidationError({'Изменения отклонены': 'Эти поля нельзя редактировать'})

        return data

