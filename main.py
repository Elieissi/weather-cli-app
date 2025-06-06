import json
import os
import requests

#This is a simple weather CLI that makes use of API's to return what your looking for. 
#Also caches results to a json for offline lookups and to use less API calls


#Core functions

def fetch_weather_data(city, key):
    # build API request with city and key
    # send request, parse JSON, return dict
    pass

def display_weather(weather):
    # extract and print weather info cleanly
    pass

def save_weather(cache, city):
    # update cache[city], write entire dict to cache.json
    pass

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
    




# Main menu and CLI
def main():
    ensure_cache_file()
    cache = load_cached_weather()
    while True:
        
        key = input("Input your API key.").strip()
        url = f"https://api.weatherapi.com/v1/current.json?key={key}&q=London"

        response = requests.get(url)

        if response.status_code == 200:
            break
        else:
            print("Invalid API key, try again")
    
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
            pass

        elif choice == "2":
            city = input("Input city name").strip().lower()
            if city in cache:
                weather = cache[city]
                display_weather(weather)
                
            else:
                input("City is not in cache")

        elif choice == "3":
            list_cached_cities(cache)

        elif choice == "4":
            
            city = input("Enter the cached city you would like to delete.").lower().strip()
            if city in cache:
                delete_cached_city(cache,city)
                
            else:
                print("City is not in cache.")


        elif choice == "5":
            clear_cache()

        elif choice == "6":
            pass
        else:
            pass


if __name__ == "__main__":
    main()
