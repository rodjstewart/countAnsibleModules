#!/usr/bin/python3
# countAnisbleModuels.py - Opens the ansible modules list page and counts them

import requests, bs4, logging

logging.basicConfig(filename='countAnsibleModulesLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

print('Counting...') # display text while counting the modules
res = requests.get('https://docs.ansible.com/ansible/latest/modules/list_of_all_modules.html')
res.raise_for_status

# Retrieve the page
soup = bs4.BeautifulSoup(res.text, "html.parser")


# Find the right list
modLinks = soup.find('ul', class_='simple').findChildren(recursive=False)

# Count the number of modules
counter = 0

for link in modLinks:
    counter += 1
    logging.info(f'link: {link}')

logging.info('There are ' + str(counter) + ' modules listed')
print('There are ' + str(counter) + ' modules listed')
