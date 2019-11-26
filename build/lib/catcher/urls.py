from django.urls import path
from .views import MessageView

app_name = "catcher"
urlpatterns = [
    path('catcher/', MessageView.as_view()),
]