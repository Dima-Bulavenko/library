from django.urls import path, include
from rest_framework import routers
# from rest_view import views  # мой код с прошлого проекта тут rest_view апка
router = routers.SimpleRouter()

# router.register(r'rest-view', views.ViewSetAPIView)
#
# urlpatterns = [
#     path('', include(router.urls)),
#     path('function/', views.view_function, name='function_view'),
#     path('class/', views.ClassAPIView.as_view(), name='class_view'),
#     path('create/', views.MyCreateAPIView.as_view(), name='create'),
#     path('retrieve/<int:pk>', views.MyRetrieveAPIView.as_view(), name='retrieve'),
#     path('retrieve-update/<int:pk>', views.MyRetrieveUpdateAPIView.as_view(), name='retrieve_update'),
#     path('api-login', views.user_login),
#     path('create-user', views.CreateUser.as_view())
# ]