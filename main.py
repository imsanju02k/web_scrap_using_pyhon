import datetime as datetime

import form as form
import requests
import json
from datetime import datetime, timedelta

today = datetime.today()
today
(today)

pin = ['110001']

num_day = 7
all_dates = []
for i in range(num_day):
    all_dates.append(today + timedelta(i))
(all_dates)
final_dates = []
for i in all_dates:
    final_dates.append(i.strftime("%d%m%y"))
print(final_dates)

while True:
    for p in pin:
        for d in final_dates:
            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(
                p, d)
            result = requests.get(URL)
            # print(result.text)
            json_result = result.json()
            # print(json_result)

            if json_result["centers"]:
                for center in json_result["centers"]:
                    for session in center["sessions"]:
                        if(session['available_capacity']>0):
                                print("pincode:" + p)
                                print("dates: " + d)
                                print("Center Name: ", center['name'])
                                print("Center Address ", center['address'])
                                print("no of vaccine", session['available_capacity'])
                                print("Vaccine Type", session['vaccine'])
                                print("\n")
