# Generated by Django 4.0 on 2022-05-25 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GOLOSOVANIE', '0017_candidate_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='candidate_to_support',
            field=models.ManyToManyField(to='GOLOSOVANIE.Candidate', verbose_name='Канидаты'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='description',
            field=models.TextField(verbose_name='Информация'),
        ),
        migrations.AlterField(
            model_name='slogan',
            name='slogan',
            field=models.CharField(max_length=150, verbose_name='Слоган'),
        ),
    ]
