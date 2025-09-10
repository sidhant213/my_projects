from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .form import LoginForm,MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm
urlpatterns = [
    # path('', views.home),
    path('',views.ProductView.as_view(), name='home'),
    path('admin/', admin.site.urls),

    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),

    
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.show_cart, name='cart'),

    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('address/', views.address, name='address'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<str:data>/', views.mobile, name='mobiledata'),
    path('laptop/', views.mobile, {'data': 'laptop'}, name='laptop'),
    path('topwear/', views.mobile, {'data': 'topwear'}, name='topwear'),
    path('bottomwear/', views.mobile, {'data': 'bottomwear'}, name='bottomwear'),
    # path('customerregistration/', views.CustomerRegistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/',views.payment_done,name='paymentdone'),




    path('account/login/',auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'),name='passwordchange'),

    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),

    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('pluscart/', views.plus_cart, name='pluscart'),
    path('minuscart/', views.minus_cart, name='minuscart'),
    path('removecart/', views.remove_cart, name='removecart'),
   
    path('registration/',views.CustomerRegistrationView.as_view(),name='customerregistration'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
