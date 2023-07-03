from django.db import models
#from separatedvaluesfield.models import SeparatedValuesField
from ad.custom.fields import SeparatedValuesField


class ad_company_base(models.Model):
    # Раздел настройки рекламной кампании
    name = models.CharField('Название кампании', max_length=255)
    priority = models.IntegerField('Приоритетность кампании', blank=True, null=True)
    type = models.TextField('Тип и подтип кампании', max_length=255) # Переделать в выбор

    week_day = SeparatedValuesField(
        max_length=150,
        blank=True,
        null=True,
        token=',',
        choices=(
            ('ПН', 'Понедельник'),
            ('ВТ', 'Вторник'),
            ('СР', 'Среда'),
            ('ЧТ', 'Четверг'),
            ('ПТ', 'Пятница'),
            ('СБ', 'Суббота'),
            ('ВС', 'Воскресение')
        )
    )

    on_holiday = models.BooleanField('Показывать в праздничные дни', default=True)
    start_date = models.DateTimeField('Дата начала кампании')
    end_date = models.DateTimeField('Дата завершения кампании', blank=True, null=True)
    key_word = models.TextField('Список ключевых фраз', max_length=32_768, blank=True, null=True)
    minus_word = models.TextField('Список минус фраз', max_length=32_768, blank=True, null=True)
    forbidden_site = models.TextField('Список запрещенных для показа сайтов (url адреса через пробел)', max_length=32_768, blank=True, null=True)

    show_gender = SeparatedValuesField(
        max_length=150,
        blank=True,
        null=True,
        token=',',
        choices=(
            ('М', 'Мужской'),
            ('Ж', 'Женский'),
            ('Л', 'Любой'),
        )
    )
    show_age = SeparatedValuesField(
        max_length=150,
        blank=True,
        null=True,
        token=',',
        choices=(
            ('1', 'Младше 18'),
            ('2', '18 - 24'),
            ('3', '25 - 34'),
            ('4', '35 - 44'),
            ('5', '45 - 54'),
            ('6', 'Старше 54'),
        )
    )
    regions = SeparatedValuesField(
        max_length=150,
        blank=True,
        null=True,
        token=',',
        choices=(
            ("01", "Республика Адыгея (Адыгея)"), ("02", "Республика Башкортостан"), ("03", "Республика Бурятия"),
            ("04", "Республика Алтай"), ("05", "Республика Дагестан"), ("06", "Республика Ингушетия"),
            ("07", "Кабардино-Балкарская Республика"), ("08", "Республика Калмыкия"), ("09", "Карачаево-Черкесская Республика"),
            ("10", "Республика Карелия"), ("11", "Республика Коми"), ("12", "Республика Марий Эл"),
            ("13", "Республика Мордовия"), ("14", "Республика Саха (Якутия)"), ("15", "Республика Северная Осетия - Алания"),
            ("16", "Республика Татарстан (Татарстан)"), ("17", "Республика Тыва"), ("18", "Удмуртская Республика"),
            ("19", "Республика Хакасия"), ("20", "Чеченская Республика"), ("21", "Чувашская Республика - Чувашия"),
            ("22", "Алтайский край"), ("23", "Краснодарский край"), ("24", "Красноярский край"), ("25", "Приморский край"),
            ("26", "Ставропольский край"), ("27", "Хабаровский край"), ("28", "Амурская область"),
            ("29", "Архангельская область"), ("30", "Астраханская область"), ("31", "Белгородская область"),
            ("32", "Брянская область"), ("33", "Владимирская область"), ("34", "Волгоградская область"),
            ("35", "Вологодская область"), ("36", "Воронежская область"), ("37", "Ивановская область"),
            ("38", "Иркутская область"), ("39", "Калининградская область"), ("40", "Калужская область"),
            ("41", "Камчатский край"), ("42", "Кемеровская область - Кузбасс"), ("43", "Кировская область"),
            ("44", "Костромская область"), ("45", "Курганская область"), ("46", "Курская область"),
            ("47", "Ленинградская область"), ("48", "Липецкая область"), ("49", "Магаданская область"),
            ("50", "Московская область"), ("51", "Мурманская область"), ("52", "Нижегородская область"),
            ("53", "Новгородская область"), ("54", "Новосибирская область"), ("55", "Омская область"),
            ("56", "Оренбургская область"), ("57", "Орловская область"), ("58", "Пензенская область"),
            ("59", "Пермский край"), ("60", "Псковская область"), ("61", "Ростовская область"),
            ("62", "Рязанская область"), ("63", "Самарская область"), ("64", "Саратовская область"),
            ("65", "Сахалинская область"), ("66", "Свердловская область"), ("67", "Смоленская область"),
            ("68", "Тамбовская область"), ("69", "Тверская область"), ("70", "Томская область"),
            ("71", "Тульская область"), ("72", "Тюменская область"), ("73", "Ульяновская область"),
            ("74", "Челябинская область"), ("75", "Забайкальский край"), ("76", "Ярославская область"),
            ("77", "город федерального значения Москва"), ("78", "город федерального значения Санкт-Петербург"),
            ("79", "Еврейская автономная область"), ("83", "Ненецкий автономный округ"),
            ("86", "Ханты-Мансийский автономный округ - Югра"), ("87", "Чукотский автономный округ"),
            ("89", "Ямало-Ненецкий автономный округ"), ("90", "Запорожская область"), ("91", "Республика Крым"),
            ("92", "город федерального значения Севастополь"), ("93", "Донецкая Народная Республика"),
            ("94", "Луганская Народная Республика"), ("95", "Херсонская область"),
            ("99", "Иные территории, включая город и космодром Байконур")
        )
    )

    advanced_targeting = models.BooleanField('Расширенный географический таргетинг', default=True)
    category_and_subcategory = models.TextField('Список категорий и подкатегорий', max_length=32_768, default='')# ?
    target_actions = models.TextField('Список целевых действий', max_length=32_768, default='')# ?
    counter_n = models.CharField('Номер подключенного счетчика', max_length=255, blank=True, null=True)
    weekly_budget = models.IntegerField('Число недельного бюджета')
    balance = models.IntegerField('Число денег на балансе', default=0)

    gender_pr = SeparatedValuesField(
        max_length=150,
        blank=True,
        null=True,
        token=',',
        choices=(
            ('М', 'Мужской'),
            ('Ж', 'Женский'),
            ('Л', 'Любой'),
        )
    )
    age_pr = SeparatedValuesField(
        max_length=150,
        blank=True,
        null=True,
        token=',',
        choices=(
            ('1', 'Младше 18'),
            ('2', '18 - 24'),
            ('3', '25 - 34'),
            ('4', '35 - 44'),
            ('5', '45 - 54'),
            ('6', 'Старше 54'),
        )
    )
    device_pr = SeparatedValuesField(
        max_length=150,
        blank=True,
        null=True,
        token=',',
        choices=(
            ('Desktop', 'Десктопы'),
            ('Smartphone', 'Смартфоны'),
            ('Tablet', 'Планшеты'),
        )
    )
    os_pr = SeparatedValuesField(
        max_length=150,
        blank=True,
        null=True,
        token=',',
        choices=(
            ('1', 'Android'),
            ('2', 'CentOS'),
            ('3', 'Chrome OS'),
            ('4', 'Free BSD'),
            ('5', 'iOS'),
            ('6', 'Windows'),
            ('7', 'macOS'),
            ('8', 'Solaris'),
            ('9', 'Ubuntu'),
            ('10', 'Linux'),
        )
    )
    solvency_pr = SeparatedValuesField(
        max_length=150,
        blank=True,
        null=True,
        token=',',
        choices=(
            ('1', '1%'),
            ('2', '2 - 5%'),
            ('3', '6 - 10%'),
        )
    )

    # Раздел Баннер
    link_to_ad = models.CharField('Ссылка на сайт рекламодателя', max_length=255)
    header_list = models.TextField('Список вариантов заголовков', max_length=32_768, blank=True, null=True)
    description_list = models.TextField('Список вариантов описаний', max_length=32_768, blank=True, null=True)
    img_link = models.TextField('Список вариантов изображений (url через пробел)', max_length=32_768, blank=True, null=True)
    product_link = models.TextField('Список ссылок на товар (url через пробел)', max_length=32_768, blank=True, null=True) # list

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рекламная кампания'
        verbose_name_plural = 'Рекламные кампании'


class ad_company_Product(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рекламная кампания (Товарная)'
        verbose_name_plural = 'Рекламные кампании (Товарная)'


class ad_company_Traffic(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рекламная кампания (Трафик)'
        verbose_name_plural = 'Рекламные кампании (Трафик)'