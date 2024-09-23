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


    path('search-jokes/', views.search_jokes, name='search_jokes'), # Real-time search done
    path('search-users/', views.search_users, name='search_users'), # Real-time search done
    path('moreinfo/<int:history_id>/', views.moreinfo, name='moreinfo'), #done

    # rating
    path('ratehistory/', views.rate_history, name='rate_history'), #done

    # offensive or not
    path('update-offensive/', views.update_offensive, name='update_offensive'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/country-status/', views.get_country_status_data, name='country_status_data'),
    path('api/offensive-status/', views.get_offensive_status_data, name='offensive_status_data'),
    
    
    path('word-frequency-data/', views.word_frequency_data, name='word_frequency_data'),  # URL for fetching word frequency data

    path('dashboard/api/average-status/', views.get_average_status, name='get_average_status'),
    path('dashboard/api/user-history/', views.get_user_history, name='get_user_history'),
    path('get-country-specific-data/', views.get_country_specific_data, name='get_country_specific_data'),






]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

