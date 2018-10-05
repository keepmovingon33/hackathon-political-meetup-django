# Generated by Django 2.1.1 on 2018-10-05 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('political_meetup_app', '0002_auto_20181004_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
            ],
        ),
    ]