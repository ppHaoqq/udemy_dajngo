from django.urls import path
from .views import BookList, BookDetail, BookCreate, BookDelete, BookUpdate


urlpatterns = [
    path('list/', BookList.as_view(), name='list'),
    path('detail/<int:pk>', BookDetail.as_view(), name='detail'),
    path('create/', BookCreate.as_view(), name='create'),
    path('delete/<int:pk>', BookDelete.as_view(), name='delete'),
    path('update/<int:pk>', BookUpdate.as_view(), name='update')
]
