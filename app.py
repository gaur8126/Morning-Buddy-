import streamlit as st 
import random 
from application import temperature_of_city, news_summarizer, get_news, smart_planner_
# Page Configuration 


# Helper functions 

def get_random_quote():
    quotes = [
        "The sun is daily reminder that we too can rise again from the darkness, that we too can shine our own light.",
        "Write it on your heart that every day is the best day in the year",
        "I get up every morning and It's going to be a great day. Your never know when it's going to be over, so I refuse to have a bad day.",
        "Today's goals: Coffee and kindness. Maybe two coffees, and then kindness.",
        "An early-morning walk is a blessing for the whole day.",
        "Morning is an important time of day because how you spend your morning can often tell you what kind of day you are going to have",
        "Lose an hour in the morning, and you will spend all day looking for it.",
        "When you arise in the morning, think of what a precious privilage it is to be alive - to breathe, to think, to enjoy, to love."
    ]

    return random.choice(quotes)

def get_random_image():
    image_urls = [
        "https://images.pexels.com/photos/34540915/pexels-photo-34540915.jpeg",
        "https://images.pexels.com/photos/34524183/pexels-photo-34524183.jpeg",
        "https://images.pexels.com/photos/34557438/pexels-photo-34557438.jpeg",
        "https://images.pexels.com/photos/34540443/pexels-photo-34540443.jpeg",
        "https://images.pexels.com/photos/34532056/pexels-photo-34532056.jpeg",
        "https://images.pexels.com/photos/34524677/pexels-photo-34524677.jpeg"
    ]

    return random.choice(image_urls)


# Page Definitions 

def home_page():
    """Display the home page with a quote and image."""
    st.title("😊 Your Morning Buddy")
    st.markdown("---")
    st.subheader("A thought for your day")
    st.info(f"{get_random_quote()}")
    st.image(get_random_image(), caption = "A beautiful morning to start your day", use_container_width = True)
    st.markdown("---")
    st.write("Use the sidebar on the left to get your daily updates!")


def weather_news_page():
    """Display the page for getting weather and news by city."""
    st.header("Get Weather of the city")
    city = st.text_input("Enter your city name:")
    if st.button("Fetch Information"):
        if city:
            temperature_output = temperature_of_city(city)
            st.subheader(f"Weather Info: {temperature_output}")
            st.success("Weather feached successfully!!!")
        else:
            st.error("Please enter a city name.")

def interest_news_page(): 
    """Display the page for getting news by interest"""
    st.header("Get News Based on Your Interest")
    interest = st.text_input("Enter your area of interest (e.g., Technology, sports, Health):","Technology")

    if st.button("Fetch News"):
        if interest:
            articles = get_news(interest)
            title = []
            url = []
            image_url = []

            for i in articles:
                title.append(i['title'])
                url.append(i['url'])
                image_url.append(i['urlToImage'])

            if not articles:
                st.error("No news found.")

            col1,col2,col3,col4,col5 = st.columns(5)
            with col1:
                st.subheader(title[0])
                st.markdown("---")
                st.image(image_url[0])
                st.markdown("---")
                st.write("Read full article here.",url[0])
                st.markdown("---")
                st.write(news_summarizer(url[0]))
            with col2:
                st.subheader(title[1])
                st.markdown("---")
                st.image(image_url[1])
                st.markdown("---")
                st.write("Read full article here.",url[1])
                st.markdown("---")
                st.write(news_summarizer(url[1]))
            with col3:
                st.subheader(title[2])
                st.markdown("---")
                st.image(image_url[2])
                st.markdown("---")
                st.write("Read full article here.",url[2])
                st.markdown("---")
                st.write(news_summarizer(url[2]))
            with col4:
                st.subheader(title[3])
                st.markdown("---")
                st.image(image_url[3])
                st.markdown("---")
                st.write("Read full article here.",url[3])
                st.markdown("---")
                st.write(news_summarizer(url[3]))
            with col5:
                st.subheader(title[4])
                st.markdown("---")
                st.image(image_url[4])
                st.markdown("---")
                st.write("Read full article here.",url[4])
                st.markdown("---")
                st.write(news_summarizer(url[4]))

        else:
            st.error("Please select your area of interest")


def smart_planner():
    """Display the page for viewing the day's schedule"""
    st.header("Your smart Planner Day")
    city = st.text_input("Enter your city name:")
    if st.button("Let's Plan"):
        if city:
            smart_plan = smart_planner_(city)
            st.subheader(smart_plan)
            st.success("Have a nice day")

        else:
            st.error("Please enter a city name.")


# Sidebar Navigation

st.sidebar.title("Navigation")
st.sidebar.markdown("---")
page_option = st.sidebar.radio("Choose a page:",("Home","Get Weather of your City","News by Interest","Smart Planner"))
st.sidebar.markdown("---")


# Page Routing 
if page_option == "Home":
    home_page()
elif page_option == "Get Weather of your City":
    weather_news_page()
elif page_option == "News by Interest":
    interest_news_page()
elif page_option == "Smart Planner":
    smart_planner()