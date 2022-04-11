import requests

url = 'https://delhihighcourt.nic.in/'
response = requests.get(url)
st_code =  response.status_code
print(st_code)
if st_code == 200:
    print('valid URL go Ahead !')
    payload = {
    'juddt':'11%2F03%2F2022' #modify the date here
    }
    # juddt=11%2F03%2F2022&Submit=Submit #Form data raw
    source_url = f'http://164.100.69.66/jsearch/juddt1page.php?dc=31&fflag=1'
    session = requests.session()
    r = requests.post(source_url, data=payload, allow_redirects=True)
    print(r)
    out_url = r.url
    rsp = requests.get(out_url)

else:
    print('Response Error!')
