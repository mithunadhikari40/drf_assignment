# Generated by Django 4.0 on 2022-01-03 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(max_length=256)),
                ('price', models.FloatField()),
                ('discount', models.FloatField(default=0.0)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]