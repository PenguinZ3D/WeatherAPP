import tkinter as tk
from app import search

#initiate gui
window = tk.Tk();
window.title("Weather APP") #Title of program
window.geometry('500x500') #Window size on startup
window.config(bg="#1f5a87")

#Title
title = tk.Label(window, text="Enter the state and city below", font=("Arial", 16), fg="white", bg="#1f5a87") #Establish label
title.pack(padx=20, pady=30) #show label on screen

#State
state_label = tk.Label(window, text="State:", font=("Arial", 30), fg="white", bg="#1f5a87")
state_entry = tk.Entry(window, width=5, justify='center', font=("Arial", 10))

state_label.pack()
state_entry.pack(padx=15,pady=20)


#City
city_label = tk.Label(window, text="City:", font=("Arial", 30), fg="white", bg="#1f5a87")
city_entry = tk.Entry(window, width=15, justify='center', font=("Arial", 10))

city_label.pack()
city_entry.pack(padx=15,pady=20)

#Results
temp_result = tk.Label(window, text="Temperature: ___", font=("Arial", 30), fg="white", bg="#1f5a87")
temp_result.pack(pady=10)

cond_result = tk.Label(window, text="Conditions: ___", font=("Arial", 30), fg="white", bg="#1f5a87")
cond_result.pack(pady=10)



def weather():
    state_data = state_entry.get()
    city_data = city_entry.get()
    
    temperature = search(state_data, city_data)[0]
    condition = search(state_data, city_data)[1]

    temp_result.config(text=f"Temperature: {temperature}°F")
    cond_result.config(text=f"Conditions: {condition}")



#Submit
submit = tk.Button(window, text="Submit", relief="solid", command=weather, bg="red", fg="white")
submit.pack()



tk.mainloop() #set main loop