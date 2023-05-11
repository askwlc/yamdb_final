import datetime as dt

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from reviews.validators import username_validation


class User(AbstractUser):
    """Переопределение полей стандартной модели User"""
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    username = models.CharField(
        unique=True,
        max_length=settings.USERNAME_MAX_LENGTH,
        validators=(username_validation,),
        verbose_name='Имя пользователя',
        help_text='Введите имя пользователя'
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Роль пользователя',
        choices=settings.ROLE_CHOICES,
        max_length=30, default=USER
    )
    email = models.EmailField(
        unique=True,
        verbose_name='Адрес электронной почты'
    )

    confirmation_code = models.CharField(
        max_length=settings.CONFIRMATION_CODE_MAX_LENGTH,
        blank=True
    )

    @property
    def is_moderator(self):
        """True для пользователей с правами модератора."""
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        """True для пользователей с правами админа и суперпользователей."""
        return (
            self.role == self.ADMIN
            or self.is_staff
            or self.is_superuser
        )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

    def __str__(self):
        return self.username


class Category(models.Model):
    """Модель категорий (типов) произведений."""
    name = models.CharField('Имя категории', max_length=256)
    slug = models.SlugField('Slug', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        default_related_name = 'categories'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Модель жанров произведений."""
    name = models.CharField('Имя жанра', max_length=256)
    slug = models.SlugField('Slug', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        default_related_name = 'genres'
        ordering = ('name',)

    def __str__(self):
        return self.slug


class Title(models.Model):
    """Модель произведений, к которым пишут отзывы."""
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL, blank=True, null=True
    )
    genre = models.ManyToManyField(Genre, blank=True, db_index=True)
    name = models.TextField('Название произведения', max_length=256)
    year = models.PositiveSmallIntegerField(
        'Год выпуска',
        validators=[MinValueValidator(
            limit_value=1,
            message='Год не может быть меньше или равен нулю'),
            MaxValueValidator(
                limit_value=dt.date.today().year,
                message='Год не может быть больше текущего года')])
    description = models.TextField(verbose_name='Описание', null=True,
                                   max_length=200, )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        default_related_name = 'titles'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Review(models.Model):
    """Модель отзывы и рейтинг"""
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    pub_date = models.DateTimeField(
        'Дата отзыва',
        auto_now_add=True,
        db_index=True
    )
    text = models.TextField()
    score = models.PositiveIntegerField(
        'Оценка',
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ],
    )

    class Meta:
        ordering = ['-pub_date']
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'], name='unique_review')
        ]


class Comment(models.Model):
    """Модель комментариев"""
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField(
        'Дата комментария',
        auto_now_add=True,
        db_index=True
    )
    text = models.TextField()

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        default_related_name = 'comments'
        ordering = ['-pub_date']

    def __str__(self):
        return str(self.author)
