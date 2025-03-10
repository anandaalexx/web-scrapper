import requests
import xlwt
from xlwt import Workbook
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

BASE_URL = 'https://remoteok.com/api/'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
REQUEST_HEADER = {
    'User_Agent': USER_AGENT,
    'Accept_Language': 'en-US, en;q=0.5', 
}

def get_job_postings():
    url = "https://remoteok.io/api" 
    headers = {"User-Agent": "Mozilla/5.0"} 
    
    res = requests.get(url, headers=headers)

    print(f"Status Code: {res.status_code}")
    print(f"Response Text: {res.text[:500]}") 

    if res.status_code != 200:
        raise Exception(f"Error: API mengembalikan status {res.status_code}")
    
    try:
        return res.json()
    except requests.exceptions.JSONDecodeError:
        raise Exception("Error: Respons API bukan JSON yang valid")

if __name__ == "__main__":
    json = get_job_postings()[1]
    print(json)