# Generated by Django 3.2.9 on 2022-01-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speech', '0002_auto_20220129_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='correctword',
            name='grade',
            field=models.CharField(default='exit', max_length=50),
            preserve_default=False,
        ),
    ]