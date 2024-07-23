from django.urls import path
from.views import*
from rest_framework.authtoken import views


urlpatterns =[
    # path('basic/auth',ClassBasedView.as_view()),
    path('sample/create/',SampleViews.as_view()),
    path('sample/get/all/',SampleViews.as_view()),
    path('sample/get/<str:id>/',SampleEdit.as_view()),
    path('sample/update/<str:id>/',SampleEdit.as_view()),
    path('sample/delete/<str:id>/',SampleEdit.as_view()),


    path('api-token-auth/',views.obtain_auth_token),
    path('register/token/',RegisterToken.as_view()),
    path('login/',LoginUser.as_view()),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('logout/', Logout.as_view()),
    # path('register/jwttoken/',RegisterBearerToken.as_view()),
]