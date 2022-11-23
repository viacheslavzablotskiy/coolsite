# from unittest import TestCase
#
# from django.urls import reverse, resolve
# from rest_framework.test import APITestCase, APIClient
# from rest_framework.authtoken.models import Token
# from rest_framework import status
# from django.contrib.auth.models import User
# from rest_framework.utils import json
#
# from rest_framework.views import APIView
# # self.client = APIClient()
# from drfsite.settings import SIMPLE_JWT
# from posts.views import WomenAPIList
#
#
#
# class RouterTestApi(APITestCase):
#     url = reverse('margo')
#
#
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='zlava', password='1902')
#         self.token = Token.objects.create(user=self.user)
#         # self.client = Client()
#         # self.client.login(email=self.user.email, password=self.pa
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
#
#         data = {
#             "id": 1,
#             'title': 'LOGIN',
#             'content': 'COOL PUT GET DELETE',
#             # "time_create": "2022-11-17T22:38:11.840967Z",
#             'is_published': True,
#             'cat_id': 'программирование',
#
#         }
#         self.client.post(self.url, data, format='json')
#
#
#     def test_router_simple_costumer(self):
#         # costumer_url = reverse('main', args=[1])
#         response = self.client.get(reverse("main", args=[1]))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['title'], 'LOGIN')
#
#     def test_get_customers_un_authenticated(self):
#         # costumer_url = reverse('main', args=[1])
#         self.client.force_authenticate(user=None, token=None)
#         response = self.client.get(reverse("main", args=[1]))
#         self.assertEquals(response.status_code, 401)