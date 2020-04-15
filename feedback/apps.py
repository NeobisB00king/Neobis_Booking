from django.apps import AppConfig


class FeedbackConfig(AppConfig):
    name = 'feedback'
    verbose_name = 'Бронирование'

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
