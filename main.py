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


def user_agent_handler(proxy_url):
	cj = cookielib.FileCookieJar("cookies")
	user_agent = urllib2.build_opener(
	urllib2.HTTPCookieProcessor(cj),
	urllib2.HTTPHandler(),
	urllib2.HTTPSHandler(),
	urllib2.ProxyHandler({'https': proxy_url,'http':proxy_url,'ftp':proxy_url}))
	user_agent.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:23.0) Gecko/20100101 Firefox/23.0')]
	return user_agent
	

def crawl_website(site_url,user_agent):
	content=urllib2.urlopen(site_url).read()
	print content






def main():
	print "Working"
	user_agent=user_agent_handler("http://172.30.0.10:3128")
	urllib2.install_opener(user_agent)
	crawl_website("https://www.google.co.in/robots.txt",user_agent)





if __name__=="__main__":
	main()
