# Generated by Django 4.0.4 on 2022-05-17 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GOLOSOVANIE', '0009_alter_candidate_batch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='batch',
            field=models.ForeignKey(default='Самовыдвиженец', null=True, on_delete=django.db.models.deletion.CASCADE, to='GOLOSOVANIE.batch', verbose_name='Партия'),
        ),
    ]
