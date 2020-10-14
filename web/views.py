from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from .models import User, Expense, Income, Token


@csrf_exempt
def submit_income(request):
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    Income.objects.create(user=this_user, amount=request.POST['amount'], text=request.POST['text'])
    return JsonResponse({'status': 'ok'}, encoder=JSONEncoder)


@csrf_exempt
def submit_expense(request):
    print("*"*50)
    print("we are here")
    print(request.POST)
    print("*"*50)
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    Expense.objects.create(user=this_user, amount=request.POST['amount'], text=request.POST['text'])
    return JsonResponse({'status': 'ok'}, encoder=JSONEncoder)
