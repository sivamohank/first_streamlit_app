
import streamlit
import pandas
import requests
import snowflake.connector


streamlit.title("My parents New Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#data is present in csv file so reading file using pandas read_csv
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#setting fruits as index
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))



if fruits_selected:
  fruits_to_show = my_fruit_list.loc[fruits_selected]
else:
    fruits_to_show = my_fruit_list


# Display the table on the page.
streamlit.dataframe(fruits_to_show)

import requests
streamlit.header("Fruityvice Fruit Advice!")
# fruityvice_response = requests. get("https://fruityvice.com/api/fruit/watermelon")
# # streamlit.text(fruityvice_response.json())
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it the screen as a table
streamlit.dataframe(fruityvice_normalized)

# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)

my_cnx = snowflake.connector.connect(**streamlit.secrets[ "snowflake" ])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit. header("The fruit load list contains:")
streamlit.dataframe(my_data_row)

# streamlit.text("")
add_my_friut=streamlit.text_input("What fruit would you like to add?")
my_data_row.append(add_my_friut)
streamlit.write("Thanks for adding ", add_my_friut)
# my_cur.execute("insert into fruit_load_list values('from streamlit')")
