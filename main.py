import json
import os

#This is a simple weather CLI that makes use of API's to return what your looking for. 
#Also caches results to a json for offline lookups and to use less API calls


#Core functions

def fetch_weather_data(city):
    pass  # call API, return parsed dict

def display_weather(data):
    pass  # show weather cleanly in terminal

def save_weather(data, city):
    pass  # save to cache.json using city as key

def load_cached_weather():
    pass  # read cache.json if it exists

def get_cached_city(data, city):
    pass  # return city weather if it’s in cache

def list_cached_cities(data):
    pass  # print all city names in cache

def delete_cached_city(data, city):
    pass  # remove one city, overwrite cache

def clear_cache():
    pass  # empty the cache.json file

def ensure_cache_file():
    pass  # create empty cache file if missing





# Main menu and CLI
def main():
    ensure_cache_file()
    cache = load_cached_weather()

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
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        else:
            pass


if __name__ == "__main__":
    main()
