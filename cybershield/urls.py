from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views

# Import the urls module from the accounts app
from accounts import urls as accounts_urls

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('accounts/', include(accounts_urls)),
    path('articles/', include('articles.urls')),  # Include URLs from the 'articles' app
    path('about/', views.about),   # About page URL
    path('', article_views.article_list, name="home"),   # Homepage URL
]

urlpatterns += staticfiles_urlpatterns()  # Serve static files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
