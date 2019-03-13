import html
from urllib.request import urlopen, Request


def get_page_sourse(URL):
    headers = {'User-Agent':'Mozilla/5.0(X11; Fedora; Linux x86_64;)'}
    request = Request(URL, headers=headers)
    page = urlopen(request).read()
    content = str(page.decode("utf-8"))
    return (content)


def get_weather_info(content,tags):
    return([get_tag_content(content,tag) for tag in tags])
def get_tag_content(content, tag):
    tag_container, tag_about_weather = tag
    weather_tag_size = len(tag_about_weather)
    weather_tag_index = content.find(tag_about_weather, content.find(tag_container))
    weather_value_start = weather_tag_index + weather_tag_size
    weather = ''
    for char in content[weather_value_start:]:
        if char != "<":
            weather += char
        else:
            break
    return(weather)


def produce_output(name,temp, cond):
    return(print(f'Temperature from {name} site: {html.unescape(temp)}\n'),
            print(f"Condition of weather from {name} site :{html.unescape(cond)}\n"))


def main():
    ACCU_URL = "https://www.accuweather.com/uk/ua/lviv/324561/weather-forecast/324561"
    ACCU_TAGS = (('<div class="temp">','<span class="large-temp">'), ('<div class="bg bg-c">','<span class="cond">'))
    RP5_URL = ("http://rp5.ua/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D1%83_%D0%9B%D1%8C%D0%B2%D0%BE%D0%B2%D1%96,"
                "_%D0%9B%D1%8C%D0%B2%D1%96%D0%B2%D1%81%D1%8C%D0%BA%D0%B0_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C")
    RP5_TAGS = (('<div id="ArchTemp">','<span class="t_0" style="display: block;">'),('<div class="ArchiveInfo">', '<span class="t_1" style="display: none;">+45 °F</span>,'))
    weather_site = {"AccuWeather":(ACCU_URL, ACCU_TAGS),"RP5":(RP5_URL, RP5_TAGS) }
    for name in weather_site:
        url , tags = weather_site[name]
        contant = get_page_sourse(url)
        temp, condition  = get_weather_info(contant, tags)
        produce_output(name, temp, condition)
if __name__ == "__main__":
    main()
