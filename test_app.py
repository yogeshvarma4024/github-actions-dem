from app import app


def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello from GitHub Actions CI!"}


def test_sum():
    client = app.test_client()
    response = client.get('/sum/4/6')
    assert response.status_code == 200
    assert response.get_json() == {"sum": 10}
