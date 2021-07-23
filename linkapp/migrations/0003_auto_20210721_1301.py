# Generated by Django 3.2.5 on 2021-07-21 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkapp', '0002_auto_20210721_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.BigIntegerField()),
                ('domain_name', models.URLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='domain_name',
        ),
    ]