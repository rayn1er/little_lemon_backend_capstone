from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(),name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    # path('message/', views.msg),
    path('booking/', views.BookingView.as_view(),name='booking'),
    path('booking/<int:pk>', views.SingleBookingView.as_view()),
     path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
