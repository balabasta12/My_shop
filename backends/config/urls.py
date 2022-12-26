
from django.contrib import admin
from django.urls import path, include
from shop.views import CategoryView, PartnerUpdate, ShopView, ProductInfoView, OrderView, register, home
urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),

    path('home/', home, name='home'),

    # path('partner/update/', PartnerUpdate.as_view()),  # Загрузка yaml файла
    # path('categories/', CategoryView.as_view(), name='categories'),
    # path('shops/', ShopView.as_view(), name='shops'),
    # path('products/', ProductInfoView.as_view(), name='shops'),
    # path('order/', OrderView.as_view(), name='order'),
    # path('boostrap/', views.boostrap_page_handler, name='boostrap'),
]
