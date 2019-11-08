from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

# Third party import
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

#  Local import
from main_api.models import (
    About, Skill, Education, Experience, Recommendation, Interested, Client, Article
)
from main_api.serializers import (
    AboutSerializer, SkillsSerializer, EducationsSerializer, ExperienceSerializer, RecommendationSerializer, InterestedSerializer, ClientsSerializer, ArticleSerializer
)


class AboutViews(ModelViewSet):

    # permission_classes = [IsAuthenticated]

    # def get(self, request, *args, **kwrgs):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    # qs = About.objects.all()
    # serializer = AboutSerializer(qs, many=True)
    # return Response(serializer.data)


class SkillsViews(ModelViewSet):

    # permission_classes = [IsAuthenticated]

    queryset = Skill.objects.all()
    serializer_class = SkillsSerializer


class EducationsViews(ModelViewSet):

    # permission_classes = [IsAuthenticated]

    queryset = Education.objects.all()
    serializer_class = EducationsSerializer


class ExperienceViews(ModelViewSet):

    # permission_classes = [IsAuthenticated]

    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class RecommendationViews(ModelViewSet):

    # permission_classes = [IsAuthenticated]

    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer


class InterestedViews(ModelViewSet):

    # permission_classes = [IsAuthenticated]

    queryset = Interested.objects.all()
    serializer_class = InterestedSerializer


class ClientsViews(ModelViewSet):

    # permission_classes = [IsAuthenticated]

    queryset = Client.objects.all()
    serializer_class = ClientsSerializer


class ArticleViews(ModelViewSet):

    # permission_classes = [IsAuthenticated]

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
