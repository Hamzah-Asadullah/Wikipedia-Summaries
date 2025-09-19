from mediawiki import MediaWiki
from time import time
from json import dumps

def safe_content(input: str) -> bool:
    return (input.find("Israel") == -1)

wp = MediaWiki()
titles: list[str] = [ "Pakistan" ]
data: dict[str, str] = {}

def save_data():
    with open("data.json", "w") as w:
        w.write(dumps(data))

i: int = 0
for title in titles:
    try:
        page = wp.page(title)
        summary: str = page.summary
        links: list[str] = page.links

        data[title] = summary
        for link in links:
            if (link not in titles) and safe_content(link):
                titles.append(link)
    except:
        continue
    i += 1
    print(f">> {i} pages processed.", end='\r')

    if (i % 1000) == 0:
        save_data()