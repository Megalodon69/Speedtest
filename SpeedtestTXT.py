import colorama
from colorama import Fore, Style
import datetime
import requests
import speedtest

colorama.init(autoreset=True)

#print(Fore.RED + """
#"                                                                                                                                                ,
#"                              |        |                                                                                                        ,
#"                              |\      /|                                                                                                        ,
#"                              | \____/ |                                                                                                        ,
#"                              |  /\/\  |                                                                                                        ,
#"                             .'___  ___`.                                                                                                       ,
#"                            /  \|/  \|/  \                                                                                                      ,
#"           _.--------------( ____ __ _____)                                                                                                     ,
#"        .-' \  -. | | | | | \ ----\/---- /                                                                                                      ,
#"      .'\  | | / \` | | | |  `.  -'`-  .'                                                                                                       ,
#"     /`  ` ` '/ / \ | | | | \  `------'\                                                                                                        ,
#"    /-  `-------.' `-----.       -----. `---.                                                                                                   ,
#"   (  / | | | |  )/ | | | )/ | | | | | ) | | )                                                                                                  ,
#"    `._________.'_____,,,/\_______,,,,/_,,,,/                                                                                                   ,
#"                                                                                                                                                ,
#""" + Style.RESET_ALL)

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
st.download(threads=10)
st.upload(threads=10)
ping = st.results.ping
server = best_server['host']
distance = round(best_server['d'] / 1000)

result_string = f"{now}\nDownload: {st.results.download / 1000000:.2f} Mbps\nUpload: {st.results.upload / 1000000:.2f} Mbps\nPing: {ping:.2f} ms\nIP Address: {ip_address}\nInternet Provider: {internet_provider}\nServer: {server} ({best_server['country']})\nDistance: {distance} km\n------------------------------\n\n"

with open('speedtest_results.txt', 'a') as f:
    f.write(result_string)

print("="*40)
print(f"Current Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"IP Address: {ip_address}")
print(f"Approximate Location: {approx_location}")
print(f"Internet Provider: {internet_provider}")
print(f"Server: {server} ({best_server['country']})")
print("="*40)
print(f"Download Speed: {st.results.download / 1000000:.2f} Mbps")
print(f"Upload Speed: {st.results.upload / 1000000:.2f} Mbps")
print(f"Ping: {ping:.2f} ms")
print("="*40)

print(result_string)
input("\nPress any key to close the script...")





