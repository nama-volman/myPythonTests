import json
import shutil
import tempfile
import urllib.request
from pathlib import Path
import pytest


USERS_URL = "https://jsonplaceholder.typicode.com/users"

def download_users_file():
    temp_dir = Path(tempfile.mkdtemp(prefix="users_"))
    users_path = temp_dir / "users.json"
    urllib.request.urlretrieve(USERS_URL,  users_path)
    return  users_path 

def delete_users_file(users_file):
    shutil.rmtree(users_file.parent, ignore_errors=True)

@pytest.fixture(scope="module")
def users_json():
    users_file = download_users_file()
    print(f"\nDownloaded users file to: {users_file}")
    json_content = json.loads(users_file.read_text(encoding="utf-8"))
    yield json_content
    delete_users_file(users_file)
    print( "\nusers file deleted!")


def test_exist_name(users_json):
    assert any(user.get("name") == "Patricia Lebsack" for user in users_json), "Patricia Lebsack was not found in the users list"

def test_users_json_content(users_json):
    print(f"users JSON content length: {len(users_json)}")
    assert len(users_json) == 10

#negative test
def test_not_exist_city(users_json):
    assert all(user.get("address", {}).get("city") != "Lebsackbury" for user in users_json), "\nExist user that living in Lebsackbury"

def test_exist_city(users_json):
    assert any(user.get("address", {}).get("city") == "Lebsackbury" for user in users_json), "\n Not exist user that living in Lebsackbury"