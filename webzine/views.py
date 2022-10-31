from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from .models import Answer, Question, Photo, WebzineContents
from .forms import QuestionForm
from django.core.paginator import Paginator

# from django.views import generic
# Create your views here.
def webzine(request):
    return render(request, 'webzine/webzine.html')

def question_list(request):
    # q = Question.objects.all()
    questions = Question.objects.order_by('-create_date')
    # Paging 기능 구현하기
    page = request.GET.get('page', '1')
    paginator = Paginator(questions, 5)
    page_obj = paginator.get_page(page)
    context = {'question_list' : page_obj}
    return render(request, 'webzine/question_list.html', context)

def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'a_question' : question }
    return render(request, 'webzine/question_detail.html', context)

# class ListView(generic.ListView):
#     def get_queryset(self):
#         return Question.objects.order_by('-create_date')

# class DetailView(generic.DetailView):
#     model = Question

def question_create(request):
    if request.method == 'POST':
        a_form = QuestionForm(request.POST)
        if a_form.is_valid():
            question = a_form.save(commit=False)
            question.save()
            return redirect('webzine:question_list')
    else:
        a_form = QuestionForm()
    context = {'form' : a_form}
    return render(request, 'webzine/question_form.html', context)

def answer_create(request, question_id):
    a_question = get_object_or_404(Question, pk=question_id)
    a_content = request.POST.get('content')
    Answer.objects.create(question = a_question, content=a_content)
    return redirect('webzine:question_detail', question_id=a_question.id)

def webzine_upload(request):
    return render(request, 'webzine:webzine_upload.html')

def upload_create(request):
    form = WebzineContents()
    form.title = request.POST['title']
    try:
        form.image = request.FILES['image']
    except:
        pass
    form.save()
    return redirect('/')