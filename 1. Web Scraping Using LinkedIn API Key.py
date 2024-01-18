#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import csv

def get_linkedin_data(api_key, first_name, last_name):
    # Obtain an access token using your LinkedIn API key

    # Make a request to the LinkedIn API to search for users
    search_url = f'https://api.linkedin.com/v2/people-search?q={first_name} {last_name}'
    headers = {
        'Authorization': f'Bearer {your_access_token}'
    }
    
    response = requests.get(search_url, headers=headers)
    data = response.json()

    # Process the data and extract relevant information
    results = data.get('elements', [])
    
    # Create a CSV file and write the results
    with open('linkedin_api_results.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Title', 'Location', 'LinkedIn Profile']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for result in results[:5]:
            name = f"{result.get('firstName', '')} {result.get('lastName', '')}"
            title = result.get('headline', '')
            location = result.get('location', {}).get('preferredGeoPlaceName', '')
            linkedin_profile = f"https://www.linkedin.com/in/{result.get('publicIdentifier', '')}"
            
            writer.writerow({'Name': name, 'Title': title, 'Location': location, 'LinkedIn Profile': linkedin_profile})

# Call the function with your API key and user's first and last name
#get_linkedin_data('your_api_key', 'First_Name', 'Last_Name')

