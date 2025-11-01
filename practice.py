from locust import HttpUser, task, between

expected_status_code = 200
max_response_time_ms = 2000


def check_response(endpoint, response, expected_status=expected_status_code, max_time=max_response_time_ms):
    """
    Helper function to validate response status code and response time.
    """
    response_time = response.elapsed.total_seconds() * 1000
    
    if response.status_code == expected_status:
        print(f"✓ GET {endpoint} - Status: {response.status_code}")
        if response_time <= max_time:
            print(f"✓ GET {endpoint} - response time: {response_time:.2f} ms")
        else:
            print(f"✗ GET {endpoint} - response time: {response_time:.2f} ms (exceeded {max_time}ms)")
    else:
        print(f"✗ GET {endpoint} - Status: {response.status_code}")


class QuickstartUser(HttpUser):
    """
    Locust user class to simulate API users and test endpoints.
    """
    
    # Wait time between requests (1-3 seconds)
    wait_time = between(1, 3)
    
    def on_start(self):
      """Called when a simulated user starts running."""
      pass

    def on_stop(self):
      """Called when a simulated user stops running."""
      pass
    
    @task(3)
    def get_products(self):
        """
        Task to test a GET API endpoint.
        It uses the user `client` attribute which is an instance of HttpSession.
        """
        endpoint = "/api/productsList"
        response = self.client.get(
            endpoint,
            headers={"Content-Type": "application/json"}
        )
        check_response(endpoint, response)

    @task
    def get_brands(self):
        """
        Task to test a GET API endpoint.
        """
        endpoint = "/api/brandsList"
        response = self.client.get(
            endpoint,
            headers={"Content-Type": "application/json"}
        )
        check_response(endpoint, response)

if __name__ == "__main__":
    print("Locust load testing script ready!")
