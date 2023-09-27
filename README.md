Welcome to this repository! 

I participated in my first triathlon with minimal training to see if I could overcome the challenge. I managed to finish the Alpe d'Huez medium-distance triathlon in 4 hours during 2023 summer.

After obtaining the results table, I wanted to conduct a more detailed race analysis. To do this, I scraped the data from the website to manipulate them through a Jupyter notebook and then package the whole thing. 

The first challenge was retrieving the data because the URL is static, and the data couldn't be obtained through a simple HTML parser with BeautifulSoup. So, I used Selenium, a Python package that allows me to retrieve the data and navigate the website pages by automatically clicking on the next page button.

After retrieving the raw data, I cleaned it to make it more usable on a large scale. Today, the program allows you to:
- Retrieve the data
- Clean the data
- Ask for the name of a participant and whether they want to provide a category or not
- Display the results for the participant and the overall averages or based on the category.

Here are my results: 

#################### Please find GINOUX Etienne results below ####################
Swim_time was 00:38:09 and the average Swim_time for M25-29 was 00:30:48
T1 was 00:14:01 and the average T1 for M25-29 was 00:04:20
Bike_time was 02:26:27 and the average Bike_time for M25-29 was 01:52:54
T2 was 00:03:59 and the average T2 for M25-29 was 00:02:17
Run_time was 00:40:46 and the average Run_time for M25-29 was 00:37:10
Time was 04:03:25 and the average Time for M25-29 was 03:07:33

Next challenge: long-distance triathlon in 2024!
