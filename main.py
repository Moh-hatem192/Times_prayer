import requests 

def fetch_prayer_time(city, country):
    url = f'http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2'
    try:
        response = requests.get(url)
        info = response.json()
        if 'data' in info:
            timings = info['data']['timings']
            return timings
        else:
            return None
    except Exception as e:
        return f'Unexcpected error occured {e}'

city = input('enter your city: ')
country = input('enter your country: ')
if city and country:
    prayer_times = fetch_prayer_time(city, country)
    for prayer, time in prayer_times.items():
        print(f'{prayer}: {time}')
else:
    print('Unable to fetch prayer times')        
