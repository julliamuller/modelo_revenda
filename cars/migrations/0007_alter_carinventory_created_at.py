# Generated by Django 5.2.1 on 2025-06-02 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_carinventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carinventory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
