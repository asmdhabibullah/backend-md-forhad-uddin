from rest_framework.serializers import ModelSerializer

from main_api.models import (
    About, Skill, Education, Experience, Recommendation, Interested, Client, Article
)


class AboutSerializer(ModelSerializer):
    """ About serializer"""
    class Meta:
        model = About
        fields = ('__all__')


class SkillsSerializer(ModelSerializer):
    """ Skills serializer"""
    class Meta:
        model = Skill
        fields = ('__all__')


class EducationsSerializer(ModelSerializer):
    """ Educations serializer"""
    class Meta:
        model = Education
        fields = ('__all__')


class ExperienceSerializer(ModelSerializer):
    """ Experience serializer"""
    class Meta:
        model = Experience
        fields = ('__all__')


class RecommendationSerializer(ModelSerializer):
    """ Recommendation serializer"""
    class Meta:
        model = Recommendation
        fields = ('__all__')


class InterestedSerializer(ModelSerializer):
    """ Interested serializer"""
    class Meta:
        model = Interested
        fields = ('__all__')


class ClientsSerializer(ModelSerializer):
    """ Clients serializer"""
    class Meta:
        model = Client
        fields = ('__all__')


class ArticleSerializer(ModelSerializer):
    """ Article serializer"""
    class Meta:
        model = Article
        fields = ('__all__')
