from locust import HttpUser, task


class UserBehavior(HttpUser):
    @task
    def get_user(self):
        self.client.get("/users/123")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 5000
    max_wait = 9000
