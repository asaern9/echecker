# Generated by Django 2.2.2 on 2019-09-01 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='checker',
            field=models.CharField(choices=[('Checker 1', 'Checker 1'), ('Checker 2', 'Checker 2'), ('Checker 3', 'Checker 3')], max_length=30, null=True),
        ),
    ]
