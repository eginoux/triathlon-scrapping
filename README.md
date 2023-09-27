Welcome to this repository! 

I participated in my first triathlon with minimal training to see if I could overcome the challenge. I managed to finish the Alpe d'Huez medium-distance triathlon in 4 hours during 2023 summer : https://www.acn-timing.com/?lng=FR#/events/2141423449174261/ctx/20230725_alpehuez/generic/198021_2/home/TRI2

After obtaining the results table, I wanted to conduct a more detailed race analysis. To do this, I scraped the data from the website to manipulate them through a Jupyter notebook and then package the whole thing. 

The first challenge was retrieving the data because the URL is static, and the data couldn't be obtained through a simple HTML parser with BeautifulSoup. So, I used Selenium, a Python package that allows me to retrieve the data and navigate the website pages by automatically clicking on the next page button.

After retrieving the raw data, I cleaned it to make it more usable on a large scale. Today, the program allows you to:
- Retrieve the data
- Clean the data
- Ask for the name of a participant and whether they want to provide a category or not
- Display the results for the participant and the overall averages or based on the category.

Next challenge: long-distance triathlon in 2024!
