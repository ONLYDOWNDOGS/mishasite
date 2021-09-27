# Generated by Django 3.2.6 on 2021-09-27 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finearts', '0004_alter_portfolio_artstyle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='artstyle',
            field=models.IntegerField(choices=[(0, 'Charcoal'), (1, 'Photoshop'), (2, 'Painting'), (3, 'Reel'), (4, 'Sketching'), (5, 'Illustrator')], default=2, max_length=11),
        ),
    ]