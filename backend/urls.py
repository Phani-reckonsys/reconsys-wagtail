from django.urls import path
from backend.apis import ContactUsAPI, NewsLetterAPI



urlpatterns = [
    path("contact-us", ContactUsAPI.as_view(), name="contact_us_form"),
    path("news-letter", NewsLetterAPI.as_view(), name="join_news_letter"),
]