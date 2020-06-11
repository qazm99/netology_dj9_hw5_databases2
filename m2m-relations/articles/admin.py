from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Theming, Theme


class ThemingInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_theme_count = 0
        dict_id_theme = dict()
        list_error = []
        for form in self.forms:
            prepared_data = form.cleaned_data
            if not prepared_data.get('DELETE'):
                if prepared_data.get('is_main'):
                    main_theme_count += 1

                theme = prepared_data.get('theme')
                if theme:
                    if dict_id_theme.get(theme.id):
                        dict_id_theme[theme.id] += 1
                    else:
                        dict_id_theme[theme.id] = 1

        if main_theme_count == 0:
            list_error.append('Не установлена главная тема.')
        elif main_theme_count > 1:
            list_error.append('Основная тема может быть только одна.')

        for count_id_thme in dict_id_theme.values():
            if count_id_thme > 1:
                list_error.append('Темы не должны повторяться в одной статье.')
                break

        if len(list_error):
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            raise ValidationError(' '.join(list_error))
        return super().clean()


class ThemingInLine(admin.TabularInline):
    model = Theming
    formset = ThemingInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ThemingInLine]


@admin.register(Theme)
class ArticleAdmin(admin.ModelAdmin):
    pass
