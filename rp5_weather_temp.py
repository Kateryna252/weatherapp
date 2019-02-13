import html
from urllib.request import urlopen, Request
RP5_URL = ("http://rp5.ua/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D1%83_%D0%9B%D1%8C%D0%B2%D0%BE%D0%B2%D1%96,"
            "_%D0%9B%D1%8C%D0%B2%D1%96%D0%B2%D1%81%D1%8C%D0%BA%D0%B0_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C")
headers = {'User-Agent':'Mozilla/5.0(X11; Fedora; Linux x86_64;)'}
rp5_request = Request(RP5_URL, headers=headers)
rp5_page = urlopen(rp5_request).read()
rp5_content = str(rp5_page.decode("utf-8"))

RP5_CONTAINER_TEG = '<div id="ArchTemp">'
RP5_TEMP_TAG = '<span class="t_0" style="display: block;">'
rp5_temp_tag = rp5_content.find(RP5_TEMP_TAG, rp5_content.find(RP5_CONTAINER_TEG))
rp5_temp_tag_size = len(RP5_TEMP_TAG)
rp5_temp_value_start = rp5_temp_tag + rp5_temp_tag_size
rp5_temp = ''
for char in rp5_content[rp5_temp_value_start:]:
    if char != '<':
        rp5_temp += char
    else:
        break

print(f'Temperature from RP5_site: {html.unescape(rp5_temp)}\n')

ACCU_COND_TEG = '<span class="cond">'
accu_cond_tag_size = len(ACCU_COND_TEG)
accu_cond_tag_index = accu_page.find(ACCU_COND_TEG)
accu_cond_value_start = accu_cond_tag_index + accu_cond_tag_size
accu_cond = ''
for char in accu_page[accu_cond_value_start:]:
    if char != "<":
        accu_cond += char
    else:
        break

print('AccuWeather:\n')
print(f'Temperature: {html.unescape(accu_temp)}\n')
print(f'Condition of weather:{accu_cond }\n')




