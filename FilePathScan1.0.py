#coding:utf-8
import requests
import getopt
import sys

def FilePathScan(url):
    try:
        with open('filepath.txt','r') as readfile:
            try:
                 with open('result.txt','a') as writefile:
                    for filepath in readfile.readlines():
                        job_url = url + filepath.strip()
                        resp = requests.get(job_url,timeout=8)
                        if (resp.status_code == 200) or (resp.status_code == 302 or (resp.status_code == 403)):
                            writefile.writelines('\r'+"[+]FOUND "+job_url)
            finally:
                writefile.close()
    finally:
        readfile.close()

if __name__ == "__main__":
    site =sys.argv[1:]
    xxx = sys.argv[0:]
    args ="".join(site)
    if len(args) < 1:
        print 'FilePathScan.py http://test.com'
    else:
        FilePathScan(args)
