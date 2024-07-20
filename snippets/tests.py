# from django.test import TestCase→コメントアウト(書籍と同じコードにするため)

# Create your tests here.
# from django.http import HttpRequest
from django.test import TestCase
from snippets.views import top

class TopPageTest(TestCase):
  def test_top_returns_200(self):
    # request = HttpRequest() #HttpRequestオブジェクトの作成
    response = self.client.get("/")
    self.assertEqual(response.status_code, 200)
    def test_top_returns_expected_content(self):
      response = self.client.get('/')
      self.assertEqual(response.content, b"Hello World")