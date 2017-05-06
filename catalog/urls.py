from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$', views.index, name='index'),
	url(r'^ksiazki/', views.BookListView.as_view(), name='books'),
	url(r'^ksiazka/(?P<pk>\d+)$', views.BookDetailView.as_view(), 
		name='book-detail'),
	url(r'^autorki/', views.AuthorListView.as_view(),
		name='authors'),
	url(r'^autor/(?P<pk>\d+)$', views.AuthorDetailView.as_view(),
		name='author-detail'),	

	url(r'^ksiazka/nowa/$', views.BookCreate.as_view(), name='book-create'),
	url(r'^ksiazka/(?P<pk>\d+)/usun/$', views.BookDelete.as_view(),
		 name='book-delete'),
	url(r'^ksiazka/(?P<pk>\d+)/edytuj/$', views.BookUpdate.as_view(), 
		name='book-update'),
	]