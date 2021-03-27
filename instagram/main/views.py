from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services.handle_get_list_of_unfollowing_users import handle_get_list_of_unfollowing_users
from .services.handle_get_followers import handle_get_followers
import json


@csrf_exempt
@api_view(['POST'])
def get_followers(request):
	"""
    Для работы с API необходимо отправить post запрос, в поле content необходимо вставить следующую информацию:

    {
		"sessionid" : "1558387502%3Ay4mOggyQrbcgdy%3A18",
		"login": "_shirling_"
    }
    """
	request_attr = json.loads(request.body)
	sessionid = request_attr['sessionid']
	login = request_attr['login']

	msg, status_code = handle_get_followers(sessionid, login)
	if status_code == 200:
		return Response( {"msg": msg} , status=status.HTTP_200_OK)
	elif status_code == 429:
		return Response( {"msg": msg} , status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response( {"msg": msg} , status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['POST'])
def get_list_of_unfollowing_users(request):
	"""
    Для работы с API необходимо отправить post запрос, в поле content необходимо вставить следующую информацию:

    {
		"sessionid" : "1558387502%3Ay4mOggyQrbcgdy%3A18",
		"login": "_shirling_"
    }
    """
	request_attr = json.loads(request.body)
	sessionid = request_attr['sessionid']
	login = request_attr['login']

	msg, status_code = handle_get_list_of_unfollowing_users(sessionid, login)
	if status_code == 200:
		return Response( {"msg": msg} , status=status.HTTP_200_OK)
	elif status_code == 429:
		return Response( {"msg": msg} , status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response( {"msg": msg} , status=status.HTTP_204_NO_CONTENT)
		