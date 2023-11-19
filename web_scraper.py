import mechanicalsoup

# Create a MechanicalSoup browser
browser = mechanicalsoup.Browser()

# Define the URL of the website you want to scrape
login_url = 'https://example.com/login'
dashboard_url = 'https://example.com/dashboard'

# Create a dictionary with your login credentials
login_data = {'username': 'your_username', 'password': 'your_password'}

# Open the login page and submit the login form
login_page = browser.get(login_url)
login_form = login_page.soup.select('form')[0]
for key, value in login_data.items():
    login_form.find('input', {'name': key})['value'] = value

# Submit the form
response = browser.submit(login_form, login_page.url)

# Check if the login was successful
if response.ok:
    print("Login successful!")

    # Now, navigate to the dashboard page and scrape data
    dashboard_page = browser.get(dashboard_url)

    # Example: Extract some information from the dashboard page
    data = dashboard_page.soup.select('.dashboard-data')
    for item in data:
        print(item.text)
else:
    print("Login failed.")

