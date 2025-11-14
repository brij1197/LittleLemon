from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register(r'tables', viewset=views.BookingViewSet,basename='booking')

urlpatterns = [
    path('',views.home,name='home'),
    path('menu/', views.MenuItemView.as_view(),name="menu"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
]