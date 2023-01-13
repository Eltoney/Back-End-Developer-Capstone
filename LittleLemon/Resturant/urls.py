from django.urls import path
from . import views
app_name = 'Resturant'
urlpatterns = [
    # path('', views.index, name='index'),
    path('menu-items/', views.MenuItemView.as_view(), name='all_items'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view())
]
