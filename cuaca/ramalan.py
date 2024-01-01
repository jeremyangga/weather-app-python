# from os import times
# from urllib import response
import requests
import json

api_url = "https://cuaca-gempa-rest-api.vercel.app/weather/"

def get_weather_report(nama_provinsi, nama_kota):
    nama_provinsi_url = nama_provinsi.lower()
    nama_provinsi_url = nama_provinsi_url.replace(' ','-')
    nama_kota_url = nama_kota.lower()
    nama_kota_url = nama_kota_url.replace(' ','-')
    response = requests.get(api_url+nama_provinsi_url+'/'+nama_kota_url)

    data_json = json.loads(response.text)
    if data_json['success'] == False:
        print("Kota tidak ditemukan")
    else:
        data_weather = data_json['data']
        detail_data_weather  = data_weather['params']
        humid = detail_data_weather[0]
        temperature = detail_data_weather[5]
        weather = detail_data_weather[6]

        #ambil semua times dari kelembapan
        raw_times_humid = []
        for i in humid['times']:
            raw_times_humid.append(i['datetime'])
        
        #pecah times
        times_humid = []
        for i in range(3,len(raw_times_humid)):
            times_humid.append(raw_times_humid[i])
        
        year = []
        month = []
        day = []
        minutes = []
        hours = []

        for h in range(len(times_humid)):
            splittime = times_humid[h]
            temp_year = []
            temp_month = []
            temp_day = []
            temp_hours = []
            temp_minutes = []
            for i in range(len(splittime)):
                # print(i,splittime[i])
                if i <= 3:
                    temp_year.append(splittime[i])
                elif i >= 4 and i <= 5:
                    temp_month.append(splittime[i])
                elif i >= 6 and i <= 7:
                    temp_day.append(splittime[i])
                elif i >= 8 and i <= 9:
                    temp_hours.append(splittime[i])
                elif i >= 10 and i <= 11:
                    temp_minutes.append(splittime[i])
 
            str_year = "".join(temp_year)
            str_month = "".join(temp_month)
            str_day = "".join(temp_day)
            str_hours = "".join(temp_hours)
            str_minutes = "".join(temp_minutes)
            year.append(str_year)
            month.append(str_month)
            day.append(str_day)
            hours.append(str_hours)
            minutes.append(str_minutes)

        # print(year)
        # print(month)
        # print(day)
        # print(hours)
        # print(minutes)
               
        #print(times_humid)

        #ambil nilai dari kelembapan
        raw_values_humid = []
        for i in humid['times']:
            raw_values_humid.append(i['value'])

        #pecah nilai kelembapan
        values_humid = []
        for i in range(3,len(raw_values_humid)):
            values_humid.append(raw_values_humid[i])

        #ambil nilai dari temperatur
        raw_values_temperature = []
        for i in temperature['times']:
            raw_values_temperature.append(i['celcius'])
        
        #pecah nilai temperature
        values_temperature = []
        for i in range(3, len(raw_values_temperature)):
            values_temperature.append(raw_values_temperature[i])
        
        #ambil nilai dari cuaca
        raw_values_weather = []
        for i in weather['times']:
            raw_values_weather.append(i['name'])
        
        #pecah nilai cuaca
        values_weather = []
        for i in range(3, len(raw_values_weather)):
            values_weather.append(raw_values_weather[i])
 
        
        print("\nRamalan Cuaca di "+nama_kota)
        print("==================================")
        for i in range(len(values_weather)):
            print("Tanggal: "+day[i]+"-"+month[i]+"-"+year[i])
            print("Jam: "+hours[i]+":"+minutes[i])
            print("Suhu: "+values_temperature[i])
            print("Cuaca: "+values_weather[i])
            print("------------------------------")

        