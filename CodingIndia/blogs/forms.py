from .models import AddBlog
from django.forms import ModelForm


class AddBlogForm(ModelForm):
    class Meta:
        model = AddBlog
        fields = "__all__"