from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.login, name='login'),
    path('home/', views.index, name='index'), #create history with restapi done
    path('logout/', views.logout, name='logout'),
    path('history/', views.history, name='history'), #with rud (ajax method ) 
    path('usersettings/', views.usersettings, name='usersettings'), #with ru only  done
    path('user_database/', views.user_database, name='user_database'),#with rd (ajax method) done
    #RESTAPI
    path('generate-sentence/', views.generate_sentence, name='generate_sentence'), #done #no refresh and redirect for generating using ai model
    path('delete-user/', views.delete_user, name='delete_user'), #done
    path('delete-history/', views.delete_history, name='delete_history'), # done

    # rate offensive 
    path('rate-history/', views.rate_history, name='rate_history'),
    
    path('search-users/', views.search_users, name='search_users'), # Real-time search
    path('moreinfo/<int:history_id>/', views.moreinfo, name='moreinfo'), #done


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

