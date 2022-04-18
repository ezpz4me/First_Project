from django.urls import path
from .views import signupviews

urlpatterns = [
    path('registration/',signupviews.as_view()),
    path('registration/<int:id>',signupviews.as_view())
]
