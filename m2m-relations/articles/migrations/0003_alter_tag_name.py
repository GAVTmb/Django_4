# Generated by Django 4.1.5 on 2023-01-27 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_scope_alter_article_options_tag_scope_article_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=25, unique=True, verbose_name='Тег'),
        ),
    ]