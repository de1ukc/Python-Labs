# Generated by Django 4.0.4 on 2022-05-16 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GOLOSOVANIE', '0002_alter_startpage_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slogan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Слоган',
            },
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('middle_name', models.CharField(max_length=150)),
                ('date_of_birth', models.DateField()),
                ('region', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('preview', models.ImageField(upload_to='photos/Electtions/<django.db.models.fields.CharField>/<django.db.models.fields.CharField>')),
                ('slogan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='GOLOSOVANIE.slogan')),
            ],
            options={
                'verbose_name': 'Кандидат',
                'verbose_name_plural': 'Кандидаты',
            },
        ),
    ]
