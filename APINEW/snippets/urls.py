from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include


urlpatterns = [
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view(),name="snippets"),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(),name="snippet-detail"),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(),name="snippet-highlight"),
    path('authors/', views.AuthorList.as_view(),name="authors"),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(),name="author-detail"),
    path('users/', views.UserList.as_view(),name="users"),
    path('users/<int:pk>/', views.UserDetail.as_view(),name="user-detail"),

]


urlpatterns = format_suffix_patterns(urlpatterns)



urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]