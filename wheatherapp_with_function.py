"""'weatherapp.py' can find the condition of the weather
 and the temperature of the air from a given web site"""
import html
from urllib.request import urlopen, Request


def get_page_sourse(url):
    """ Function, that help get all code from web-site"""
    headers = {'User-Agent': 'Mozilla/5.0(X11; Fedora; Linux x86_64;)'}
    request = Request(url, headers=headers)
    page = urlopen(request).read()
    content = str(page.decode("utf-8"))
    return content


def get_weather_info(content, tags):
    """ Function, that passes through each of the given tags"""
    return[get_tag_content(content, tag) for tag in tags]


def get_tag_content(content, tag):
    """ Function that uses a specified tag to receive the required information
        the condition of the weather and the temperature of the air from a given web site"""
    tag_container, tag_info_weather = tag
    weather_tag_size = len(tag_info_weather)
    weather_tag_index = content.find(tag_info_weather, content.find(tag_container))
    weather_value_start = weather_tag_index + weather_tag_size
    weather = ''
    for char in content[weather_value_start:]:
        if char != "<":
            weather += char
        else:
            break
    return weather


def produce_output(name, temp, cond):
    """Function, that can display information, that were founded before"""
    return print(f'Temperature from {name} site: {html.unescape(temp)}\n'), \
           print(f'Condition of weather from {name} site: {html.unescape(cond)}\n')


def main():
    """ main function, where you can call up the required functions """
    accu_url = "https://www.accuweather.com/uk/ua/lviv/324561/weather-forecast/324561"
    accu_tags = (('<div class="temp">', '<span class="large-temp">'),
                 ('<div class="bg bg-c">', '<span class="cond">'))
    rp5_url = ("http://rp5.ua/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D1%83"
               "_%D0%9B%D1%8C%D0%B2%D0%BE%D0%B2%D1%96,"
               "_%D0%9B%D1%8C%D0%B2%D1%96%D0%B2%D1%81%D1%8C%D0%BA%D0%B0"
               "_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C")
    rp5_tags = (('<div id="ArchTemp">', '<span class="t_0" style="display: block;">'),
                ('<div class="ArchiveInfo">', '</span>, '))
    weather_site = {"AccuWeather": (accu_url, accu_tags), "RP5": (rp5_url, rp5_tags)}
    for name in weather_site:
        url, tags = weather_site[name]
        content = get_page_sourse(url)
        temp, condition = get_weather_info(content, tags)
        produce_output(name, temp, condition)


if __name__ == "__main__":
    main()
