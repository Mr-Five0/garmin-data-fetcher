from garminconnect import (
    Garmin,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
    GarminConnectAuthenticationError
)
import json
from datetime import date, timedelta
import dotenv
import os

dotenv.load_dotenv()

email = os.getenv("email")
password = os.getenv("password")

try:
    client = Garmin(email, password)
    client.login()
    
    today = date.today().isoformat()
    #yesterday = (date.today() - timedelta(days=1)).isoformat()
    
    today_summary = client.get_stats(today)
    heart_rate = client.get_heart_rates(today)
    steps = client.get_steps_data(today)

    # print(today_summary)
    # print(heart_rate)
    # print(steps)
    
    with open(f"summary-{today}.json", "w", encoding="utf-8") as f:
        json.dump(today_summary, f, ensure_ascii=False, indent=2)
        print(f"Summary data saved to summary-{today}.json")
        
    with open(f"heart_rate-{today}.json", "w", encoding="utf-8") as f:
        json.dump(heart_rate, f, ensure_ascii=False, indent=2)
        print(f"Heart rate data saved to heart_rate-{today}.json")
        
    with open(f"steps-{today}.json", "w", encoding="utf-8") as f:
        json.dump(steps, f, ensure_ascii=False, indent=2)
        print(f"Steps data saved to steps-{today}.json")

except GarminConnectAuthenticationError:
    print("Authentication Error, check your email or password.")
except GarminConnectConnectionError:
    print("Connection Error, failed to connect to Garmin Connect.")
except GarminConnectTooManyRequestsError:
    print("Too many requests. Please try again later.")
except Exception as err:
    print(f"Other error occurred: {err}")
