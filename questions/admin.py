from django.contrib import admin
from .models import Question
from .models import Answer
from .models import Tag
from .models import Profile
from .models import Like


admin.site.register(Tag)
admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Like)