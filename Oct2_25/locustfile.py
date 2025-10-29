"""
Load Testing Script for amjresume.com using Locust

Installation:
pip install locust

Usage:
locust -f locustfile.py --host=https://amjresume.com

Then open http://localhost:8089 in your browser to configure and start the test
"""

from locust import HttpUser, task, between
import random

class WebsiteUser(HttpUser):
    # Wait between 1-3 seconds between tasks (simulating real user behavior)
    wait_time = between(1, 3)
    
    def on_start(self):
        """Called when a user starts - good for login or initial setup"""
        # Visit homepage first (like a real user would)
        self.client.get("/")
    
    @task(3)  # Weight of 3 - this task runs 3x more often
    def view_homepage(self):
        """Test homepage loading"""
        self.client.get("/")
    
    @task(2)  # Weight of 2
    def view_about(self):
        """Test about page or other pages"""
        # Adjust these paths based on your actual website structure
        pages = ["/about", "/contact", "/projects"]
        page = random.choice(pages)
        self.client.get(page, name="/random-page")
    
    @task(1)  # Weight of 1
    def view_specific_resource(self):
        """Test specific resources or API endpoints"""
        # Example: testing image loads, CSS, JS files
        resources = [
            "/static/css/style.css",
            "/static/js/main.js",
            "/favicon.ico"
        ]
        resource = random.choice(resources)
        self.client.get(resource, name="/static-resource")
    
    def on_stop(self):
        """Called when a user stops"""
        pass


class MobileUser(HttpUser):
    """Simulate mobile users with different headers"""
    wait_time = between(2, 5)
    
    def on_start(self):
        self.client.headers.update({
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15'
        })
    
    @task
    def browse(self):
        self.client.get("/")