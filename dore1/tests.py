from django.test import TestCase
from django.urls import reverse
from .models import UserModel
from .views import Views

class TestCase(TestCase):
    def setUp(self):
        UserModel.objects.create(
            username="hassan ghabel",
            ncode="088054688",
            phonenumber="0989158830786",
            rtahsi="electronic",
            arr="pr-pr20"
        )

    def test_user_creation(self):
        """Test user object creation"""
        user = UserModel.objects.get(username="hassan ghabel")
        self.assertEqual(user.username, "hassan ghabel")
        self.assertEqual(user.ncode, "088054688")
        self.assertEqual(user.phonenumber, "0989158830786")
        self.assertEqual(user.rtahsi, "electronic")
        self.assertEqual(user.arr, "pr-pr20")
       
        

    def test_index_view(self):
        """Test index view"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "قرار هست در این دوره به صورت قدرتمند کسب درآمد با هوش مصنوعی را دنبال کنیم اگر عاشق بروز شدن و کسب درآمد با هوش مصنوعی هستی بزن بریم")
        self.assertTemplateUsed(response, 'index.html')
   

   