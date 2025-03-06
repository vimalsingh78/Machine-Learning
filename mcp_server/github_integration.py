import os
import requests
from dotenv import load_dotenv

load_dotenv()

class GitHubIntegration:
    def __init__(self):
        self.token = os.getenv('GITHUB_TOKEN')
        self.username = os.getenv('GITHUB_USERNAME')
        self.base_url = 'https://api.github.com'
        self.headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json'
        }
    
    def test_connection(self):
        """Test the GitHub connection"""
        response = requests.get(
            f'{self.base_url}/user',
            headers=self.headers
        )
        return response.status_code == 200
    
    def list_repositories(self):
        """List user's repositories"""
        response = requests.get(
            f'{self.base_url}/user/repos',
            headers=self.headers
        )
        return response.json() if response.status_code == 200 else []
    
    def create_repository(self, name, description="", private=False):
        """Create a new repository"""
        data = {
            "name": name,
            "description": description,
            "private": private
        }
        response = requests.post(
            f'{self.base_url}/user/repos',
            headers=self.headers,
            json=data
        )
        return response.json() if response.status_code == 201 else None
    
    def create_issue(self, repo_name, title, body):
        """Create an issue in a repository"""
        data = {
            "title": title,
            "body": body
        }
        response = requests.post(
            f'{self.base_url}/repos/{self.username}/{repo_name}/issues',
            headers=self.headers,
            json=data
        )
        return response.json() if response.status_code == 201 else None