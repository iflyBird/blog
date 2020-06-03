from django.urls import path
from home.views import IndexView
from home.views import DetailVIew
urlpatterns=[
    #首页的路由
    #默认根目录，不加路由的话
    path('',IndexView.as_view(),name='index'),
    #详情视图的路由
    path('detail/',DetailVIew.as_view(),name='detail')


]