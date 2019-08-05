from django.urls import path

from apps.snippets import views

app_name = "snippets"

urlpatterns = [

    path('snippet_list/', views.SnippetList.as_view()),
    path('snippet_detail/<int:pk>/', views.SnippetDetail.as_view()),

]
