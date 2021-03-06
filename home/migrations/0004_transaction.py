# Generated by Django 3.2.4 on 2021-07-04 12:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210703_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TransactionId', models.CharField(max_length=10)),
                ('FromAccNo', models.CharField(max_length=5)),
                ('ToAccNo', models.CharField(max_length=5)),
                ('Amount', models.IntegerField()),
                ('dateTime', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
