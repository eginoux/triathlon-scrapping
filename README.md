Welcome to this repository!

I participated in my first triathlon with minimal training to see if I could overcome the challenge. I managed to finish the Alpe d'Huez medium-distance triathlon in 4 hours during 2023 summer : https://www.acn-timing.com/?lng=FR#/events/2141423449174261/ctx/20230725_alpehuez/generic/198021_2/home/TRI2

After obtaining the results table, I wanted to conduct a more detailed race analysis. To do this, I scraped the data from the website to manipulate them through a Jupyter notebook and then package the whole thing.

The first challenge was retrieving the data because the URL is static, and the data couldn't be obtained through a simple HTML parser with BeautifulSoup. So, I used Selenium, a Python package that allows me to retrieve the data and navigate the website pages by automatically clicking on the next page button.

After retrieving the raw data, I cleaned it to make it more usable on a large scale. Today, the program allows you to:
- Retrieve the data
- Clean the data
- Ask for the name of a participant and whether they want to provide a category or not
- Display the results for the participant and the overall averages or based on the category.

Here is the output of the main.py file:

Getting mens data from local directory ✅
<br/> "Getting women data from local directory ✅
<br/> Enter a valid participant: [LASTNAME Name] GINOUX Etienne
<br/> Do you want to specify a category? [Y/n] n
<br/> ########## Please find GINOUX Etienne results below ##########
<br/> Swim_time was 00:38:09 (average was 00:31:50)
<br/> T1 was 00:14:01 (average was 00:04:17)
<br/> Bike_time was 02:26:27 (average was 01:59:18)
<br/> T2 was 00:03:59 (average was 00:02:21)
<br/> Run_time was 00:40:46 (average was 00:39:58)
<br/> Time was 04:03:25 (average was 03:17:49)"


Next challenge: long-distance triathlon in 2024!
