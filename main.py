import json
import os
import requests

#This is a simple weather CLI that makes use of API's to return what your looking for. 
#Also caches results to a json for offline lookups and to use less API calls


#Core functions

def fetch_weather_data(cache, city, key):
    # build API request with city and key
        # send request, parse JSON, return dict
        
    try:
        urls = f"https://api.weatherapi.com/v1/current.json?key={key}&q={city}" #Is the url the request is going to
        responses = requests.get(urls) #Is sending the request to the url
    
        data = responses.json() #Is what the api replied, parsed.

        if "error" not in data: #If we used the response 200 method, it won't catch invalid city names because the API is called successfully, no matter whats returned

            cache[city] = data

            with open("cache.json", "w") as file:
                json.dump(cache, file, indent=2)
        
        else:
            print("Error, invalid city name.")
            
    
    except Exception as e:
        print(f"Error occured, {e}")

def display_weather(weather):
    city = weather["location"]["name"]
    region = weather["location"]["region"]
    country = weather["location"]["country"]
    localtime = weather["location"]["localtime"]

    condition = weather["current"]["condition"]["text"]
    temp_c = weather["current"]["temp_c"]
    temp_f = weather["current"]["temp_f"]
    feelslike_c = weather["current"]["feelslike_c"]
    humidity = weather["current"]["humidity"]
    wind_kph = weather["current"]["wind_kph"]
    wind_dir = weather["current"]["wind_dir"]

    print(f"\nCity: {city}, {region}, {country}")
    print(f"Local time: {localtime}")
    print(f"Condition: {condition}")
    print(f"Temperature: {temp_c} °C ({temp_f} °F)")
    print(f"Feels like: {feelslike_c} °C")
    print(f"Humidity: {humidity}%")
    print(f"Wind: {wind_kph} kph ({wind_dir})\n")



def load_cached_weather():
    # return contents of cache.json or {} if missing
    with open("cache.json", "r") as file:
        cache = json.load(file)
        return cache

def get_cached_city(cache, city):
    # return cache[city] if exists, else None
    return cache.get(city)

def list_cached_cities(cache):
    # print each city name from cache.keys()
    for city in cache:
        print(city)

def delete_cached_city(cache, city):
    # remove cache[city], overwrite cache.json
    if city in cache:
        del cache[city]
        with open("cache.json", "w") as file:
            json.dump(cache, file, indent =2)


def clear_cache():
    # overwrite cache.json with {}
    with open("cache.json", "w") as file:
        json.dump({}, file, indent=2)

def ensure_cache_file():
    # if cache.json doesn't exist, create with {}
    if not os.path.exists("cache.json"):
        with open("cache.json", "w") as file:
            json.dump({}, file, indent=2)
    


def validate_key():
    while True:
        key = input("Input your API key. ").strip()
        url = f"https://api.weatherapi.com/v1/current.json?key={key}&q=London"

        response = requests.get(url)

        if response.status_code == 200:
            return key
        else:
            print("Invalid API key, try again")

# Main menu and CLI
def main():
    ensure_cache_file()
    cache = load_cached_weather()
    key = validate_key()
    
    while True:
        print("\nWeather CLI")
        print("1. Get weather for city")
        print("2. View cached city weather")
        print("3. List all cached cities")
        print("4. Delete a cached city")
        print("5. Clear cache")
        print("6. Exit")

        choice = input("Select option: ").strip()

        if choice == "1":

            city = input("Enter the city name ").strip().lower()
            cached_city = get_cached_city(cache, city)

            if cached_city:
                print(cached_city)

            else:
                fetch_weather_data(cache, city, key)
                cache = load_cached_weather()
            

        elif choice == "2":

            city = input("Input city name ").strip().lower()
            if city in cache:
                weather = cache[city]
                display_weather(weather)
                
            else:
                print("City is not in cache")

        elif choice == "3":
            list_cached_cities(cache)

        elif choice == "4":
            
            city = input("Enter the cached city you would like to delete. ").lower().strip()

            if city in cache:
                delete_cached_city(cache,city)
                cache = load_cached_weather()
                
            else:
                print("City is not in cache.")


        elif choice == "5":
            clear_cache()
            cache = load_cached_weather()

        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
