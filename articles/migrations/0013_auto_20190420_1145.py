# Generated by Django 2.0.7 on 2019-04-20 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_auto_20190420_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commenttuser',
            name='article',
            field=models.CharField(max_length=20, verbose_name='评论的文章'),
        ),
    ]
