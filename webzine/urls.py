# webzine > urls.py

from unicodedata import name
from django.urls import path
from .views import * # webzine>views의 모든 함수를 가져옴.
from django.conf import settings
from django.conf.urls.static import static

app_name = "webzine"
urlpatterns = [
    path('webzine', webzine, name='webzine'),
    path('question_list', question_list, name='question_list'),
    path('<int:question_id>', question_detail, name="question_detail"),
    path('question_create', question_create, name="question_create"),
    path('answer/create/<int:question_id>', answer_create, name="answer_create"),
    path('webzine_upload/', webzine_upload, name='webzine_upload'),
    # path('webzine/', upload_create, name="upload_create"),
] 

# 업로드 구현을 해야하고 
# 
'''
업로드 구현해야하고 이미지가 여러개가 묶여있으니까 그거 다 불러와야하고 for문
안에 어떻게 꾸며질지 구상해야함.
'''