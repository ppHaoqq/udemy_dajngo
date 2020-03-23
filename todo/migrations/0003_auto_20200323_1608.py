# Generated by Django 3.0.3 on 2020-03-23 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200323_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='original_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='定価'),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='著者'),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='eval',
            field=models.CharField(blank=True, choices=[('★☆☆☆☆', '★☆☆☆☆'), ('★★☆☆☆', '★★☆☆☆'), ('★★★☆☆', '★★★☆☆'), ('★★★★☆', '★★★★☆'), ('★★★★★', '★★★★★')], max_length=100, null=True, verbose_name='評価'),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='kind',
            field=models.CharField(blank=True, choices=[('Python', 'Python'), ('お金', 'お金'), ('ビジネス', 'ビジネス'), ('勉強', '勉強'), ('知識', '知識')], max_length=100, null=True, verbose_name='種別'),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='金額'),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='review',
            field=models.TextField(blank=True, max_length=400, null=True, verbose_name='レビュー'),
        ),
    ]
