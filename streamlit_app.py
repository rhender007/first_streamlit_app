import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        # streamlit.text("insert into fruit_load_list values ('" + new_fruit + " ')")
        my_cur.execute("insert into fruit_load_list values ('" + new_fruit + " ')")
        
        return "Thanks for adding " + new_fruit


# my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
# my_data_row = my_cur.fetchone()

# streamlit.dataframe(my_data_row)


streamlit.title("My Parents New Healthy Diner")

streamlit.header("Breakfast Menu")
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

# New section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
      
except URLError as e:
    streamlit.error()
      
# streamlit.write('The user entered ', fruit_choice)


# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_rows = my_cur.fetchall()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_rows)

# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_rows = my_cur.fetchall()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_rows)

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

streamlit.header("The fruit load list contains:")
#Snowflake related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()
    
# Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.text(my_data_rows)


    

    
    
#     streamlit.header("Add a Fruit!")
# try:
#     fruit_choice = streamlit.text_input('Add a fruit here')
#     if not fruit_choice:
#       streamlit.error("Please select a fruit to add.")
#     else:
#         back_from_function = get_fruityvice_data(fruit_choice)
#         streamlit.dataframe(back_from_function)
      
# except URLError as e:
#     streamlit.error()



# Add a button to insert the fruit
#if streamlit.button('Add fruit'):
    # my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    # debug stop here for now
    #streamlit.stop()
    #fruit_add = streamlit.text_input('What fruit would you like added?')
    #insert_row_snowflake(new_fruit)
    #streamlit.write('Thanks for adding ', new_fruit)
    
try:
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    new_fruit = streamlit.text_input('What fruit would you like to add?')
    if not new_fruit:
        streamlit.error("Please provide a fruit to add.")
    else:
        resp = insert_row_snowflake(new_fruit)
        streamlit.text(resp)
except URLError as e:
    streamlit.error()
    
# TODO: fix this insert
# my_cur.execute("insert into fruit_load_list values ('from streamlit')")

