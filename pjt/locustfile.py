from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(3, 4)
    
    @task(1)
    def index(self):
      self.client.get('http://127.0.0.1:8000/')