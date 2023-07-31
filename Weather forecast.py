response = requests.get(URL)
res = response.json()
print(res)
print()
print()
condition = res["weather"][0]["main"]
description = res["weather"][0]["description"]"""
from tkinter import *
import requests
import json
import datetime
from PIL import ImageTk
from PIL import Image
window=Tk()
window.title("Weather Forecast")
window.configure(background="white")
window.minsize(650,650) #width,height
window.maxsize(650,650)
window.geometry("300x300+50+50") #width x height + x + y
L0=Label(window,text="WELCOME TO MY WEATHER FORECAST",font=("bold",12),foreground="white",background="#BF3EFF",
         width=52,height=3)
L0.place(x=15,y=10)
L1=Label(window,text="Enter a city:",font=8,background="white",padx=50,pady=6)
L1.place(x=10,y=93)
search_bar_image=PhotoImage(file="search bar.png")
L4=Label(window,image=search_bar_image,width=250,height=50)
L4.place(x=240,y=85)
E1=Entry(window,bd=5,font=8,border=0,width=16)
E1.place(x=270,y=100)
E1.focus()


light=ImageTk.PhotoImage(Image.open("light_mode.jpg"))
L2=Label(image=light)
dark=ImageTk.PhotoImage(Image.open("dark_mode.jpg"))
L3=Label(image=dark)
switch_value=True
def toggle():
    global switch_value
    if switch_value == True:
        switch.config(image=dark,bg="#26242f",activebackground="#26242f")
        window.config(bg="#26242f")
        switch_value = False
        L1 = Label(window, text="Enter a city:", font=8, background="#26242f",foreground="white",padx=50, pady=6)
        L1.place(x=10, y=100)
    else:
        switch.config(image=light,bg="white",activebackground="white")
        window.config(bg="white")
        switch_value = True
        L1 = Label(window, text="Enter a city:", font=8, background="white",padx=50, pady=6)
        L1.place(x=10, y=100)
switch=Button(window,image=light,bd=0,bg="white",width=180,height=70,command=toggle)
switch.place(x=20,y=130)

#dates
dt=datetime.datetime.now()
date=Label(window,text=dt.strftime('%A'), bg='white', font=("bold", 15))
date.place(x=10,y=200)
month=Label(window,text=dt.strftime('%B'), bg='white', font=("bold", 15))
month.place(x=150,y=200)

#time
hour=Label(window,text=dt.strftime('%I : %M %p'),bg="white",font=("bold",15))
hour.place(x=10,y=230)

#MOON-SUN
if int((dt.strftime('%I'))) >= 8 & int((dt.strftime('%I'))) <= 5:
    img = ImageTk.PhotoImage(Image.open('moon.png'))
    panel = Label(window, image=img)
    panel.place(x=370,y=250)
else:
    img = ImageTk.PhotoImage(Image.open('sun.png'))
    panel = Label(window, image=img)
    panel.place(x=370,y=250)

def city_name():
    #API CALL
    api_key=(your private api key)
    api_request=requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                               +E1.get() + "&units=metric&appid="+api_key)
    api = json.loads(api_request.content)

    #Temperatures
    y = api['main']
    current_temperature=y['temp']
    humidity = y['humidity']
    tempmin = y['temp_min']
    tempmax = y['temp_max']

    #Coordinates
    x = api['coord']
    longtitude = x['lon']
    latitude = x['lat']

    #Country
    z = api['sys']
    country = z['country']
    city= api['name']

    #Adding the received info into the screen
    label_temp.configure(text=current_temperature)
    label_humidity.configure(text=humidity)
    max_temp.configure(text=tempmax)
    min_temp.configure(text=tempmin)
    label_lon.configure(text=longtitude)
    label_lat.configure(text=latitude)
    label_country.configure(text=country)
    label_city.configure(text=city)

#Search Bar and Button
city_nameButton=Button(window,text="Search",bg="white",command=city_name)
city_nameButton.grid(row=1,column=1,padx=505,pady=95,stick=W + E + N + S)

# Country  Names and Coordinates
label_city_1 = Label(window, text="City:", width=0,
                     bg='white', font=("bold", 15))
label_city_1.place(x=370,y=460)
label_city = Label(window, text="...", width=0,
                   bg='white', font=("bold", 15))
label_city.place(x=430, y=460)
label_country_1 = Label(window, text="Country:", width=0,
                        bg='white', font=("bold", 15))
label_country_1.place(x=370,y=500)
label_country = Label(window, text="...", width=0,
                      bg='white', font=("bold", 15))
label_country.place(x=470, y=500)

longtitude = Label(window, text="Longtitude:",width=0,
                   bg='white',font=("bold",15))
longtitude.place(x=370,y=540)
label_lon = Label(window, text="...", width=0,
                  bg='white', font=("Helvetica", 15))
label_lon.place(x=500, y=540)
latitude = Label(window, text="Latitude:", width=0,
                 bg='white', font=("bold", 15))
latitude.place(x=370, y=580)
label_lat = Label(window, text="...", width=0,
                  bg='white', font=("Helvetica", 15))
label_lat.place(x=470, y=580)

# Current Temperature

label_temp = Label(window, text="...", width=0, bg='white',
                   font=("Helvetica", 70), fg='black')
label_temp.place(x=20, y=280)

# Other temperature details

humi = Label(window, text="Humidity: ", width=0,
             bg='white', font=("bold", 15))
humi.place(x=10, y=450)

label_humidity = Label(window, text="...", width=0,
                       bg='white', font=("bold", 15))
label_humidity.place(x=120, y=450)

maxi = Label(window, text="Max. Temp.: ", width=0,
             bg='white', font=("bold", 15))
maxi.place(x=10, y=510)

max_temp = Label(window, text="...", width=0,
                 bg='white', font=("bold", 15))
max_temp.place(x=150, y=510)

mini = Label(window, text="Min. Temp.: ", width=0,
             bg='white', font=("bold", 15))
mini.place(x=10, y=570)

min_temp = Label(window, text="...", width=0,
                 bg='white', font=("bold", 15))
min_temp.place(x=150, y=570)



window.mainloop()
