from rest_framework import serializers
from .models import Question, Answer
from .custom_serializer_relation import UserEmailAndNameRelationalField


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    married = serializers.BooleanField()
    
    
class QuestionSerializer(serializers.ModelSerializer):
    
    answers = serializers.SerializerMethodField()
    user = UserEmailAndNameRelationalField(read_only=True)
    
    class Meta:
        model = Question
        fields = '__all__'
        
    def get_answers(self, obj):
        results = obj.answers.all()
        return AnswerSerializer(instance=results, many=True).data
        
        
class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Answer
        fields = '__all__'