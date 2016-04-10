#encoding:utf-8
import Queue
import io
import time
import requests
from  multiprocessing import Pool

def scan(filepath):
    x ='http://aq609.com'
    job_url = x+str.strip(filepath)
    res = requests.get(job_url,timeout=3)
    if((res.status_code == 200) or (res.status_code == 302) or (res.status_code == 403)):
        result = '[+]Found '+job_url + " " + str(res.status_code)
        print result
    return job_url

if __name__ == '__main__':
    start = time.time()
    # s = ['/robots.txt\n', '/admin/index.php\n', '/index.html\n', '/login.php\n', '/index.php\n']
    # print s

    with open('filepath.txt') as f:
            catalog=f.readlines()
    f.close()
   # print catalog
    p = Pool(4)
    p.map(scan,catalog)
    end = time.time()
    print 'use: %.2f s' % (end - start)


