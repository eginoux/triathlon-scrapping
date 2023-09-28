Welcome to this repository!

I participated in my first triathlon with minimal training to see if I could overcome the challenge. I managed to finish the Alpe d'Huez medium-distance triathlon in 4 hours during 2023 summer : https://www.acn-timing.com/?lng=FR#/events/2141423449174261/ctx/20230725_alpehuez/generic/198021_2/home/TRI2

After obtaining the results table, I wanted to conduct a more detailed race analysis. To do this, I scraped the data from the website to manipulate them through a Jupyter notebook and then package the whole thing.

The first challenge was retrieving the data because the URL is static, and the data couldn't be obtained through a simple HTML parser with BeautifulSoup. So, I used Selenium, a Python package that allows me to retrieve the data and navigate the website pages by automatically clicking on the next page button.

After retrieving the raw data, I cleaned it to make it more usable on a large scale. Today, the program allows you to:
- Loading the data or get it from the web
- Clean the data
- Ask for the name of a participant and a category or not
- Display the results for the participant and averages / min / max overall or based on the category if specified

Here is the output of the main.py file:

Getting mens data from local directory ✅
<br/> Getting women data from local directory ✅
<br/> Enter a valid participant: [LASTNAME Name] GINOUX Etienne
<br/> Do you want to specify a category? [Y/n] n
<br/> ###################### Please find GINOUX Etienne results below ######################
<br/> Swim_time was 00:38:09 (average was 00:31:50, min was 00:17:22 and max was 00:58:39)
<br/> T1 was 00:14:01 (average was 00:04:17, min was 00:01:19 and max was 00:24:29)
<br/> Bike_time was 02:26:27 (average was 01:59:18, min was 01:08:58 and max was 03:13:29)
<br/> T2 was 00:03:59 (average was 00:02:21, min was 00:00:47 and max was 00:15:07)
<br/> Run_time was 00:40:46 (average was 00:39:58, min was 00:22:58 and max was 01:08:30)
<br/> Time was 04:03:25 (average was 03:17:49, min was 01:52:29 and max was 05:01:33)


Next challenge: long-distance triathlon in 2024!
