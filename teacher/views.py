from django.http import HttpResponseRedirect
from django.core.mail import message, send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .models import Comment, Formulario
from .forms import FormularioForm, QuizForm, UserRegistraitonForm, CommentForm

# Create your views here.

def register(request):
    if(request.method == 'POST'):
        form = UserRegistraitonForm(request.POST)
        if(form.is_valid()):
            form.save()
            messages.success(request, f'Conta criada.')
            render(request, 'teacher/register.html', context)
    else:
        form = UserRegistraitonForm()
        
    context = {'form': form}
    return render(request, 'teacher/register.html', context)

def home_pageIndex_view(request):
    return render(request, "teacher/index.html")

def home_pageHTML_view(request):
    return render(request, "teacher/html.html")

def home_pageHTMLElements_view(request):
    return render(request, "teacher/htmlelements.html")

def home_pageHTMLForms_view(request):
    return render(request, "teacher/htmlforms.html")

def home_pageHTMLTables_view(request):
    return render(request, "teacher/htmltables.html")

def home_pageHTMLSemantic_view(request):
    return render(request, "teacher/htmlsemantic.html")

def home_pageCSS_view(request):
    return render(request, "teacher/css.html")

def home_pageCSSSyntax_view(request):
    return render(request, "teacher/csssyxntaxandselectors.html")

def home_pageAbout_view(request):
    return render(request, "teacher/about.html")

@login_required
def home_quiz_view(request):
    
    answers = {
        'answer1' : 'Cascading Style Sheets',
        'answer2' : 'Standard Generalized Markup Language marked the beginning of style sheets in 1980s.',
        'answer3' : 'It is a pre-planned libraries, which allows easier and more standards-compliant webpage styling, using CSS language.',
        'answer4' : 'HyperText Markup Language',
        'answer5' : 'No, there are single HTML tags that do not need a closing tag.',
        'answer6' : 'To insert the copyright symbol, you need to type &copy; or & #169; in an HTML file.',
        'answer7' : 'The Inline style in a CSS is used to add up styling to individual HTML elements.',
        'answer8' : 'World Wide Web Consortium maintains the CSS specifications.',
        'answer9' : 'By using indents.',
        'answer10' : 'No.',
    }
    
    form = QuizForm(request.POST or None)
    
    if form.is_valid():
        form.created_by = request.user
        
        points = 0
        
        for question in answers:
            if(request.POST[question] == answers[question]):
                points += 2
                
        form.save()
        
        context = {'points': points, 'user': form.created_by, 'form':form}
        
        return render(request, 'teacher/quiz.html', context)

    context = {'form': form}
    return render(request, 'teacher/quiz.html', context)


# Comments
def home_comments_view(request):
    
    form = CommentForm(request.POST or None)
     
    if form.is_valid():
        #comment = Comment(name=request.user, comment=request.POST['comment'])
        #comment.save()
        
        form.save()
    

    context = {'form': form, 'comentario': Comment.objects.all()}
    return render(request, "teacher/comments.html", context)

# Formulario Pages
@login_required
def home_pageContact_view(request):
    context = {'contacts': Formulario.objects.all()}
    return render(request, "teacher/homeContacto.html", context)

def nova_contact_view(request):
    form = FormularioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('teacher:homeContacto'))

    context = {'form': form}

    return render(request, 'teacher/novaContacto.html', context)

def edita_contact_view(request, contact_id):
    contact = Formulario.objects.get(id=contact_id)
    form = FormularioForm(request.POST or None, instance=contact)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('teacher:homeContacto'))

    context = {'form': form, 'contact_id': contact_id}
    return render(request, 'teacher/editaContacto.html', context)

def apaga_contact_view(request, contact_id):
    Formulario.objects.get(id=contact_id).delete()
    return HttpResponseRedirect(reverse('teacher:homeContacto'))