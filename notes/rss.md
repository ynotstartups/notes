# RSS

I found myself constantly checking several websites to get information.

For example,

Every Monday, I check [barbican cinema website](https://www.barbican.org.uk/whats-on/cinema) because the cinema ticket is only £6 on Monday.

If I want to check if there are new art exhibitions, I use [timeout](https://www.timeout.com/london/art/top-10-art-exhibitions-in-london) .

I go on [Hacker News](https://news.ycombinator.com/), however I only visit links with a large amount of comments.

...

This habit makes me wonder is there a way I can automate this.

Funny enough, this is what my employer Lyst is trying to solve. Instead of users going to different retailer site to shop or compare, users can just go to Lyst and get the best price.

Turns out [RSS](https://en.wikipedia.org/wiki/RSS) is designed just for this purpose, basically, you can consider RSS is like Lyst but for the internet, or a twitter which can follow anything on the internet.

## RSS Feed Example

See below for an example RSS feed, RSS uses xml and it is super simple.

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
 <title>RSS Title</title>
 <description>This is an example of an RSS feed</description>
 <link>http://www.example.com/main.html</link>

 <item>
  <title>Example entry</title>
  <description>Here is some text containing an interesting description.</description>
  <link>http://www.example.com/blog/post/1</link>
 </item>

</channel>
</rss>
```

## RSS Client

To interactive with RSS feeds, you will need a RSS client, e.g. [feedly](https://feedly.com/) is a popular a web based client.

I use a terminal based client called [newsboat](https://newsboat.org/releases/2.27/docs/newsboat.html#_introduction).

To subscribe to new RSS feeds, I add rss url to a file called `~/.newsboat/urls`.

e.g.

```
# Github Engineering Blog
http://githubengineering.com/atom.xml tech

# News with more than 200 comments from Hacker News
https://hnrss.org/newest?comments=200 tech news
```

The most amazing thing of newsboat is that it can take the output of a [program](https://newsboat.org/releases/2.27/docs/newsboat.html#_scripts_and_filters_snownews_extensions) as a RSS feed.

See below for example of using python web scraping to generate RSS feed.

## Some learnings after started using RSS feed

- Did you know you can subscribe to a specific playlist instead of a whole channel, why didn't youtube provide this functionality?
- Little python scripting can save me so much time and effort, the return of investment for these scripts are super high.
- I can finally keep track of the different engineering blogs, github's engineering blog, or individual bloggers.
- Turns out Podcasts are always distributed using RSS!

## Conclusion

RSS is so simple yet elegant and super powerful, a simple script can save you so much time and effort.

## Getting Barbican's Monday Movie Example

```python
from dataclasses import dataclass


@dataclass
class RSSItemData:
    title: str
    url: str
    description: str


@dataclass
class RSS:
    title: str
    url: str
    description: str
    items: list[RSSItemData]

    def __str__(self):
        rss_response = ""
        rss_response += '<?xml version="1.0" encoding="UTF-8"?>\n'
        rss_response += '<rss version="2.0">\n'
        rss_response += "<channel>\n"
        rss_response += f"<title>{self.title}</title>\n"
        rss_response += f"  <link>{self.url}</link>\n"
        rss_response += f"  <description>{self.description}</description>\n"
        for item in self.items:
            rss_response += "  <item>\n"
            rss_response += f"   <title>{item.title}</title>\n"
            rss_response += f"   <link>{item.url}</link>\n"
            rss_response += f"   <description>{item.description}</description>\n"
            rss_response += f"   <guid>{item.url}</guid>\n"
            rss_response += "  </item>\n"
        rss_response += "</channel>\n"
        rss_response += "</rss>\n"
        rss_response += "\n"
        return rss_response
```

```python
#!/usr/bin/env python3
import re
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import urllib.parse

from rss import RSSItemData, RSS

CHANNEL_TITLE = "£6 Monday Movies In Barbican Cinema"
CHANNEL_URL = "https://www.barbican.org.uk/whats-on?af%5B16%5D=16"

date_today = datetime.now().date()
days_ahead = 0 - date_today.weekday()
next_monday_date = date_today + timedelta(days_ahead)

next_monday_movies_url = (
    CHANNEL_URL
    + "&calendar_ranges%5B1%5D=1&dates%5Bmin%5D={}&dates%5Bmax%5D={}".format(
        next_monday_date, next_monday_date
    )
)

# Parse html
response = requests.get(CHANNEL_URL)
soup = BeautifulSoup(response.content, features="html.parser")

movies = soup.find_all(class_="search-listing__details")

movie_data = []
for movie in movies:
    title = movie.find(class_="listing-title").string
    url = "https://www.barbican.org.uk" + movie.find("a")["href"]
    movie_data.append(
        {
            "url": url,
            "title": title,
        }
    )

# Construct Rss feed
items = [
    RSSItemData(
        title=f'{next_monday_date} {data["title"]}',
        url=data["url"],
        description="",
    )
    for data in movie_data
]
rss = RSS(
    title=CHANNEL_TITLE,
    url=CHANNEL_URL,
    description="",
    items=items,
)
print(rss)
```

## Random RSS Feed Example

- News such as TechCrunch, Economist...
- Software releases such as mypy, django...
- it service status, slack system status, new relic status...
