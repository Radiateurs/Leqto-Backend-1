# Generated by Django 2.0.6 on 2018-06-22 00:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import enumchoicefield.fields
import lesson.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.CharField(blank=True, max_length=2048, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('sub_title', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=64000)),
                ('module', models.CharField(max_length=40)),
                ('date_time', models.DateTimeField()),
                ('payment_type', enumchoicefield.fields.EnumChoiceField(default=lesson.models.PaymentType(1), enum_class=lesson.models.PaymentType, max_length=10)),
                ('tag', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('street', models.CharField(max_length=256)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lesson.City')),
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lesson.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson.Location')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lesson.Location')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='school_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lesson.School'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='room_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='lesson.Room'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feedback',
            name='lesson_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson.Lesson'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lesson.Country'),
        ),
    ]
