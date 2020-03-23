from django.db import models

# Create your models here.
class BookModel(models.Model):
    KIND = (
        ('Python', 'Python'),
        ('お金', 'お金'),
        ('ビジネス', 'ビジネス'),
        ('勉強', '勉強'),
        ('知識', '知識')
    )

    EVALUATION = (
        ('★☆☆☆☆', '★☆☆☆☆'),
        ('★★☆☆☆', '★★☆☆☆'),
        ('★★★☆☆', '★★★☆☆'),
        ('★★★★☆', '★★★★☆'),
        ('★★★★★', '★★★★★'),
        )

    title = models.CharField(max_length=100, verbose_name='タイトル')
    price = models.IntegerField(verbose_name='金額', blank=True, null=True)
    original_price = models.IntegerField(verbose_name='定価', blank=True, null=True)
    author = models.CharField(max_length=100, verbose_name='著者', blank=True, null=True)
    kind = models.CharField(max_length=100, choices=KIND, verbose_name='種別', blank=True, null=True)
    eval = models.CharField(max_length=100, choices=EVALUATION, verbose_name='評価', blank=True, null=True)
    review = models.TextField(max_length=400, verbose_name='レビュー', blank=True, null=True)
    def __str__(self):
        return self.title