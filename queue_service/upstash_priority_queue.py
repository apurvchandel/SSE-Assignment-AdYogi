import requests

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
