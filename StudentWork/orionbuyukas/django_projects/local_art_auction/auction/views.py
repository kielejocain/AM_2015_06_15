from django.shortcuts import render

# Create your views here.
def bid(request):

    if request.method == "POST":
        max_bid = request.POST['max_bid']
        bid = Bid()
        newUser.username = username
        newUser.set_password(password)
        newUser.save()
        return render(request, 'signup-complete.html', {})
    return render(request, 'signup.html', {})