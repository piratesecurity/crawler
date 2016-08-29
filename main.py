"""
This is Main Program for Customized webcrawler
Author: Bharath Ambati
Email : gowtamsecure@gmail.com
Date  : 28/08/16

"""

import urllib
import urllib2
import threading
import cookielib

all_websites=[]
no_of_threads=100

def user_agent_handler(proxy_url):
	cj = cookielib.FileCookieJar("cookies")
	user_agent = urllib2.build_opener(
	urllib2.HTTPCookieProcessor(cj),
	urllib2.HTTPHandler(),
	urllib2.HTTPSHandler(),
	urllib2.ProxyHandler({'https': proxy_url,'http':proxy_url,'ftp':proxy_url}))
	user_agent.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:23.0) Gecko/20100101 Firefox/23.0')]
	return user_agent
	
def read_website_urls(file):
	fd=open(file,"r")
	contents=fd.read().split("\n")
	for line in contents:
		line_split=line.split("	")
		try:
			all_websites.append("https://"+line_split[2]+"/robots.txt")
		except:
			pass
	
	fd.close()
	#print all_websites	


def crawl_website(site_urls,user_agent):
	for site_url in site_urls:	
		try:		
			content=urllib2.urlopen(site_url).read()
			write_file="data/"+site_url.split("/")[2]+".txt"
			print write_file
			print site_url
			wfd=open(write_file,"wc")
			wfd.write(content)
			wfd.close()
			#print content
		except:                            # if https failed then try http protocol
			print "-----------Site Failed-------------\n"
			print site_url
			if site_url[4]=='s':       # checking https connection or not
				site_url="http://"+site_url.split("//")[1]
				site_urls.append(site_url)
			
			print "+++++++++++End+++++++++++++++++++++\n"






def main():
	#print "Working"
	read_website_urls("top_500.txt")
	user_agent=user_agent_handler("http://172.30.0.22:3128")
	urllib2.install_opener(user_agent)
	all_threads=[]
	for no in range(0,no_of_threads):
		t=threading.Thread(target=crawl_website,args=(all_websites[50*(no-1):no*50],user_agent,))
		t.start()
	for thread in all_threads:
		thread.join()




if __name__=="__main__":
	main()

