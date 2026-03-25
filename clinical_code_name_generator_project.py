print("WELCOME the Clinical Study Code Name Generator")

import random

hospital = input("Enter a hospital or Institude name: ").strip()
focus = input("Enter the medical speciality or research focus: ").strip()

hospital_code = hospital[:3].upper()
focus_code = focus[:3].upper()

number = random.randint(100,999)

print(f"Your Cliniccal project codename could be:  {hospital}-{focus}-2026-{number}")





