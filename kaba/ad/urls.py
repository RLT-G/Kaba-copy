from django.urls import path

# главная
# from ad.views.index import index
from ad.views.ad_views import *


urlpatterns = [

    # главная
    # path('index/', index.indexDef, name='ad_indexDef'),

    # добавление в бд
    path('create/', create, name='create'),
    # главная для ad
    path('', index, name='index')
    # # учить по карточкам
    # path('card&<str:action>&<int:term_pk>/', card.cardDef, name='ad_cardDef'),
    # # создаст сессию со списком pk терминов для изучения
    # path('card&<str:term_topic>&<str:mode>/', card.card_session_term_listDef, name='ad_card_session_term_listDef'),
]
