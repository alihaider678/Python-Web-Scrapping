from bs4 import BeautifulSoup
import requests
import csv

# Get HTML code from Website
source = requests.get('https://coreyms.com/').text

soup = BeautifulSoup(source, 'lxml')

#print(soup.prettify())

# Get first Article of website
article = soup.find('article')
#print(article.prettify())

# Get title of article 1
header = article.h2.a.text
#print(header)

# Get Summary(when get specific class then use find method)
summary = article.find('div', class_='entry-content').p.text
#print(summary)

# Get video source(iframe complete link)
vid_src = article.find('iframe', class_='youtube-player')
#print(vid_src)

# Get link of embeded video
vid_src = article.find('iframe', class_='youtube-player')['src']
#print(vid_src)

# Parse the link/grab the link for check that what's the Id of link
vid_src = article.find('iframe', class_='youtube-player')['src']
vid_id = vid_src.split('/')
#print(vid_id) # our url broken into list several parts

# Now we know that the id of video and now split with question mark(?) for more clerify
vid_src = article.find('iframe', class_='youtube-player')['src']
vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]
#print(vid_id) # This will the actually video link.

# Get video link from article
yt_link = f'https://youtube.com/watch?v={vid_id}'
#print(yt_link)




# Now we find all articles data soo let try.
source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')

# Get CSV file
csv_file = open('cms_scrape.csv', 'w')

# pass csv file 
csv_writer = csv.writer(csv_file)

# Now we want the header of csv file (basically this is column name)
csv_writer.writerow(['headline', 'summary', 'video_link'])


for article in soup.find_all('article'):
	try:
		header = article.h2.a.text
		print(header)
		
		summary = article.find('div', class_='entry-content').p.text
		print(summary)
		
		vid_src = article.find('iframe', class_='youtube-player')['src']
		
		vid_id = vid_src.split('/')[4]
		vid_id = vid_id.split('?')[0]
		
		yt_link = f'https://youtube.com/watch?v={vid_id}'
		print(yt_link)

		print()

		# we can pass the value here in list
		csv_writer.writerow([header, summary, yt_link])

	except Exception as E:
		print(None)
csv_file.close()
