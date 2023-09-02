import colorama
from colorama import Fore, Style
import datetime
import requests
import speedtest
import json

colorama.init(autoreset=True)

ip_response = requests.get('https://ipapi.co/json/')
ip_data = ip_response.json()
approx_location = f"{ip_data['city']}, {ip_data['region']}, {ip_data['country_name']}"
ip_address = ip_data['ip']
internet_provider = ip_data['org']
now = datetime.datetime.now()
st = speedtest.Speedtest()

print("Finding best server...")
best_server = st.get_best_server()

print(f"Best server found: {best_server['host']} ({best_server['country']})\n")

print("Starting speedtest...")
st.download(threads=12)
st.upload(threads=12)
ping = st.results.ping
server = best_server['host']
distance = round(best_server['d'] / 1000)

result_data = {
    "date_time": now.strftime('%Y-%m-%d %H:%M:%S'),
    "ip_address": ip_address,
    "approx_location": approx_location,
    "internet_provider": internet_provider,
    "server": server,
    "country": best_server['country'],
    "download_speed": round(st.results.download / 1000000, 2),
    "upload_speed": round(st.results.upload / 1000000, 2),
    "ping": round(ping, 2),
}

result_string = json.dumps(result_data, indent=4)

with open('speedtest_results.json', 'a') as f:
    f.write(result_string)

print("="*40)
print(f"Current Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"IP Address: {ip_address}")
print(f"Approximate Location: {approx_location}")
print(f"Internet Provider: {internet_provider}")
print(f"Server: {server} ({best_server['country']})")
print("="*40)
print(f"Download Speed: {round(st.results.download / 1000000, 2)} Mbps")
print(f"Upload Speed: {round(st.results.upload / 1000000, 2)} Mbps")
print(f"Ping: {round(ping, 2)} ms")
print("="*40)

print(result_string)
input("\nPress any key to close the script...")

