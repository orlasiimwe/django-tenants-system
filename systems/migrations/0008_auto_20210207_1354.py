# Generated by Django 3.1.6 on 2021-02-07 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0007_auto_20210207_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='id_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
