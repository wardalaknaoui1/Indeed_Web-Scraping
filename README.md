# Indeed_Web-Scraping

                                    
This code is for scraping Indeed using Beautiful soup and requests. If you are looking for a specific job, this notebook will be so helpful in saving time.
I have customized this code for a Business Analyst role in Tulsa, OK. After running the code, a CSV file file named results will downloaded on your C drive. 
For a better experience, I recommend running these codes on your local machine.

If you think you spotted an error or have a question about this code, please feel free to make a pull request against my repository.


What is Web Scraping?(1)

Web scraping refers to the extraction of data from a website. This information is collected and then exported into a format that is more useful for the user. Be it a spreadsheet or an API.
Although web scraping can be done manually, in most cases, automated tools are preferred when scraping web data as they can be less costly and work at a faster rate.
But in most cases, web scraping is not a simple task. Websites come in many shapes and forms, as a result, web scrapers vary in functionality and features.
How do Web Scrapers Work?

Automated web scrapers work in a rather simple but also complex way. After all, websites are built for humans to understand, not machines.
First, the web scraper will be given one or more URLs to load before scraping. The scraper then loads the entire HTML code for the page in question. More advanced scrapers will render the entire website, including CSS and Javascript elements.
Then the scraper will either extract all the data on the page or specific data selected by the user before the project is run.
Ideally, the user will go through the process of selecting the specific data they want from the page. For example, you might want to scrape an Amazon product page for prices and models but are not necessarily interested in product reviews.
Lastly, the web scraper will output all the data that has been collected into a format that is more useful to the user.

Most web scrapers will output data to a CSV or Excel spreadsheet, while more advanced scrapers will support other formats such as JSON which can be used for an API.

(1): https://www.parsehub.com/blog/what-is-web-scraping/
