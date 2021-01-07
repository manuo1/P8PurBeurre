from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase
from django.urls import reverse
from _pytest.monkeypatch import MonkeyPatch

from app_users.views import loginPage

"""
class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.monkeypatch = MonkeyPatch()

    def test_login(self):
        print('start test login')
        request = self.factory.get(reverse('loginPage'))
        request.method = 'POST'
        request.user = AnonymousUser()

        class MockUser:
            def __init__(self):
                self.is_authenticated= True
                self.username='username'
                self.password='password'

        class MockAuthenticate:
            def __init__(self, request, username, password):
                self.user = MockUser()
                return self.user

        self.monkeypatch.setattr('app_users.views.authenticate', MockAuthenticate)

        class MockLogin:
            def __init__(self,request, user, backend=None):
                pass

        response = loginPage(request)
        #self.assertEquals(request.user.is_authenticated, True)
        self.assertRedirects(response, '/user/profile/')
"""
