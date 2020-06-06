from django.conf.urls import url

from . import views

app_name = 'riddles'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]+)/$', views.detail, name='detail'),
    url(r'^([0-9]+)/answer/$', views.answer, name='answer'),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^password-change/', views.PasswordChangeView.as_view()),
    # отправка сообщения
    url(r'^([0-9]+)/post/$', views.post, name='post'),
    # отправка списка сообщений
    url(r'^([0-9]+)/msg_list/$', views.msg_list, name='msg_list'),
    # отправка оценки
    url(r'^([0-9]+)/post_mark/$', views.post_mark, name='post_mark'),
    # средняя оценка
    url(r'^([0-9]+)/get_mark/$', views.get_mark, name='get_mark'),
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^post_riddle/$', views.post_riddle, name='post_riddle'),
    url(r'^subscribe/$', views.SubscribeView.as_view()),
    url(r'^unsubscribe/$', views.unsubscribe, name='unsubscribe'),
]
