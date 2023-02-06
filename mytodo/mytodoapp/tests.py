from django.test import TestCase
from .models import Book   #사실 에러
# Create your tests here.
class ModelTest(TestCase):
    # 테스트를 수행하기 전에 호출되는 함수
    def setup(self):
        self.book_title = 'harry poter'
        self.book_author= 'lee'
        self.book = Book(
            title=self.book_title, author = self.book_author)

        # 테스트를 위한 함수

    def test_model_can_create_a_bucketlist(self):
        old_count = Book.objects.count()
        self.book.save()
        new_count = Book.objects.count()
        self.assertNotEqual(old_count, new_count)

from rest_framework.test import APIClient
from rest_framework import status

class ViewTest(TestCase):
    def setup(self):
        self.client = APIClient()
        self.book_data = {'title':'ring','author':'joo'}
        self.response = self.client.post('/api/books/', self.book_data,format='json')

    # 테스트를 위한 함수
    def test_api_can_create_a_book(self):
        print(self.response.content)
        self.assertNotEqual(self.response.status_code,
                            status.HTTP_201_CREATED)

