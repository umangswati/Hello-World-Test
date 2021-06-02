from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "jan": "This is Jan Month",
    "feb": "This is feb month",
    "mar": "This is mar month",
    "apr": "This is april month",
    "may": "This is may month",
    "jun": "This is jun month",
    "jul": "This is feb month",
    "Aug": "This is feb month",
    "sep": "This is feb month",
    "oct": "This is feb month",
    "nov": "This is feb month",
    "dec": "This is feb month",

 
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        list_item = ""
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge",args=[month])
        list_items += f"<li><h1><a href=\"{month_path}\">{capitalized_month}</a></h1></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request,month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")


    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>not a valid month</h1>")

    
        