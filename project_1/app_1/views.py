from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("This is my response!")
def dashboard(request):
    return HttpResponse(" place where user"+ str(id) + " dashboard is")
def user_page(request, id):
    return HttpResponse("this is the user page")
# def catch_all(request):
#     return HttpResponse("you found a match with the last route")
def firstTemplate(request):
    context = {
        'name': "bob smith", 
        'email': "bob@gmail.com"
    }
    return render(request, "index.html", context)
def submission(request):
    print(request.POST['user_name'])
    print(request.POST)
    request.session['user_name'] = request.POST["user_name"]
    request.session["secret"] = request.POST["secret"],
    request.session["character"] = request.POST["character"]
    return redirect("/thank_you")
    # return HttpResponse("This form has been submitted thank you " + request.POST['user_name'])
def thank_you(request):
    # context = {
    #     "name" : request.session["user_name"],
    #     "secret" : request.session["secret"],
    #     "character" : request.session['character'],
    # }
    return render(request, "thank_you.html")
# bad idea to render on a post route
