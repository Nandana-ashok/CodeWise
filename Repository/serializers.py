from rest_framework import serializers
from Repository.models import QuestionsDb

class QuestionSerializer(serializers.Serializer):
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

    question_id = serializers.IntegerField()
    answer = serializers.CharField()
    points = serializers.IntegerField(required=False, allow_null=True)
    owner = serializers.CharField()
    remarks = serializers.CharField(required=False, allow_null=True)
    submission_date = serializers.DateTimeField(read_only=True)

    def validate(self,validated_data):
        question_id = validated_data.get("question_id")
        if not QuestionsDb.objects.filter(id=question_id).exists():
            raise serializers.ValidationError("Question does not exist.....")
        return validated_data