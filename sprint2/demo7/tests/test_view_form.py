from app import app


test_client = app.test_client()


def test_file_upload():
    print(test_client.options("/form").headers["Allow"])