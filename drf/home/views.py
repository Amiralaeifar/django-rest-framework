from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person, Question, Answer
from .serializers import PersonSerializer, QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import status
from permissions import IsOwnerOrReadOnly
from django.core.paginator import Paginator



class Home(APIView):
    
    permission_classes = [AllowAny,]
    
    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(instance=persons, many=True)
        return Response(data=ser_data.data)


class QuestionListView(APIView):
    
    permission_classes = [IsAuthenticated,]
    
    def get(self, request):
        questions = Question.objects.all()
        page_number = self.request.query_params.get('page', 1)
        page_size = self.request.query_params.get('limit', 2)
        paginator = Paginator(questions, page_size)
        srz_data = QuestionSerializer(instance=paginator.page(page_number), many=True).data
        return Response(data=srz_data, status=status.HTTP_200_OK)

    
class QuestionCreateView(APIView):
    
    permission_classes = [IsAuthenticated,]
    
    def post(self, request):
        srz_data = QuestionSerializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class QuestionUpdateView(APIView):
    
    permission_classes = [IsOwnerOrReadOnly,]
    
    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        srz_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        self.check_object_permissions(request, question)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    
class QuestionDeleteView(APIView):
    
    permission_classes = [IsOwnerOrReadOnly,]
    
    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        question.delete()
        return Response({'message': 'deleted successfully'}, status=status.HTTP_200_OK)
    