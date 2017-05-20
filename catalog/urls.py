from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$', views.index, name='index'),
	url(r'^ksiazki/', views.BookListView.as_view(), name='books'),
	url(r'^ksiazka/(?P<pk>\d+)$', views.BookDetailView.as_view(),
		name='book-detail'),
	url(r'^ksiazka/(?P<pk>\d+)/szczegoly/$', views.BookFullDetailView.as_view(),
		name='book-detail-full'),
	url(r'^regaly/', views.RegalListView.as_view(), name='regals'),
	url(r'^regal/(?P<pk>\d+)$', views.RegalDetailView.as_view(),
		name='regal-detail'),
	url(r'^autorki/', views.AuthorListView.as_view(),
		name='authors'),
	url(r'^autor/(?P<pk>\d+)$', views.AuthorDetailView.as_view(),
		name='author-detail'),

	url(r'^ksiazka/nowa/$', views.BookCreate.as_view(), name='book-create'),
	url(r'^ksiazka/(?P<pk>\d+)/usun/$', views.BookDelete.as_view(),
		 name='book-delete'),
	url(r'^ksiazka/(?P<pk>\d+)/edytuj/$', views.BookUpdate.as_view(),
		name='book-update'),
	url(r'^autor/dodaj/$', views.author_create, name='author-create'),
	url(r'^autor/(?P<pk>\d+)/usun/$', views.AuthorDelete.as_view(),
	 	name='author-delete'),
	url(r'^szukaj/', views.BookSearchListView.as_view(), name='search-list-view'),
	#url(r'^ksiazka/nowa/autor-dodaj/$', views.AuthorCreate.as_view(), name='author-create'),

	url(r'^pop/', views.pop, name='pop'),
	url(r'^catpop/', views.catpop, name='catpop'),

	]
