# Generated by Django 2.2 on 2019-04-26 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32)),
            ],
        ),
    ]
