from django.urls import path
from .views import BookCreate,BookList,BookUpdate,BookRetrieve,BookDelete
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns=[
    path('token-auth/',obtain_auth_token,name='api_token_auth'),
    path('create/',BookCreate.as_view(),name='bookcreate'),
    path('list/',BookList.as_view(),name='book_list'),
    path('bookupdate/<int:pk>/',BookUpdate.as_view(),name='update_book'),
    path('bookretrieve/<int:pk>/',BookRetrieve.as_view(),name='retrieve_book'),
    path('bookdelete/<int:pk>/',BookDelete.as_view(),name='delete_book'),
]
