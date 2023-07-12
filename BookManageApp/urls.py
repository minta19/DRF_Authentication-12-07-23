from django.urls import path
from .views import BookCreate,BookList,BookEdit
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns=[
    path('token-auth/',obtain_auth_token,name='api_token_auth'),
    path('create/',BookCreate.as_view(),name='bookcreate'),
    path('list/',BookList.as_view(),name='book_list'),
    path('details/<int:pk>/',BookEdit.as_view(),name='edit_book')
]