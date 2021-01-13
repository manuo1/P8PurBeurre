from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app_users.views import registerPage, loginPage, logoutCurrentUser, profile


class TestAppUsersUrls(SimpleTestCase):
    def test_loginpage_url_resolves(self):
        url = reverse('loginPage')
        self.assertEquals(resolve(url).func, loginPage)

    def test_registerpage_url_resolves(self):
        url = reverse('registerPage')
        self.assertEquals(resolve(url).func, registerPage)

    def test_logoutcurrentser_url_resolves(self):
        url = reverse('logoutCurrentUser')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, logoutCurrentUser)

    def test_profilepage_url_resolves(self):
        url = reverse('profilePage')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, profile)
