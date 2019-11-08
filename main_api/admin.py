from django.contrib import admin
from main_api.models import (
    About, Skill, Education, Experience, Recommendation, Client, Interested, Article
)

admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Recommendation)
admin.site.register(Interested)
admin.site.register(Client)
admin.site.register(Article)
