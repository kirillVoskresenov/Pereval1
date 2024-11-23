# Generated by Django 4.2.16 on 2024-11-23 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.FloatField()),
                ('width', models.FloatField()),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter_level', models.CharField(choices=[('1A', '1A'), ('1Б', '1Б'), ('2A', '2A'), ('2Б', '2Б'), ('3A', '3A'), ('3Б', '3Б')], default='1A', max_length=2)),
                ('spring_level', models.CharField(choices=[('1A', '1A'), ('1Б', '1Б'), ('2A', '2A'), ('2Б', '2Б'), ('3A', '3A'), ('3Б', '3Б')], default='1A', max_length=2)),
                ('summer_level', models.CharField(choices=[('1A', '1A'), ('1Б', '1Б'), ('2A', '2A'), ('2Б', '2Б'), ('3A', '3A'), ('3Б', '3Б')], default='1A', max_length=2)),
                ('autumn_level', models.CharField(choices=[('1A', '1A'), ('1Б', '1Б'), ('2A', '2A'), ('2Б', '2Б'), ('3A', '3A'), ('3Б', '3Б')], default='1A', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=255, verbose_name='Отчество')),
                ('phone_number', models.CharField(max_length=12, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('other_titles', models.CharField(max_length=255)),
                ('connect', models.TextField(blank=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', 'New'), ('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='new', max_length=255)),
                ('coords', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perevalapp.coordinate')),
                ('image', models.ManyToManyField(to='perevalapp.image')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perevalapp.level')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perevalapp.user')),
            ],
        ),
    ]
