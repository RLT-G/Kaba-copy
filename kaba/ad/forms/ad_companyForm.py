from django.core.exceptions import ValidationError
from ad.models.ad_company.ad_company import ad_company_base
from django.forms import ModelForm, TextInput, Textarea, NumberInput, CheckboxInput, SelectMultiple
from django.forms import SelectDateWidget


class ad_company_baseForm(ModelForm):
    class Meta:
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            pass

        model = ad_company_base
        fields = ['name', 'priority', 'type', 'week_day', 'on_holiday', 'start_date', 'end_date', 'key_word',
                  'minus_word', 'forbidden_site', 'show_gender', 'show_age', 'regions', 'advanced_targeting',
                  'category_and_subcategory', 'target_actions', 'counter_n', 'weekly_budget', 'balance', 'gender_pr',
                  'age_pr', 'device_pr', 'os_pr', 'solvency_pr', 'link_to_ad', 'header_list', 'description_list',
                  'img_link', 'product_link']
        widgets = {
            'name': TextInput(attrs={'class': 'Name', 'placeholder': 'Название кампании'}),
            'priority': NumberInput(attrs={'class': 'Name', 'placeholder': 'Приоритетность кампании'}),
            'type': Textarea(attrs={'class': 'Name', 'placeholder': 'Тип и подтип кампании (Конверсия-трафик или товарная)', 'cols': 60, 'rows': 3}),

            'week_day': SelectMultiple(attrs={'class': 'Name'}),

            'on_holiday': CheckboxInput(attrs={'class': 'Name'}),
            'start_date': SelectDateWidget(attrs={'class': 'Name', 'placeholder': 'Дата начала кампании'}),
            'end_date': SelectDateWidget(attrs={'class': 'Name', 'placeholder': 'Дата завершения кампании'}),
            'key_word': Textarea(attrs={'class': 'Name', 'placeholder': 'Список ключевых фраз (Максимум 50)', 'cols': 60, 'rows': 3}),
            'minus_word': Textarea(attrs={'class': 'Name', 'placeholder': 'Список минус фраз (Максимум 50)', 'cols': 60, 'rows': 3}),
            'forbidden_site': Textarea(attrs={'class': 'Name', 'placeholder': 'Список запрещенных для показа сайтов (url адреса через пробел)', 'cols': 60, 'rows': 3}),

            'show_gender': SelectMultiple(attrs={'class': 'Name'}),
            'show_age': SelectMultiple(attrs={'class': 'Name'}),

            'regions': SelectMultiple(attrs={'class': 'Name'}),

            'advanced_targeting': CheckboxInput(attrs={'class': 'Name', 'placeholder': 'Расширенный географический таргетинг'}),
            'category_and_subcategory': Textarea(attrs={'class': 'Name', 'placeholder': 'Список категорий и подкатегорий', 'cols': 60, 'rows': 3}),
            'target_actions': Textarea(attrs={'class': 'Name', 'placeholder': 'список Целевых действий [текст названия целевого действия, текст типа цены, число предельной цены]', 'cols': 60, 'rows': 3}),
            'counter_n': TextInput(attrs={'class': 'Name', 'placeholder': 'Номер подключенного счетчика'}),
            'weekly_budget': NumberInput(attrs={'class': 'Name', 'placeholder': 'Число недельного бюджета'}),
            'balance': NumberInput(attrs={'class': 'Name', 'placeholder': 'Число денег на балансе'}),

            'gender_pr': SelectMultiple(attrs={'class': 'Name'}),
            'age_pr': SelectMultiple(attrs={'class': 'Name'}),
            'device_pr': SelectMultiple(attrs={'class': 'Name'}),
            'os_pr': SelectMultiple(attrs={'class': 'Name'}),
            'solvency_pr': SelectMultiple(attrs={'class': 'Name'}),

            'link_to_ad': TextInput(attrs={'class': 'Name', 'placeholder': 'Ссылка на сайт рекламодателя'}),
            'header_list': Textarea(attrs={'class': 'Name', 'placeholder': 'Список вариантов заголовков', 'cols': 60, 'rows': 3}),
            'description_list': Textarea(attrs={'class': 'Name', 'placeholder': 'Список вариантов описаний', 'cols': 60, 'rows': 3}),
            'img_link': Textarea(attrs={'class': 'Name', 'placeholder': 'Список вариантов изображений (url через пробел)', 'cols': 60, 'rows': 3}),
            'product_link': Textarea(attrs={'class': 'Name', 'placeholder': 'Список ссылок на товар (url через пробел)', 'cols': 60, 'rows': 3}),
        }

    def clean_name(self):
        value = self.cleaned_data['name']
        if len(str(value)) > 255:
            raise ValidationError('Длина превышает 255 символов')
        return value

    def clean_type(self):
        value = self.cleaned_data['type']
        if len(str(value)) > 255:
            raise ValidationError('Длина превышает 255 символов')
        return value

    def clean_key_word(self):
        value = self.cleaned_data['key_word']
        if len(str(value).split()) > 50:
            raise ValidationError('Количество ключевых фраз превышает 50')
        return value

    def clean_minus_word(self):
        value = self.cleaned_data['minus_word']
        if len(str(value).split()) > 50:
            raise ValidationError('Количество минус фраз превышает 50')
        return value

    def clean_forbidden_site(self):
        value = self.cleaned_data['forbidden_site']
        if len(str(value).split()) > 200:
            raise ValidationError('Количество запрещенных сайтов превышает 200')
        return value

    def clean_counter_n(self):
        value = self.cleaned_data['counter_n']
        if not str(value).isdigit():
            raise ValidationError('В номере счетчика присутствуют недопустимые символы')
        return value
