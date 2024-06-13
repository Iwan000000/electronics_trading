from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    # Сохраняйте поле имени пользователя так, как того требует встроенная система аутентификации Django
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True, verbose_name='почта')
    first_name = models.CharField(max_length=20, verbose_name='имя', **NULLABLE)
    last_name = models.CharField(max_length=30, verbose_name='фамилия', **NULLABLE)

    # Установите для поля USERNAME_FIELD значение «электронная почта».
    USERNAME_FIELD = 'email'
    # Укажите поля, которые будут запрашиваться при создании суперпользователя
    REQUIRED_FIELDS = ['username']

    # Определите уникальное связанное_имя для групп и user_permissions.
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text=(
            'Группы, к которым принадлежит этот пользователь. Пользователь получит все разрешения '
            'предоставлено каждой из их групп.'
        ),
        related_name='custom_user_set',  # Уникальное связанное_имя для вашей пользовательской модели пользователя
        related_query_name='custom_user',
        # Уникальное связанное_имя_запроса для вашей пользовательской модели пользователя.
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',  # Уникальное связанное_имя для вашей пользовательской модели пользователя.
        related_query_name='custom_user',
        # Уникальное связанное_имя_запроса для вашей пользовательской модели пользователя.
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
