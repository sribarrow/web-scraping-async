import requests
from bs4 import BeautifulSoup
import time

def get_session()->requests.Session:
    return requests.Session()

def get_data(n: int, sess: requests.Session) -> str:
    url = f"https://scrapethissite.com/pages/forms/?page_num={n}"
    r = sess.get(url)
    sp = BeautifulSoup(r.text, 'html.parser')
    # print(sp)
    return sp.title.text

if __name__ == "__main__":
    title_dict ={}
    s = get_session()
    start = time.perf_counter()
    for x in range(1,1000):
        title_dict[x]= get_data(x, s)
    end = time.perf_counter()
    print(title_dict)
    print(f"Time taken to run 10 iterarions = {end-start}")
    # Time taken to run 10 iterarions = 8.415007823 -- with session
    # Time taken to run 10 iterarions = 4.303393053000001 -- without session
    # Time taken to run 10 iterarions = 36.035149024 -- async 
    # 1000 -> Time taken to run 10 iterarions = 326.719981334