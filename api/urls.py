from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'hero', views.HeroViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'experience', views.ExperienceViewSet)
router.register(r'certifications', views.CertificationViewSet)
router.register(r'contact', views.ContactViewSet)
router.register(r'messages', views.MessageViewSet)
router.register(r'blog', views.BlogPostViewSet)
router.register(r'activities', views.ExtraCurricularActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
