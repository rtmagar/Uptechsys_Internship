# Generated by Django 3.2 on 2021-04-14 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
