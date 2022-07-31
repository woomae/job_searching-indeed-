import csv
from save import extract_indeed_pages
from save import extract_job
from encodings import utf_8

def make_csv(jobs):
  file = open("jobs.csv",mode="w",encoding="utf_8")
  writer = csv.writer(file)
  writer.writerow(["title","company","location","job_id"])
  for job in jobs:
    writer.writerow(list(job.values()))
  return

done_csv = extract_job(extract_indeed_pages())
make_csv(done_csv)