# Generated by Django 4.0.4 on 2022-05-14 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StartPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arztozka_img', models.ImageField(upload_to='photos/Start_Page/')),
            ],
        ),
    ]