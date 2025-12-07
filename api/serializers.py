from rest_framework import serializers
from .models import Hero, Skill, Project, Experience, Certification, Contact, Message, BlogPost, ExtraCurricularActivity


class HeroSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False, allow_null=True)
    video_url = serializers.FileField(required=False, allow_null=True)
    resume_url = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = Hero
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False, allow_null=True)
    video_url = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = Project
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class CertificationSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Certification
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('created_at',)


class BlogPostSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = BlogPost
        fields = '__all__'


class ExtraCurricularActivitySerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = ExtraCurricularActivity
        fields = '__all__'
