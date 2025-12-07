from django.contrib import admin
from .models import Hero, Skill, Project, Experience, Certification, Contact, Message, BlogPost, ExtraCurricularActivity


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline', 'created_at')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'order')
    list_filter = ('category',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'featured', 'order', 'created_at')
    list_filter = ('category', 'featured')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_date', 'end_date', 'current')
    list_filter = ('current',)


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuer', 'category', 'issue_date', 'expiry_date')
    list_filter = ('category',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'location', 'availability')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'read', 'created_at')
    list_filter = ('read', 'created_at')
    readonly_fields = ('created_at',)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published', 'created_at')
    list_filter = ('published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ExtraCurricularActivity)
class ExtraCurricularActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'role', 'start_date', 'end_date', 'current', 'order')
    list_filter = ('current', 'organization')
    ordering = ('order', '-start_date')
