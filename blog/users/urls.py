#进行users 子应用的视图路由
from django.urls import path
from users.views import  RegisterView
from users.views import ImageCodeView
from users.views import SmsCodeView
from users.views import  LoginView
from users.views import  ForgetPasswordView
from users.views import LogoutView
from users.views import UserCenterView
from users.views import WriteBlogView
urlpatterns=[
    #path的第一个参数是；路由
    #第二个参数是视图函数名
    path('register/',RegisterView.as_view(),name='register'),
    # path('register/',RegisterView.as_view(),name='register'),

    #图片验证码路由
    #首页联系管理订阅订阅随笔- 53  文章- 0  评论- 7
    # django基类View.as_view()
    path('imagecode/',ImageCodeView.as_view(),name='imagecode'),
    #短信验证码
    path('smscode/',SmsCodeView.as_view(),name='smscode'),
    #登录路由
    path('login/',LoginView.as_view(),name='login'),
    #忘记密码路由
    path('forgetpassword/',ForgetPasswordView.as_view(),name='forgetpassword'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('center/',UserCenterView.as_view(),name='center'),
    #写博客路由
    path('writeblog',WriteBlogView.as_view(),name="writeblog")

]
