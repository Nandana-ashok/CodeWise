from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Repository.models import QuestionsDb
from Repository.serializers import QuestionSerializer
# Create your views here.

class QuestionListCreateView(APIView):
    def get(self,request):

        qs = QuestionsDb.objects.all().values()

        serializer_instance = QuestionSerializer(qs,many=True)

        return Response(data = serializer_instance.data)

    def post(self,request):

        form_data = request.data

        serializer_instance = QuestionSerializer(data=form_data)

        if serializer_instance.is_valid():

            actual_data = serializer_instance.validated_data
            QuestionsDb.objects.create(**actual_data)
            return Response(data={'Message':"Question added successfully... "})
        
        else :
            return Response(data={'errors':serializer_instance.errors})
class RetrievalUpdateDeleteView(APIView):
    def get(self,request,qid):

        qs = QuestionsDb.objects.get(id=qid)

        serializer_instance = QuestionSerializer(qs)

        return Response(data =serializer_instance.data)
    def put(self,request,qid):

        form_data = request.data

        serializer_instance = QuestionSerializer(data=form_data)

        if serializer_instance.is_valid():

            actual_data = serializer_instance.validated_data

            qs = QuestionsDb.objects.filter(id=qid).update(**actual_data)

            return Response(data = serializer_instance.data)
        else:
            return Response(data = serializer_instance.errors)
    def delete(Self,request,qid):

        QuestionsDb.objects.filter(id=qid).delete()
        return Response({
            "Message":'Question deleted successfully.....'
        })
       