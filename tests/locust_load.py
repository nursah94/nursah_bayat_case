from locust import HttpUser, task, between

class N11User(HttpUser):
    wait_time = between(1, 3)

    @task
    def search_telefon(self):
        
        with self.client.get("/arama?q=telefon", name="Search: telefon", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Unexpected status code: {response.status_code}")