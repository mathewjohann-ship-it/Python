import requests
from colorama import Fore, Style
import random

url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

def get_random_technology_fact():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        lst = [Fore.LIGHTCYAN_EX, Fore.YELLOW, Fore.GREEN, Fore.LIGHTMAGENTA_EX]
        print(random.choice(lst)+f"Did you know? {fact_data['text']}")
    else:
        print(Fore.RED+"Failed to fetch fact")


while True:
    user_input = input(Fore.BLUE+"Press Enter to get a random technology fact or type 'q' to quit...")
    if user_input.lower() == 'q':
        break
    get_random_technology_fact()