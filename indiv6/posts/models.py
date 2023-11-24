from django.db import models


# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Сообщение')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Дата изменения')
    post_likes = models.IntegerField(default=0)
    status = (('r1', 'Роман'), ('p', 'Поэма'), ('s', 'Стихотворение'))
    status = models.CharField(max_length=2, choices=status, blank=True, default='r1')
    post_author = models.ForeignKey('Author', blank=True, null=True, verbose_name='Автор', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=120, verbose_name='Имя')
    second_name = models.CharField(max_length=120, verbose_name='Фамилия')
    email = models.EmailField(max_length=254, verbose_name='Почта')

    def __unicode__(self):
        return self.first_name + ' ' + self.second_name

    def __str__(self):
        return self.first_name + ' ' + self.second_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    comment_text = models.TextField(verbose_name='Комментарий')
    comment_article = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.comment_text

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'