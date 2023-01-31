from requests import get
from bs4 import BeautifulSoup
from rich import print

url = 'https://www.cbr.com/'
soup = BeautifulSoup(get(url).text, 'lxml')

# Get the featured articles
all_articles = soup.find('section', class_='w-featured-pinned-article').find_all('article')

# Loop through each article in the `all_articles` list and print the results
for article in all_articles:
    title = article.find('a', class_='bc-title-link')
    all_image_sources = article.find('picture').find_all('source')

    # Print the title, link, and image sources
    print(f'''
    [bold green]Title[/bold green]: [blue]{title.text.strip()}[/blue]
    [bold green]Link[/bold green]: [blue]https://www.cbr.com{title["href"]}[/blue]
    [bold green]Image sources[/bold green]:''')

    # Loop through each image source in the `all_image_sources` list and print the results
    for image_source in all_image_sources:
        print(f'''
        [bold yellow]Link[/bold yellow]: [blue]{image_source["srcset"]}[/blue]
        [bold yellow]Size[/bold yellow]: [red]{image_source["sizes"]}[/red]
        ''')