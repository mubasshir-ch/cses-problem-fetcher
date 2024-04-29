from bs4 import BeautifulSoup as bs
import requests

url = 'https://cses.fi/problemset/'

response = requests.get(url)
soup = bs(response.text, 'html.parser')

content = soup.find('div', class_='content')

cnt = 1
tot = 0
general_done = False

url_len = len("https://cses.fi/problemset/task/1234")

hyphen_len = 80
for child in content.children:
    if child.name == "h2":
        title = f"{child.text}"
        if "General" in title:
            continue
        if(len(title) % 2):
            title += " "
        spaces = (hyphen_len - len(title)) // 2
        print("-" * hyphen_len)
        print(" " * spaces +  title + " " * spaces)
        print("-" * hyphen_len)
    if child.name == "ul":
        if not general_done:
             general_done = True
             continue
        li_tags = child.find_all('li')
        for li in li_tags:
                a_tag = li.find('a')
                pre_space = " " if cnt < 10 else ""
                problem_title = f"{pre_space}{cnt}. {a_tag.text}"
                spaces = hyphen_len - len(problem_title) - url_len
                print( problem_title + " " * spaces+  f"https://cses.fi{a_tag['href']}")
                cnt += 1
                tot += 1
        cnt = 1

print(f"Total problems: {tot}")
