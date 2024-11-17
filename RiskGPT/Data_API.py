import requests
# the data here i am targetting is of USA
def get_weather_data():
    api_key = "bd5e378503939ddaee76f12ad7a97608"

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "Washington, D.C.",  # USA's capital city
        "appid": api_key,  # API key
        "units": "metric"  # Temperature in Celsius
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.json()}
def get_news_data():
    """
    Fetch recent news related to New York using MediaStack API.
    """
    api_key = "5fc1fc6f85d9a0a881a01959bbece325"
    base_url = "http://api.mediastack.com/v1/news"
    params = {
        "access_key": api_key,
        "countries": "us",  # USA news
        "languages": "en",  # English only
        "limit": 5,  # Fetch top 5 articles
        "sort": "published_desc"  # Sort by newest
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.json()}
def get_gdp_data_usa():
    """
    Fetch GDP data for the USA from the World Bank API.
    """
    base_url = "http://api.worldbank.org/v2/country/US/indicator/NY.GDP.MKTP.CD"
    params = {
        "format": "json",
        "per_page": 5  # Fetch top 5 records
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if len(data) > 1:
            return data[1]  # Return the data array
        else:
            return {"error": "No data available"}
    else:
        return {"error": response.text}




