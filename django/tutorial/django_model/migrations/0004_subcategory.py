# Generated by Django 3.1.7 on 2021-04-08 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_model', '0003_auto_20210408_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'subcategories',
                'db_table': 'subcategory',
                'ordering': ['name'],
            },
        ),
    ]