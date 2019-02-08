import html
from urllib.request import urlopen
Example_webscraping = "http://example.webscraping.com"
example_page = urlopen(Example_webscraping).read()
example_page = str(example_page)
print(example_page)


list_of_countries = []
Example_scraping_country_tag = 'png" />'
while Example_scraping_country_tag in example_page:
    example__scraping_country_size = len(Example_scraping_country_tag)
    example_scraping_country_tag_index = example_page.find(Example_scraping_country_tag)
    example_scraping_country_value_start = example_scraping_country_tag_index + example__scraping_country_size
    example_temp = ""
    for char in example_page[example_scraping_country_value_start:]:
        if char != '-' and char != '<':
            example_temp += char
        else:
            break
    list_of_countries.append(example_temp)
    all_text_before_country = example_scraping_country_value_start + len(example_temp)
    example_page = example_page[all_text_before_country:]
print(f'All countries from site:{list_of_countries}\n')