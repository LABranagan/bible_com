# Generated by Django 2.2.4 on 2019-08-30 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentaries', '0003_auto_20190829_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='transliteration',
            field=models.CharField(default='??', max_length=50),
        ),
    ]
