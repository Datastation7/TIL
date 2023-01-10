from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # 1. 유효성 검사 (Validation)
    # 2. HTML 안에 <input> 태그 만들기 번거러움
    # 3. 저장할 때 request.POST 에서 하나하나 꺼내기 번거러움

    title = forms.CharField(min_length=2, max_length=100)

    class Meta:
        model = Article
        fields = ("title", "content", )
