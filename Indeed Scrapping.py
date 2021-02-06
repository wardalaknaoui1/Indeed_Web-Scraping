#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
from random import random
from time import sleep
from email.message import EmailMessage
from collections import namedtuple
import smtplib
import csv


# In[2]:


Template= "https://www.indeed.com/jobs?q={}&l={}"


# In[3]:


def get_url(position, location):
    template = "https://www.indeed.com/jobs?q={}&l={}"
    url = template.format(position, location)
    return url


# In[4]:


url= get_url("Data Analyst", "Tulsa ok")


# In[5]:


response= requests.get(url)


# In[6]:


response


# In[7]:


response.reason


# In[8]:


def collect_job_cards_from_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.find_all('div', 'jobsearch-SerpJobCard')
    return cards, soup


# In[9]:


soup = BeautifulSoup(response.text, 'html.parser')


# In[10]:


cards = soup.find_all('div', 'jobsearch-SerpJobCard')


# In[11]:


def collect_job_cards_from_page(html):
    
    
    return cards, soup


# In[12]:


card= cards[0]


# In[13]:


atag= card.h2.a


# In[14]:


job_title= atag.get("title")


# In[15]:


atag.get('href')


# In[16]:


job_url= 'https://www.indeed.com' + atag.get('href')


# In[17]:


company= card.find('span', 'company').text.strip()


# In[18]:


job_location= card.find('div', 'recJobLoc').get('data-rc-loc')


# In[19]:


job_summary= card.find('div', 'summary').text.strip()


# In[20]:


post_date= card.find('span', 'date').text


# In[21]:


from datetime import datetime


# In[22]:


today= datetime.today().strftime('%Y-%m-%d')


# In[23]:


try:
    job_Salary= card.find('span', 'SalaryText').text
except AttributeError:
    job_salary = ''


# In[24]:


def get_record(card):
    atag= card.h2.a
    job_title= atag.get("title")
    job_url= 'https://www.indeed.com' + atag.get('href')
    company= card.find('span', 'company').text.strip()
    job_location= card.find('div', 'recJobLoc').get('data-rc-loc')
    job_summary= card.find('div', 'summary').text.strip()
    post_date= card.find('span', 'date').text
    today= datetime.today().strftime('%Y-%m-%d')
    try:
        job_Salary= card.find('span', 'SalaryText').text
    except AttributeError:
        job_salary = ''
    record= (job_title, company, job_location, post_date, today, job_summary, job_salary, job_url )
    return record


# In[25]:


records = []
for card in cards:
    record = get_record(card)
    records.append(record)
    


# In[26]:


records[0]


# In[27]:


url= soup.find('a', {'aria-label': 'Next'})


# In[28]:


while True:
    try:
        url= 'https://www.indeed.com' + soup.find('a', {'aria-label': 'Next'}).get('href')
    except AttributeError:
        break
    response= requests.get(url)
    soup= BeautifulSoup(response.text, 'html.parser')
    cards= soup.find_all('div', 'jobsearch-SerpJobCard')
    for card in cards:
        record = get_record(card)
        records.append(record)


# In[29]:


len(records)


# In[30]:


def main(position, location):
    records=[]
    url


# In[31]:


from bs4 import BeautifulSoup
import requests
from random import random
from time import sleep
from email.message import EmailMessage
from collections import namedtuple
import smtplib
import csv
def get_url(position, location):
    template = "https://www.indeed.com/jobs?q={}&l={}"
    url = template.format(position, location)
    return url
def get_record(card):
    atag= card.h2.a
    job_title= atag.get("title")
    job_url= 'https://www.indeed.com' + atag.get('href')
    company= card.find('span', 'company').text.strip()
    job_location= card.find('div', 'recJobLoc').get('data-rc-loc')
    job_summary= card.find('div', 'summary').text.strip()
    post_date= card.find('span', 'date').text
    today= datetime.today().strftime('%Y-%m-%d')
    try:
        job_Salary= card.find('span', 'SalaryText').text
    except AttributeError:
        job_salary = ''
    record= (job_title, company, job_location, post_date, today, job_summary, job_salary, job_url )
    return record
def main(position, location):
    records=[]
    url= get_url(position, location)
    while True:
        response= requests.get(url)
        soup= BeautifulSoup(response.text, 'html.parser')
        cards= soup.find_all('div', 'jobsearch-SerpJobCard')
        for card in cards:
            record = get_record(card)
            records.append(record)
        try:
            url= 'https://www.indeed.com' + soup.find('a', {'aria-label': 'Next'}).get('href')
        except AttributeError:
            break
# Save the job data
    with open('results.csv', 'w', newline= '', encoding='utf-8') as f:
        writer= csv.writer(f)
        writer.writerow(['JobTitle', 'company', 'location', 'postDate', 'ExtractDate', 'Summary', 'Salary', 'JobUrl'])
        writer.writerows(records)


# In[32]:


# Run the main program
main('business analyst', 'Tulsa Ok')


# In[33]:


pwd


# In[ ]:




