import scrapy
from scrapy import Request
from bs4 import BeautifulSoup
class Gitlab(scrapy.Spider):
    name = "gitlab"
    allowed_domains = ["puhuitech.cn"]
    COOKIE = {'remember_user_token':'W1s5MDZdLCIkMmEkMTAkem1sZy5odzZadVloaU1oT2kydzBMdSIsIjE1MDk3NTUzNzUuNTE2MjA4NiJd--d9576239966e4c8d802d0d3d249fdac7d5d3a84e'}
    headers = {
        'Connection': 'keep - alive',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }
    def start_requests(self):
	for i in self.gen_urls():
        	yield Request(i, callback=self.parse, cookies=self.COOKIE,headers=self.headers)
    def gen_urls(self):
	urslist=[]
	for i in range(1,43):
		starturl="http://gitlab.puhuitech.cn/search?group_id=&page=%d&project_id=&repository_ref=&search=a&utf8=%s" %(i,'%E2%9C%93')
		urslist.append(starturl)
	return urslist
    def parse(self, response):
        filename = response.url.split("/")[-2]
	html = response.body.decode("utf-8")
	soup = BeautifulSoup(html, 'html.parser')
	for i in  soup.find_all('a',class_='project'):
		
              	f=open(filename,'a+')
	      	f.write(str(i.get('href'))+'\n')
	      	f.close()


