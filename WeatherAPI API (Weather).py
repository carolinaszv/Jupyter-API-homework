#!/usr/bin/env python
# coding: utf-8

# # WeatherAPI (Weather)
# 
# Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.
# 
# Be sure to take advantage of both the documentation and the API Explorer!
# 
# ## 0) Import any libraries you might need
# 
# - *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*
# - *Tip: Remember you only need to import requests once!*

# In[1]:


import requests


# In[ ]:





# ## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).
# 
# - *Tip: The URL we used in class was for a place near San Francisco. What was the format of the endpoint that made this happen?*
# - *Tip: Save the URL as a separate variable, and be sure to not have `[` and `]` inside.*
# - *Tip: How is north vs. south and east vs. west latitude/longitude represented? Is it the normal North/South/East/West?*
# - *Tip: You know it's JSON, but Python doesn't! Make sure you aren't trying to deal with plain text.* 
# - *Tip: Once you've imported the JSON into a variable, check the timezone's name to make sure it seems like it got the right part of the world!*

# In[2]:


medellin_url = "http://api.weatherapi.com/v1/current.json?key=0a92ef3bdeda43698a240620221506&q=Medellin&aqi=no"
response = requests.get(medellin_url)
medellin_data = response.json()


# In[ ]:





# In[ ]:





# ## 2) What's the current wind speed? How much warmer does it feel than it actually is?
# 
# - *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*
# - *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference.*

# In[7]:


print("The current wind speed in Medellin is", medellin_data['current']['wind_mph'],"mph.")


# In[8]:


medellin_current = medellin_data['current']['temp_f']
medellin_feelslike = medellin_data['current']['feelslike_f']

if medellin_feelslike > medellin_current:
    print(f"It feels {medellin_feelslike - medellin_current :.1f} degrees warmer.")
elif medellin_feelslike < medellin_current:
    print(f"It feels {medellin_current - medellin_feelslike :.1f} degrees colder.")
else:
    print("It feels exactly as it should.")


# In[ ]:





# ## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible tomorrow?
# 
# - *Tip: Check the documentation!*
# - *Tip: If you aren't sure what something means, ask in Slack*

# In[13]:


medellin_forecast_url = "http://api.weatherapi.com/v1/forecast.json?key=0a92ef3bdeda43698a240620221506&q=Medellin&days=3&aqi=no&alerts=no"
response = requests.get(medellin_forecast_url)
medellin_moon = response.json()


# In[14]:


print(medellin_moon['forecast']['forecastday'][1]['astro']['moon_illumination'], "percent of the moon will be visible tomorrow.")


# In[ ]:





# ## 4) What's the difference between the high and low temperatures for today?
# 
# - *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*

# In[11]:


print(f"The difference between the high and low temperatures for today is", round(medellin_moon['forecast']['forecastday'][0]['day']['maxtemp_f']-medellin_moon['forecast']['forecastday'][0]['day']['mintemp_f']))

#using round because I can't figure out f-string decimal place here :(


# In[ ]:





# ## 4.5) How can you avoid the "oh no I don't have the data any more because I made another request" problem in the future?
# 
# What variable(s) do you have to rename, and what would you rename them?

# In[12]:


print("I didn't have this problem, so I do not know how to answer this.")


# In[ ]:





# ## 5) Go through the daily forecasts, printing out the next three days' worth of predictions.
# 
# I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).
# 
# - *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*

# In[40]:


medellin_forecast = response.json()


# In[41]:


for forecast_high in medellin_forecast['forecast']['forecastday']:
    high_temp = forecast_high['day']['maxtemp_f']
    if high_temp >= 76:
        print("On", forecast_high['date'], "it's forecast to be a high of", high_temp, "degrees, which is hot in Carolina's world.")
    elif high_temp < 76:
        print("On", forecast_high['date'], "it's forecast to be a high of", high_temp, "degrees, which is nice & warm in Carolina's world.")
    elif high_temp > 64:
        print("On", forecast_high['date'], "it's forecast to be a high of", high_temp, "degrees, which is cold in Carolina's world.")


    


# In[ ]:





# ## 5b) The question above used to be an entire week, but not any more. Try to re-use the code above to print out seven days.
# 
# What happens? Can you figure out why it doesn't work?
# 
# * *Tip: it has to do with the reason you're using an API key - maybe take a look at the "Air Quality Data" introduction for a hint? If you can't figure it out right now, no worries.*

# In[42]:


medellin_forecast_url = "http://api.weatherapi.com/v1/forecast.json?key=0a92ef3bdeda43698a240620221506&q=Medellin&days=7&aqi=no&alerts=no"
response = requests.get(medellin_forecast_url)
medellin_forecast = response.json()


# In[43]:


for forecast_high in medellin_forecast['forecast']['forecastday']:
    high_temp = forecast_high['day']['maxtemp_f']
    if high_temp >= 76:
        print("On", forecast_high['date'], "it's forecast to be a high of", high_temp, "degrees, which is hot in Carolina's world.")
    elif high_temp < 76:
        print("On", forecast_high['date'], "it's forecast to be a high of", high_temp, "degrees, which is nice & warm in Carolina's world.")
    elif high_temp > 64:
        print("On", forecast_high['date'], "it's forecast to be a high of", high_temp, "degrees, which is cold in Carolina's world.")


# In[44]:


print("I changed the URL day up to 7 and did not work. My API Key shows that I have a free account, so I am limited to three days.")


# ## 6) What will be the hottest day in the next three days? What is the high temperature on that day?

# In[109]:


max_temp = 0

for forecast_high in medellin_forecast['forecast']['forecastday']:
    if forecast_high['day']['maxtemp_f'] > max_temp:
        max_temp = forecast_high['day']['maxtemp_f']
        max_day = forecast_high['date']
print(max_day, "will be the hottest day in the next three days with a high temperature of", highest_max_temp, "degrees.")


# In[108]:


#I don't know what I'm doing wrong here and there is no one available to help so I'm throwing in the towel.


# In[ ]:





# ## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?
# 
# I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say "{temperature} and cloudy" instead of just the temperature. 
# 
# - *Tip: You'll only need one day of forecast*

# In[78]:


miami_24hr_url = "http://api.weatherapi.com/v1/forecast.json?key=0a92ef3bdeda43698a240620221506&q=Miami, Florida&days=1&aqi=no&alerts=no"
response = requests.get(miami_24hr_url)
miami_24hr = response.json()


# In[100]:


print("Here's a look at how the weather will be for the next 24+ hours in Miami, Florida:")
for miami_hrs in miami_24hr['forecast']['forecastday']:
    for miami_wx in miami_hrs['hour']:
        time = miami_wx['time']
        temp = miami_wx['temp_f']
        cloud_cover = miami_wx['condition']['text']
        print("At",time,"it will be", temp, "degrees and",cloud_cover)


# In[ ]:





# ## 8) For the next 24-ish hours in Miami, what percent of the time is the temperature above 85 degrees?
# 
# - *Tip: You might want to read up on [looping patterns](http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/)*

# In[129]:


above_85 = 0
for miami_hrs in miami_24hr['forecast']['forecastday']:
    for miami_wx in miami_hrs['hour']:
        time = miami_wx['time']
        temp = miami_wx['temp_f']
        if temp > 85:
            above_85 = above_85 + 1
print("About",(above_85/24)*100, "percent of the next 24-ish hours will be above 85 degrees.")


# In[ ]:





# In[ ]:





# ## 9) How much will it cost if you need to use 1,500,000 API calls?
# 
# You are only allowed 1,000,000 API calls each month. If you were really bad at this homework or made some awful loops, WeatherAPI might shut down your free access. 
# 
# * *Tip: this involves looking somewhere that isn't the normal documentation.*

# In[ ]:


print("It would cost $4 a month to upgrade from the free 1,000,000 API calls to the next available tier of 2,000,000 API calls.")


# In[ ]:





# ## 10) You're too poor to spend more money! What else could you do instead of give them money?
# 
# * *Tip: I'm not endorsing being sneaky, but newsrooms and students are both generally poverty-stricken.*

# In[ ]:


print("You could pay with time by waiting until midnight on the 1st of the next month UTC for the quota to reset.")

