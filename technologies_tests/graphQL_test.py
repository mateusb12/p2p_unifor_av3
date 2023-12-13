import random

from locust import HttpUser, TaskSet, task


class UserTasks(TaskSet):
    def __init__(self, parent):
        super().__init__(parent)
        self.user_ids = None

    def on_start(self):
        # Define sample user IDs for testing
        self.user_ids = ["user1", "user2", "user3"]

    @task
    def get_user(self):
        # Select a random user ID
        user_id = self.user_ids[random.randint(0, len(self.user_ids) - 1)]

        # Prepare the GraphQL request
        query = """
            query GetUser($userID: String!) {
                user(id: $userID) {
                    name
                    email
                    friends
                    posts
                    activity
                }
            }
        """
        variables = {"userID": user_id}

        # Send the GraphQL request
        response = self.client.post("/graphql", json={"query": query, "variables": variables})

        # Check for successful response
        response.raise_for_status()

        # Parse and analyze the response data
        data = response.json()
        assert data["data"]["user"]


class GraphQLStressTest(HttpUser):
    tasks = [UserTasks]
    min_wait = 100
    max_wait = 500

    # Set the number of concurrent users for the test
    # (adjust this value to your desired test load)
    users = 10
