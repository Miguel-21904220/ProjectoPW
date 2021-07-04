from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

app_name = 'teacher'

urlpatterns = [ 
    path('', views.home_pageIndex_view, name='index'),
    path('html', views.home_pageHTML_view, name='html'),
    path('htmlelements', views.home_pageHTMLElements_view, name='htmlelements'),
    path('htmlforms', views.home_pageHTMLForms_view, name='htmlforms'),
    path('htmltables', views.home_pageHTMLTables_view, name='htmltables'),
    path('htmlsemantic', views.home_pageHTMLSemantic_view, name='htmlsemantic'),
    path('css', views.home_pageCSS_view, name='css'),
    path('csssyntax', views.home_pageCSSSyntax_view, name='csssyntax'),
    path('about', views.home_pageAbout_view, name='about'),
    path('quiz', views.home_quiz_view, name='quiz'),
    path('contactos/', views.home_pageContact_view, name='homeContacto'),
    path('nova/', views.nova_contact_view, name='novaContacto'),
    path('edita/<int:contact_id>', views.edita_contact_view, name='editaContacto'),
    path('apaga/<int:contact_id>', views.apaga_contact_view, name='apagaContacto'),
    
    path('comments', views.home_comments_view, name='comments'),
    
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='teacher/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
