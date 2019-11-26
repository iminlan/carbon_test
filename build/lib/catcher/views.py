from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from .serializers import MessageSerializer
from .models import Message


class MessageView(APIView):
    def get(self, request):
        message = Message.objects.all()
        serializer = MessageSerializer(message, many=True)
        return Response({"message": serializer.data})

    def post(self, request):
        message = request.data.get('message')
        serializer = MessageSerializer(data=message)
        if serializer.is_valid(raise_exception=True):
            message_saved = serializer.save()
        return Response({"success": "Message '{}' created successfully".format(message_saved.name)})


def table(request):
    messages = Message.objects.all()
    lm = len(messages)
    messages = messages[(lm-100):lm]
    return render(request, 'cpu_load_table.html', {'object_list': messages})
