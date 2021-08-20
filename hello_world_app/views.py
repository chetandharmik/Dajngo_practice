from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt 
import urllib
import requests
from Hello_world import config
from .models import User

# Create your views here.
#Author : Chetan Dharmik
#Date : 12/08/2021
#function to get name
@csrf_exempt
def name(request):
    result={}
    try:
        data={"First_name":"Chetan123",
            "last_name":"Dharmik"}
    except (Exception) as error:
        print(error)
    return JsonResponse(data)





#Author : Chetan Dharmik
#Date : 12/08/2021
#function to get Designation
#@csrf_exempt
def designation(request):
    try:
        data={"Designation":"Solution Analyst"}
    except (Exception) as error:
        print(error)       
    return JsonResponse(data)





#Author : Chetan Dharmik
#Date : 12/08/2021
#function to get simple data
@csrf_exempt
def fake_api(request):
    try:
        data={"fake_api":"test"}
    except (Exception) as error:
        print(error)       
    return JsonResponse(data)





#Author : Chetan Dharmik
#Date : 12/08/2021
#function to get data in the form of array
@csrf_exempt
def arr_func(request):
    arr=[]
    try:
        data=[{"1":"my name"}]

    except (Exception) as error:
        print(error) 
    return JsonResponse(data,safe=False)






#Author : Chetan Dharmik
#Date : 12/08/2021
#function to get data from url
def  url_resp(request):
    name=[]
    data_id=[]
    postid=[]
    try:
        request = urllib.request.urlopen(config.url_hub)
        data = json.load(request)
        for i in range(len(data)):
            postid.append(data[i]['postId'])
            data_id.append(data[i]['id'])
            name.append(data[i]['name'])
    except (Exception) as error:
        print(error) 
    return JsonResponse(name,safe=False)


#Author : Chetan Dharmik
#Date : 12/08/2021
#function to add user data in User table
@csrf_exempt
def add_user_detail(request):
    try:
        user=User()
        user.name="Chetan"
        user.email="abcd@gmail.com"
        user.mobile_no="9822464647"
        user.designation="Solution Analyst"
        user.save()
        # data1=user.object.all()
        return JsonResponse(user,safe=False)
    except (Exception) as error:
        print(error) 


#Author : Chetan Dharmik
#Date : 19/08/2021
#function to add user data and check the response
@csrf_exempt
def Post_operation(request):
    try:
        data=json.loads(request.body.decode("utf-8"))
        U_name = data.get('user_name')
        U_id = data.get('user_id')
        U_position = data.get('user_position')
        user_data = {
                'user_name': U_name,
                'user_id': U_id,
                'user_position': U_position,
            }
        return JsonResponse(user_data,safe=False)
    except (Exception) as error:
        print(error) 


#Author : Chetan Dharmik
#Date : 19/08/2021
#function to process data and get the Total death in the country.
@csrf_exempt
def get_Total_death(request):
    try:
        death={}
        sum1=0
        request = urllib.request.urlopen(config.dump_api)
        data=json.load(request)

        for i in range(len(data['Countries'])):
            death[i]=data['Countries'][i]['TotalDeaths']
            sum1=sum1+ death[i]
        return JsonResponse(data,safe=False)
    except (Exception) as error:
        print(error) 

#Author : Chetan Dharmik
#Date : 20/08/2021
#function to process data and get the name of the countries and add it in the array.
@csrf_exempt
def get_name_of_countries(request):
    try:
        country={}
        sum1=0
        request = urllib.request.urlopen(config.dump_api)
        data=json.load(request)

        for i in range(len(data['Countries'])):
            country[i]=data['Countries'][i]['Country']
        return JsonResponse(country,safe=False)
    except (Exception) as error:
        print(error) 


#Author : Chetan Dharmik
#Date : 20/08/2021
    
        









