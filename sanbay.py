from requests import Request, Session
import csv

login_url = 'https://www.shanbay.com/api/v1/account/login/web/'
get_familiar_words = 'https://www.shanbay.com/api/v1/bdc/library/familiar/?page=%s&_=1493170715107'
get_master_words = 'https://www.shanbay.com/api/v1/bdc/library/master/?page=%s&_=1493170715107'

s = Session()
req = Request('PUT',  login_url, data= {"username":"yourname@host.com","password":"******"})

prepped = s.prepare_request(req)

resp = s.send(prepped)

print(resp.text)

#home = s.prepare_request(Request('GET', 'https://www.shanbay.com/'))
with open('master_words.csv', 'w') as csvfile:
    fieldnames = ['content', 'definition']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')

    writer.writeheader()

    for i in range(1, 280):

        print('get page : %s' % i)
        learn_resp = s.send(s.prepare_request(Request('GET', get_master_words % i)))
        resp_words = learn_resp.json()

        for w in resp_words["data"]["objects"]:
            w['definition'] = w['definition'].replace('\n','').replace('\r','')
            #writer.writerow(w)
            print('%s   %s' % (w['content'],w['definition']))
