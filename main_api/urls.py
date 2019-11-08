from django.urls import path
from rest_framework.routers import DefaultRouter
from main_api.views import (
    AboutViews, SkillsViews, EducationsViews, ExperienceViews, RecommendationViews, InterestedViews, ClientsViews, ArticleViews
)

router = DefaultRouter()

router.register('about', AboutViews, base_name='about')
router.register('skills', SkillsViews, base_name='skills')
router.register('educations', EducationsViews, base_name='educations')
router.register('experiences', ExperienceViews, base_name='experiences')
router.register('recommend', RecommendationViews, base_name='recomande')
router.register('interested', InterestedViews, base_name='interested')
router.register('clients', ClientsViews, base_name='clients')
router.register('article', ArticleViews, base_name='article')

urlpatterns = router.urls
