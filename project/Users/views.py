# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import SignUpForm, AuthenticationForm, UserUpdateForm
from .models import User, History, WordFrequency
from .nlpmodel import dummy
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.views.decorators.http import require_http_methods
from django.db.models import Avg
from django.db.models.functions import Trim
import os


def moreinfo(request, history_id):
    user_id1 = request.session.get('user_id')
    history = History.objects.filter(id=history_id, user_id=user_id1).first()
    return render(request, 'more-infopopup.html', {'history': history})


def generate_sentence(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        #selected_number = data.get('joke_type')
        
        # Map selected_number to corresponding keyword
        # if selected_number == 1:
        #     keyword = "Sport"
        # elif selected_number == 2:
        #     keyword = "Food"
        # elif selected_number == 3:
        #     keyword = "Game"
        # elif selected_number == 4:
        #     keyword = "Nostalgia"
        # elif selected_number == 5:
        #     keyword = "Weather"
        # else:
        #     return JsonResponse({'error': 'Invalid number selected'}, status=400)
        
        selected_country = data.get('country')
        print(selected_country)
         # Map selected_country to corresponding country
        if selected_country == 1:
            Country = "Malaysia"
        elif selected_country == 2:
            Country = "China"
        elif selected_country == 3:
            Country = "India"
        elif selected_country == 4:
            Country = "South Korea"
        elif selected_country == 5:
            Country = "Qatar"
        else:
            return JsonResponse({'error': 'Invalid country selected'}, status=400)
        
        # Assuming dummy function call and sentence generation logic
        # Replace with your actual logic
        #sentence = f"You generated the sentence with keyword '{keyword}'."
        usr_obj = User.objects.get(id=request.session.get('user_id'))

        # sentence = dummy(Country, selected_number)
        sentence = dummy(Country)

        #History.objects.create(user=usr_obj, description=sentence, keyword="No keyword",country = Country,offensive=None, status=0).save() 
        # return JsonResponse({'sentence': sentence})
        newhistory = History.objects.create(user=usr_obj, description=sentence, keyword="No keyword",country = Country,offensive=None, status=0)
        return JsonResponse({'sentence': sentence, 'id': newhistory.id})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            print("testting testing tseting")
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    user_id = request.session.get('user_id')
    if user_id:
        return redirect('index')
    elif request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.data['username']
            password = form.data['password']
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = None
            if user is not None and user.password == password:     
                request.session['user_id'] = user.id
         
                return redirect('index')
            else:
            # Authentication failed
                error_message = 'Invalid username or password'
    else:
        form = AuthenticationForm()
        error_message = None
    return render(request, 'login.html', {'form': form, 'error_message': error_message})

def index(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
    else:
        user = None
    return render(request, 'home.html', {'user': user})

def history(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
        histories = History.objects.filter(user_id=user_id)
        if len(histories) == 0:
            histories = None

    else:
        user = None
        histories = None
    
    return render(request, 'history.html', {'user': user, 'histories': histories})


def usersettings(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
    else:
        user = None

    old_profile_image = user.profile_image.path if user and user.profile_image and user.profile_image != 'images/profilepic.jpg' else None
    
    if request.method == 'POST':
        if 'remove_profile_image' in request.POST:
            if old_profile_image and os.path.exists(old_profile_image):
                os.remove(old_profile_image)
            user.profile_image = 'images/profilepic.jpg'  # Set back to default
            user.save()
            return redirect('usersettings')
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('usersettings')
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'usersettings.html',{'user': user, 'form': form})

def user_database(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
        all_user = User.objects.all()
    else:
        user = None
        all_user = None
    return render(request, 'user_database.html',{'user': user, 'allusers': all_user})

def logout(request):
    auth_logout(request)
    request.session.flush()  # Clear all session data
    return redirect('login')

def delete_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username_to_delete = data.get('username')
        
        try:
            user_to_delete = User.objects.get(username=username_to_delete)

             # Delete the user's profile image if it exists and is not the default image
            if user_to_delete.profile_image != 'images/profilepic.jpg':
                image_path = user_to_delete.profile_image.path
                if os.path.exists(image_path):
                    os.remove(image_path)
                    
            user_to_delete.delete()
            return JsonResponse({'message': f'User {username_to_delete} deleted successfully!'})
        except User.DoesNotExist:
            return JsonResponse({'message': f'User {username_to_delete} does not exist.'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def delete_history(request):
    # if request.method == 'POST':
    #     data = json.loads(request.body)
    #     history_id = data.get('id')
    #     try:
    #         history = History.objects.get(id=history_id)
    #         history.delete()
    #         return JsonResponse({'message': 'History deleted successfully'})
    #     except History.DoesNotExist:
    #         return JsonResponse({'message': 'History not found'}, status=404)
    # else:
    #     return JsonResponse({'message': 'Invalid request method'}, status=405)
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            history_id = data.get('id')
            history = History.objects.get(id=history_id)
            history.delete()
            return JsonResponse({'message': 'History deleted successfully'})
        except History.DoesNotExist:
            return JsonResponse({'message': 'History not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)



def rate_history(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        history_id = data.get('id')
        rating = data.get('rating')
        print(history_id)
        print(rating)
        try:
            history = History.objects.get(id=history_id)
            history.status = rating
            history.save()
            return JsonResponse({'message': 'History updated successfully'})
        except History.DoesNotExist:
            return JsonResponse({'message': 'History not found'}, status=404)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
    
@require_http_methods(["GET"])
def search_users(request):
    query = request.GET.get('q', '')
    print(request.user)
    
    if query:
        users = User.objects.filter(username__icontains=query)
    else:
        users = User.objects.all()  # Return all users if query is empty

    results = [{
        'username': user.username,
        'country': user.country,  # Assuming you have a Profile model linked to User with country info
        'age': user.age,          # Assuming age is also stored in the Profile model
        'gender': user.gender,    # Assuming gender is also stored in the Profile model
        'can_delete': user != request.user,
    } for user in users]

    return JsonResponse({'users': results})

@require_http_methods(["GET"])
def search_jokes(request):
    query = request.GET.get('q', '')
    user_id = request.session.get('user_id')
    #histories = History.objects.filter(user_id=user_id)
    
    if query:
        histories = History.objects.filter(user_id=user_id, description__icontains=query).values('id', 'description')
    else:
        histories = History.objects.filter(user_id=user_id).values('id', 'description') # Return all histories if query is empty
    results = list(histories)
    # results = [{
    #     'id': history.id,
    #     'description': history.description,
    # } for history in histories]
    # print(results)

    return JsonResponse({'histories': results})


def update_offensive(request):
    data = json.loads(request.body)
    history_id = data.get('id')
    offensive = data.get('offensive')
    try:
        history = History.objects.get(id=history_id)
        history.offensive = offensive
        history.save()
        return JsonResponse({'message': 'Offensive status updated successfully'})
    except History.DoesNotExist:
        return JsonResponse({'message': 'History not found'}, status=404)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=500)
    

    

def dashboard(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
    else:
        user = None
    return render(request, 'Dashboard.html', {'user': user})

def get_country_status_data(request):

    # country_status = History.objects.annotate(trimmed_country=Trim('country')).values('trimmed_country').annotate(avg_status=Avg('status')).order_by('trimmed_country')
    
    # data = {
    #     'countries': [item['trimmed_country'] for item in country_status],
    #     'avg_statuses': [item['avg_status'] for item in country_status],
    # }
    country_status = History.objects.filter(status__gt=0).annotate(
        trimmed_country=Trim('country')
    ).values('trimmed_country').annotate(
        avg_status=Avg('status')
    ).order_by('trimmed_country')
    
    data = {
        'countries': [item['trimmed_country'] for item in country_status],
        'avg_statuses': [item['avg_status'] for item in country_status],
    }
    
    return JsonResponse(data)


def get_offensive_status_data(request):
    try:
        # Calculate counts directly
        count_offensive = History.objects.filter(offensive=True).count()
        count_non_offensive = History.objects.filter(offensive=False).count()
        count_not_rated = History.objects.filter(offensive__isnull=True).count()
        
        # Prepare the data
        data = {
            'categories': ['Offensive', 'Non-Offensive', 'Not Rated'],
            'counts': [count_offensive, count_non_offensive, count_not_rated]
        }
        
        return JsonResponse(data)
    except Exception as e:
        print("Error occurred:", e)  # Debugging line
        return JsonResponse({'error': 'An error occurred'}, status=500)
    
def word_frequency_data(request):
    """Fetch word frequency data for the word cloud."""
    word_frequencies = WordFrequency.objects.all()
    
    # Prepare data for Chart.js
    data = {
        'words': [entry.word for entry in word_frequencies],
        'frequencies': [entry.frequency for entry in word_frequencies]
    }
    #print(data)

    return JsonResponse(data)