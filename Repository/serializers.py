from rest_framework import serializers
from Repository.models import QuestionsDb
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','email','password']
        read_only_fields = ['id']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def create(self,validated_data):

        user = User.objects.create_user(**validated_data)
        return user



class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    language = serializers.ChoiceField(choices = QuestionsDb.LANGUAGE_CHOICES,default ="python")
    difficulty_level = serializers.ChoiceField(choices = QuestionsDb.DIFFICULTY_LEVELS,default ="easy")
    topic = serializers.CharField(max_length=200)
    notes =serializers.CharField(max_length=1000)
    sample_input = serializers.CharField(max_length=1000)
    sample_output = serializers.CharField(max_length=1000)
    published_date = serializers.DateTimeField(read_only=True)
    is_active = serializers.BooleanField(default=True)

class SubmissionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question_id = serializers.IntegerField()
    answer = serializers.CharField()
    points = serializers.IntegerField(required=False, allow_null=True)
    remarks = serializers.CharField(required=False, allow_null=True)
    submission_date = serializers.DateTimeField(read_only=True)

    def validate(self,validated_data):
        question_id = validated_data.get("question_id")
        if not QuestionsDb.objects.filter(id=question_id).exists():
            raise serializers.ValidationError("Question does not exist.....")
        return validated_data