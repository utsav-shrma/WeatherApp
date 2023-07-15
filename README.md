# WeatherApp
A Django-based backend serves as the foundation for a basic weather API app. 
This app utilizes the OpenWeatherMap API to retrieve forecast data based on the specified time period provided in the request. It also stores the API responses locally. If a subsequent request is made for the same coordinates, it checks the expiration time of the data and sends/updates the data accordingly.

# Endpoint

# POST : /weather/api/

        {
        "lat":{},
        "lon":{},
        "detailType":"{}"
        }

        lat: lattitude
        lon: longitude
        detailType:  forecast detail type 
                      H: Hourly
                      D: Daily
                      W: Weekly

# How to setup
1. Clone Repo
2. Run **pipenv install** to create the virtual environement
3. Provide your OpenWeatherMap API access token in the **ACCESS_TOKEN** variable in **WeatherApp/weatherApp/weatherApp** file.
4. Run **pipenv shell** to activate virtual env
5. Navigate to **./weatherApp**
6. Run **python manage.py migrate** to set up database locally
7. Run **python manage.py runserver** to run it
8. Go to your brower and make your POST request with the given JSON format to get data 
        
