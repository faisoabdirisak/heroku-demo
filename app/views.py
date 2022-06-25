from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from django.contrib import messages



# Create your views here.

def home(request):
    return render(request, 'school/home.html')

@login_required(login_url='login')
def read(request):
    return render(request, 'school/read.html')

@login_required(login_url='login')
def math(request):
    return render(request, 'school/math.html')

@login_required(login_url='login')
def color(request):
    return render(request, 'school/color.html')

@login_required(login_url='login')
def environment(request):
    return render(request, 'school/environment.html')

@login_required(login_url='login')
def comp(request):
    return render(request, 'school/computer.html')

@login_required(login_url='login')
def religion(request):
    return render(request, 'school/religion.html')


# def submit_review(request):
   
#     if request.method == 'POST':
#         try:
#             reviews = Review.objects.get(owner=request.owner)
#             form = Review(request.POST, instance=reviews)
#             form.save()
#             messages.success(request, 'Thank you! Your review has been updated.')
#             return redirect('home')
#         except Review.DoesNotExist:
#             form = ReviewForm(request.POST)
#             if form.is_valid():
#                 data = Review()
#                 data.rating = form.cleaned_data['rating']
#                 data.review = form.cleaned_data['review']
#                 data.save()
#                 messages.success(request, 'Thank you! Your review has been submitted.')
#                 return redirect('home')