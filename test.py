if __name__ == "__main__":
    import requests

    token = "my-secret-api-key-123"

    headers = {
        "authorization": f"Bearer {token}",
    }

    print(requests.get(
        "http://localhost:8000/jobs/32",
        headers=headers,
    ).json())