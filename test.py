if __name__ == "__main__":
    import requests

    token = "my-secret-api-key-123"

    headers = {
        "authorization": f"Bearer {token}",
    }

    params = {
        "name": "sudhir singh",
        "gender": "M",
        "class": "zen"
    }

    print(requests.get(
        "http://localhost:8000/list/users",
        headers=headers,
        params=params
    ).json())
