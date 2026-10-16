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