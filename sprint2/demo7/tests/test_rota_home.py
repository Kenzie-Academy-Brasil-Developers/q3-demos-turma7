from app import app


def client_app():
    return app.test_client()


def test_home_status():
    client = client_app()
    return_response = client.get("/")
    assert return_response.status_code == 200, "Bad status"
    

