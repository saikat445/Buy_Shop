# Generated by Django 2.1.5 on 2022-04-01 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20220401_0753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='id',
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
