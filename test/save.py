from turtle import title
import requests as re
from bs4 import BeautifulSoup as bs

LIMIT = 20
URL =f"https://kr.indeed.com/jobs?q=Python&limit={LIMIT}&fromage=3"

def ext_something(html):
  title = html.find("h2","jobTitle").find("a").find("span")["title"]
  company = html.find("span",{"class":"companyName"}).string
  location = str(html.find("div",{"class":"companyLocation"}).text)
  job_id = html.find("h2",{"class":"jobTitle"}).find("a")["data-jk"]
  return {"title":title, "company":company, "location":location,"link": f"https://www/indeed.com/viewjob?jk={job_id}"}

def extract_indeed_pages():
  result = re.get(URL)
  soup = bs(result.text, "html.parser")
  pagination = soup.find("div",{"class":"pagination"})
  links = pagination.find_all('a')
  pages=[]
  for link in links[:-1]:
    pages.append(int(link.string))
  max_page = pages[-1]
  return max_page

def extract_job(last_page):
  jobs =[]
  for page in range(last_page):
    print(f"Scrapping page {page}")
    result = re.get(f"{URL}&start = {page*LIMIT}")
    soup = bs(result.text, "html.parser")
    results = soup.find_all("div", "cardOutline")
  for result in results:
    job = ext_something(result)
    jobs.append(job)
  return jobs