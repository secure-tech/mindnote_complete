from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexRedirect.as_view(),name='index'),
    path('diary/',views.PostListView.as_view(),name='page-list'),
    path('diary/info/',views.InfoTemplateView.as_view(),name='info'),
    path('diary/write',views.PageCreateView.as_view(),name='page-create'),
    path('diary/page/<int:pk>/',views.PageDetailView.as_view(),name='page-detail'),
    path('diary/page/<int:pk>/edit/',views.PageUpdateView.as_view(),name='page-update'),
    path('diary/page/<int:pk>/delete/',views.PageDeleteView.as_view(),name='page-delete'),
]