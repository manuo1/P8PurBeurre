import sys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from django.conf import settings
from selenium import webdriver

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--headless')
firefox_options.add_argument('window-size=1920x1080')


class FirefoxFunctionalTestCases(StaticLiveServerTestCase):
    """Functional tests using the Firefox web browser in headless mode."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Firefox(
            executable_path=str(
                    settings.BASE_DIR / 'webdrivers' / 'geckodriver.exe'),
            options=firefox_options,
        )
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()

    def setUp(self):
        User = get_user_model()
        User.objects.create_user(
            username="testusername",
            password="testpassword",
            email="testusername@mail.com"
        )

    def test_user_can_connect_and_disconnect(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element_by_css_selector('#button-login').click()
        self.driver.find_element_by_css_selector('#id_username').send_keys(
            "testusername"
        )
        self.driver.find_element_by_css_selector('#id_password').send_keys(
            "testpassword"
        )
        self.driver.find_element_by_css_selector('#button-login-submit').click()
        self.driver.find_element_by_css_selector('#button-logout').click()
        self.assertTrue(
            self.driver.find_element_by_css_selector('#button-login')
        )
        
    def test_user_can_create_an_account(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element_by_css_selector('#button-login').click()
        self.driver.find_element_by_css_selector(
                                    '#button-create-account').click()
        self.driver.find_element_by_css_selector('#id_username').send_keys(
            "testusername2"
        )
        self.driver.find_element_by_css_selector('#id_first_name').send_keys(
            "testuserfirstname2"
        )
        self.driver.find_element_by_css_selector('#id_email').send_keys(
            "testusername2@mail.com"
        )
        self.driver.find_element_by_css_selector('#id_password1').send_keys(
            "testpassword2"
        )
        self.driver.find_element_by_css_selector('#id_password2').send_keys(
            "testpassword2"
        )
        self.driver.find_element_by_css_selector(
                                    '#button-create-submit').click()
        message = self.driver.find_element_by_css_selector(
                                '#login-messages').get_attribute('innerHTML')
        self.assertEqual( message ,
                " Un nouveau compte vient d'être créé pour testusername2 ")

    def test_user_can_display_his_profile(self):
        self.driver.get(self.live_server_url)
        self.driver.find_element_by_css_selector('#button-login').click()
        self.driver.find_element_by_css_selector('#id_username').send_keys(
            "testusername"
        )
        self.driver.find_element_by_css_selector('#id_password').send_keys(
            "testpassword"
        )
        self.driver.find_element_by_css_selector(
                                            '#button-login-submit').click()
        self.driver.find_element_by_css_selector('#button-profile').click()
        email = self.driver.find_element_by_css_selector(
                                '#profile-mail').get_attribute('innerHTML')
        self.assertEqual( email ," testusername@mail.com ")