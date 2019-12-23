from github import Github
from file_utils import safe_file_read

def auth():
    """Authenticates the program with the github api and the wakatime api
    """
    safe_file_read("configs/.secrets.json", "json")
    
