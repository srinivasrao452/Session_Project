
from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    data = "Welcome to Session Concept"
    return HttpResponse(data)


def create_session_view(request):
    request.session.set_test_cookie()
    return HttpResponse("Session is created in the Server side")

def delete_session_view(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("Session id value deleted successfully.")
        return response
    else:
        response = HttpResponse("session id value is not available")
        return response


def save_session_data_view(request):
    request.session["eno"] = 101
    request.session["ename"] = "Purna"
    request.session["salary"] = 10000
    request.session["languages"] = "Python"

    return HttpResponse("Session data saved in to server side.")


def access_session_data_view(request):
    response = ""
    if request.session.get("eno"):
        response = response + "<h1>Employee number is : {}<br>".format(request.session.get("eno"))

    if request.session.get("ename"):
        response = response + "Employee name is : {}<br>".format(request.session.get("ename"))

    if request.session.get("salary"):
        response = response + "Employee salary is : {}<br>".format(request.session.get("salary"))

    if request.session.get("languages"):
        response = response + "Employee language  : {}</h1><br>".format(request.session.get("languages"))

    if response:
        return HttpResponse(response)

    else:
        return HttpResponse('session data not available')


def delete_session_data_view(request):
    if request.session:
        try:
            del request.session["eno"]
            del request.session["ename"]
            del request.session["salary"]
            del request.session["languages"]
        except KeyError:
            return HttpResponse("session data not deleted successfully.")
        else:
            return HttpResponse("session data cleared now.")
    else:
        return HttpResponse("Session data not available to delete")








