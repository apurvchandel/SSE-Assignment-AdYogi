import requests
import unittest
from unittest.mock import patch



class UpstashPriorityQueue:
    def __init__(self, upstash_url, token):
        self.upstash_url = upstash_url
        self.token = token

    def enqueue(self, request, priority):
        data = {'request': request, 'priority': priority}
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.post(f'{self.upstash_url}/enqueue', json=data, headers=headers)
        return response.json()

    def dequeue(self):
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(f'{self.upstash_url}/dequeue', headers=headers)
        return response.json()
    

class TestUpstashPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.queue = UpstashPriorityQueue("https://prompt-deer-29810.upstash.io", "AXRyAAIjcDExZDlmNDkxMTk0ZmM0ZmI3OWY1NmRiM2JiMDc0MzI0N3AxMA")

    @patch('requests.post')
    def test_enqueue(self, mock_post):
        mock_post.return_value.json.return_value = {"status": "success"}
        response = self.queue.enqueue("task1", 1)
        self.assertEqual(response["status"], "success")

    @patch('requests.get')
    def test_dequeue(self, mock_get):
        mock_get.return_value.json.return_value = {"request": "task1"}
        response = self.queue.dequeue()
        self.assertEqual(response["request"], "task1")

if __name__ == '__main__':
    unittest.main()
