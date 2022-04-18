import urllib3 #pip install urllib3
import re
import pandas as pd #pip install pandas
#import certifi
http = urllib3.PoolManager()
url = 'https://www.metacritic.com/browse/movies/score/metascore/year/filtered?year_selected=2020&sort=desc&view=detailed'
resp = http.request('GET', url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'})
print(resp.status)
# Covert the results from raw bytes to text
datastring = str(resp.data, "utf-8")


#Title, 
titles = re.findall("class=\"title\"><h3>(.*?)<\/h3><\/a>", datastring)
#print(titles) 
# check if it succeded 

# Release date
release_date = re.findall("<span>(.*\d\d\d\d)<\/span>", datastring)
#print(release_date) 
# check if it succeded 

# Movie summary
movie_description = re.findall( "<div class=\"summary\">\n\s+(.*)", datastring)
#print(movie_description) 
# check if it succeded 

#Metascore
metascore =re.findall('<div class="metascore_w large movie positive">(.*?)<\/div>\n\s+<\/a>\n\s+<\/div>\n\s+<div class',datastring)
#print(metascore)

#URL Photo
thumbnail = re.findall('.*<img src="(.*)" alt=".* \/><\/a>',datastring)
#print(thumbnail) 
# check if it succeded 
df = pd.DataFrame(list(zip(titles, release_date, movie_description, metascore, thumbnail)), columns=['Title','Release Date', 'Metascore', 'Movie Description', 'Thumbnail photo URL'])
print(df)