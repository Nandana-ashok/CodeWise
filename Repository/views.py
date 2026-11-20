from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from Repository.models import QuestionsDb,SubmissionsDb
from Repository.serializers import RegistrationSerializer,QuestionSerializer,SubmissionSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RegistrationView(APIView):
    def post(self,request):

        serializer_instance = RegistrationSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"Message":"Registration Successfull...."})
        return Response({"errors":serializer_instance.errors})
    
    def get(self,request):

        qs = User.objects.all()
        serializer_instance = RegistrationSerializer(qs,many=True)
        return Response(data=serializer_instance.data)


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


class SubmissionCreateListView(APIView):

    permission_classes = [IsAuthenticated]
    
    def get(self,request):

        qs = SubmissionsDb.objects.filter(owner=request.user)

        submission_instance = SubmissionSerializer(qs,many=True)

        return Response(data=submission_instance.data)
  
    def post(self,request):

        form_data = request.data

        submission_instance = SubmissionSerializer(data=form_data)

        if submission_instance.is_valid():

            actual_data = submission_instance.validated_data
            SubmissionsDb.objects.create(**actual_data,owner=request.user)
            return Response({"Message":"Answer added successfully...."})
        else:
            return Response(data={'errors':submission_instance.errors})


class SubmissionRetrieveUpdateDeleteView(APIView):

    permission_classes = [IsAuthenticated]
    
    def get(self,request,qid):
       
        # qs = SubmissionsDb.objects.get(id=qid)

        qs = get_object_or_404(SubmissionsDb,id=qid,owner=request.user)

        submission_instance = SubmissionSerializer(qs)

        return Response(data=submission_instance.data)

    def put(self,request,qid):

        submission = get_object_or_404(SubmissionsDb,id=qid,owner=request.user)
        

        form_data = request.data

        submission_instance = SubmissionSerializer(data=form_data)

        if submission_instance.is_valid():

            actual_data = submission_instance.validated_data
            SubmissionsDb.objects.filter(id=qid,owner=request.user).update(**actual_data)
            return Response({"Message":"Answer updated successfully...."})
        else:
            return Response(data = submission_instance.errors)
    
    def delete(self,request,qid):

        submission = get_object_or_404(SubmissionsDb,id=qid,owner=request.user)
        submission.delete()
        return Response({"Message":"Submission deleted successfully..."})


class EvaluateSubmissionView(APIView):
    def put(self,request,qid):

        form_data = request.data

        SubmissionsDb.objects.filter(id=qid).update(**form_data)

        return Response(data={
            "Message":"Updated....!"
        })



    