# Generated by Django 2.2.2 on 2019-09-01 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_order_checker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='checker',
            field=models.CharField(choices=[('Checker 1', 'Checker 1'), ('Checker 2', 'Checker 2'), ('Checker 3', 'Checker 3')], default='Checker 1', max_length=30, null=True),
        ),
    ]
