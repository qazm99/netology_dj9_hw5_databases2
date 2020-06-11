from django.db import models


class Theme(models.Model):
    name = models.CharField(max_length=256, verbose_name='Тема')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return f'{self.name}'

    # def __repr__(self):
    #     return (self.pk, self.name)


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    thems = models.ManyToManyField(Theme, through='Theming', related_name='articles', related_query_name='scopes')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'{self.title}'


class Theming(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, verbose_name='Тема')
    is_main = models.BooleanField(verbose_name='Основная тема')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематика'

    def __str__(self):
        return f'{self.article.__str__()[:40]}...:{self.theme}'
