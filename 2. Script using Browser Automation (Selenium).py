#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
import csv

def get_linkedin_data_browser(first_name, last_name):
    # Set up the WebDriver (make sure you have installed the appropriate driver for your browser)
    driver = webdriver.Chrome()

    # Navigate to LinkedIn
    driver.get('https://www.linkedin.com')

    # Implement login process if necessary
    # Fill in search fields and submit the form
    search_box = driver.find_element_by_name('keywords')
    search_box.send_keys(f'{first_name} {last_name}')
    search_box.submit()

    # Wait for search results to load
    # Extract relevant information from the first 5 results
    results = driver.find_elements_by_class_name('search-result')

    # Create a CSV file and write the results
    with open('linkedin_browser_results.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Title', 'Location', 'LinkedIn Profile']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for result in results[:5]:
            name = result.find_element_by_class_name('actor-name').text
            title = result.find_element_by_class_name('subline-level-1').text
            location = result.find_element_by_class_name('subline-level-2').text
            linkedin_profile = result.find_element_by_tag_name('a').get_attribute('href')
            
            writer.writerow({'Name': name, 'Title': title, 'Location': location, 'LinkedIn Profile': linkedin_profile})

    # Close the browser
    driver.quit()

# Call the function with the user's first and last name
#bget_linkedin_data_browser('First_Name', 'Last_Name')

