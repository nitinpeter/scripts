import bs4pyt
from fpdf import FPDF

start_url = requests.get('http://mayavistory.blogspot.com/')
images=[]
soup=bs4.BeautifulSoup(start_url.text, 'lxml')
#all_images = soup.findAll('div',class_='separator')
for a in soup.find_all('a', href=True):
  url = a['href']
  filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
  print(filename)
  if filename:
    images.append(filename.group(1))
	with open('output/%s'%filename.group(1),'wb') as f:
	  if 'http' not in url:
	    # image source can be relative
		url = '{}{}'.format(site,url)
      response = requests.get(url)
	  f.write(response.content)
	  
pdf = FPDF()
for image in images:
  pdf.add_page()
  pdf.image(image)
pdf.output("output/comic_file.pdf","F")

	    