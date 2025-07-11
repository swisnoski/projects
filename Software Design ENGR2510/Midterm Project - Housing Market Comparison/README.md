# Project Summary: 
This project aims to answer the question: "How does the housing market vary across the United States with regards to the largest city in each state?". To answer this question, we are looking at sale listing data provided by RentCast. We are using RentCast's API to generate data from the largest city of each state, and then creating heatmaps and scatterplots based on the variation of price, age, and size of the homes. To reduce unwanted variation, we are focusing specifically on single family homes with two bedrooms. 

# Instructions: 
### Setting Up a RentCast API Key: 
This project requires a RentCast API Key. Follow the instructions below to recieve your key. The instructions are repeated in the computational essay. 

RentCast which is a real estate analysis tool that can be found at https://www.rentcast.io/api. RentCast provides access to an API that allows us to access public sales listings. With this API you can make up to fifty inquiries a month free of charge, with each inquiry providing up to five-hundred data points.
To access the API: 
- Click on the header labeled "API".
- Click "Start for Free". This should take you to the API dashboard which will prompt you to log in. 
- Follow the directions to make an account, unlocking your API dashboard. However, in order to use an API key, you need to sign up for a plan. 
- At the bottom of the page click "select plan", and select the developer plan. This plan is REQUIRED, but it is also FREE OF CHARGE. In order to sign up, you will have to provide credit card information. We promise that you will not be charged, even if you forget to cancel the subscription, since the plan is entirely free. 
- Once you have activated your plan, scroll up to the API keys module. 
- On the right of the module there is a plus sign with Create API Key next to it. This will create your API key and prompt you to label it. 

Now you have successfully created an active API key and can begin to make inquiries. Running the get_fifty_states_data() function will use all of your free inquiries, SO ONLY RUN THE FUNCTION ONCE. If you run the file more than once, you WILL be charged 0.20$ per additional inquiry. If you need to make more than 50 inquiries, you can sign up for a second, third, or fourth account. Importantly, you can use a fake or even non-existent email to sign up for RentCast.

## Running Our Project: 
Once you have your API key, you are ready to run our project. Follow the steps below to recreate our visualizations: 
- Open the computational essay. 
- Run the autoreload box at the top of the essay. 
- Under the "Acquiring Cities" portion of our essay, replace the string "your_api_key_here" with your api_key as a string. This should be the only time you use your API key.
- Run the box that includes the get_fifty_states_data() function. If you created your API correctly, you should see each state abbreviation followed by the status code 200. 
- Replace your API key string with "your_api_key_here" to avoid calling the function again
- Run the rest of the boxes in the essay in order. These boxes, in this order, should:
    1. Import the needed visualization functions 
    2. Create a heatmap of price 
    3. Create a heatmap of square footage
    4. Create a heatmaps of year built 
    5. Create a scatter plot of year built vs. price 
    6. Create a scatter plot of square footage vs. price
    7. Create a scatter plot of year built vs. square footage

# Project Requirement:
Our project has the following the requirements as outlined in requirements.txt:
- colorspacious~=1.1.2
- geopandas~=0.14.2
- matplotlib~=3.7.2
- numpy~=1.24.3
- pandas~=2.0.3
- Requests~=2.31.0
- seaborn~=0.13.2
- Shapely~=2.0.3