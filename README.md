## CBR Scraper
This is a simple scraper for the [CBR](https://www.cbr.com/) website.

It is written in Python and uses the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library for parsing HTML and the [Requests](https://requests.readthedocs.io/en/master/) library for making HTTP requests.

In addition, it uses the [Rich](https://github.com/textualize/rich/blob/master/README.md) library for displaying the results in a nice way.

### Usage
The scraper uses the Poetry package manager to manage dependencies. To install the dependencies, run `poetry install`.

And to run the scraper, run `poetry run python main.py`.

The scraper does not take any user input. It will scrape all the featured articles on CBR and display the results in the terminal.