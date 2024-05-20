from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from backend.serializers import ContactUsSerializer, NewsLetterSerializer

def send_mail_on_new_lead(subject: str, message: str):
    try:
        send_mail(
            subject,
            message,
            from_email=settings.FROM_MAIL_FOR_UPDATES,
            recipient_list=[settings.TO_MAIL_FOR_UPDATES],
            fail_silently=False,
        )
    except Exception as ex:
        print("Exception sending email:", ex)

class ContactUsAPI(APIView):
    serializer_class = ContactUsSerializer

    def post(self, request):
        serializer = ContactUsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        send_mail_on_new_lead("New lead arrived at www.reckonsys.com", repr(serializer.data))

        return Response({"status": "ok"}, status=status.HTTP_201_CREATED)

class NewsLetterAPI(APIView):
    serializer_class = NewsLetterSerializer

    def post(self, request):
        serializer = NewsLetterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status": "ok"}, status=status.HTTP_201_CREATED)