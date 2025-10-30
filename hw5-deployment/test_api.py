
import requests

def test_api():
    url = "http://localhost:8000/predict"
    client = {
        "lead_source": "organic_search",
        "number_of_courses_viewed": 4,
        "annual_income": 80304.0
    }
    try:
        response = requests.post(url, json=client)
        result = response.json()
        print(f"API Response: {result}")
        return result['conversion_probability']
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    test_api()
