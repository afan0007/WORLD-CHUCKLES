# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import SignUpForm, AuthenticationForm, UserUpdateForm
from .models import User, History
from .nlpmodel import dummy
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.views.decorators.http import require_http_methods


def moreinfo(request, history_id):
    history = get_object_or_404(History, id=history_id)
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

        History.objects.create(user=usr_obj, description=sentence, keyword="No keyword",country = Country,offensive=None, status=0).save() 

        
        return JsonResponse({'sentence': sentence})
    
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
    
    if request.method == 'POST':
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