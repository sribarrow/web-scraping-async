# import requests
from bs4 import BeautifulSoup
import aiohttp
import asyncio
import time
import logging

async def main() -> None:
    title_dict ={}
    tasks = []
    start = time.perf_counter()
    async def get_data(session, url):
        try:
            async with session.get(url) as response:
                resp = await response.text()
                return resp, url
        except Exception as e_get_data:
            logging.error(e_get_data)
            
            
    async with aiohttp.ClientSession() as session:
        for page in range(1,1000):
            url = f"https://scrapethissite.com/pages/forms/?page_num={page}"
            tasks.append(get_data(session, url))
        htmls = await asyncio.gather(*tasks)
        # async with session.get(url) as response:
        #     # print(response.text())
        #     resp = await response.text()
        #     sp = BeautifulSoup(resp, 'html.parser')
        #     title_dict[page] = sp.title.text
        for html in htmls:
            sp = BeautifulSoup(html[0], "html.parser")
            title_dict[html[1]] = sp.title.text
    end = time.perf_counter()
    print(title_dict)
    print(f"Time taken to run this program - {end-start}")
    # 50 -> Time taken to run this program - 5.374581828
    # 100 -> Time taken to run this program - 35.876141149
    
   

if __name__ == "__main__":
    # https://stackoverflow.com/questions/13825278/python-request-with-authentication-access-token
    asyncio.run(main())
    