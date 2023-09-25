Welcome to this repository! 

I participated in my first triathlon with minimal training to see if I could overcome the challenge. I managed to finish the Alpe d'Huez medium-distance triathlon in 4 hours.

After obtaining the results table, I wanted to conduct a more detailed race analysis. To do this, I scraped the data from the website to manipulate them through a Jupyter notebook.

The first challenge was retrieving the data because the URL is static, and the data couldn't be obtained through a simple HTML parser with BeautifulSoup. So, I used Selenium, a Python package that allows me to retrieve the data and navigate the site by automatically clicking the next page button.

Next, I saved the data to a simple CSV file so that I could process the data in a notebook using the pandas, numpy, and matplotlib libraries.

But the work doesn't end there. Next year, I've registered for the long-distance edition. Therefore, I'll retrieve the data for the long-distance race to set time-related goals for each course, aiming to achieve the same standards as in the medium-distance triathlon.

Feel free to reach out if you have any questions about this repository.
