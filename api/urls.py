from django.urls import include, path


urlpatterns = [
    path('users/', include('users.urls')),
    path('address_book/', include('address_book.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
