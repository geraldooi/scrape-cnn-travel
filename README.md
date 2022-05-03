# Web scraper to get news article content

This is a very simple side project by using Pyhton programming language.

This project was inspired by [DevProjects](https://www.codementor.io/projects/tool/web-scraper-to-get-news-article-content-atx32d46qe).

## Introduction

We want to build a simple web scraper that will return the content of a news article when given a specific URL. Some examples of real products which use similar technologies include price-tracking websites and SEO audit tools which may scrape top search results. This project may take you around 4 to 8 hours to complete.

## Requirements

Choose one news website - see article examples below for inspiration. Given a specific article URL from the website of your choice, return the title and content of the article to the user.

Examples article URLs:

- [New York Times](https://www.nytimes.com/2020/09/02/opinion/remote-learning-coronavirus.html)
- [Washington Post](https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/)
- [CNN](https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html) <-- I choose this
- [Reuters](https://www.reuters.com/article/us-health-coronavirus-global-deaths/global-coronavirus-deaths-pass-agonizing-milestone-of-1-million-idUSKBN26K08Y)

**For an extra challenge:** Parse out information such as the article title, updated date, and byline to return separately to the user.

## Limitation

Only the article from [CNN Travel](https://edition.cnn.com/travel) can be scraped by this python script. This is due to the class name used by other CNN news category are different.

## Future Work

Expand to other News categories by implementing URL checking to get which category the News belong to.

## To run the code

```bash
python scrape_cnn.py <news_url>
```

or

```bash
python scrape_cnn.py
```
