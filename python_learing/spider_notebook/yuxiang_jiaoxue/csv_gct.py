import requests, csv, re
from lxml import etree


headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

r = requests.get('http://seputu.com/', headers=headers)

html = etree.HTML(r.text)

div_mulus = html.xpath('//div[@class="mulu"]')

rows = []
for div_mulu in div_mulus:
    # H2标记
    div_h2 = div_mulu.xpath('.//div[@class="mulu-title"]/center/h2/text()')
    if len(div_h2) > 0:
        h2_title = div_h2[0]
        a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')
        for a in a_s:
            # href属性
            href = a.xpath('./@href')[0]
            # 找子标题
            box_title = a.xpath('./@title')[0]

            pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
            match = pattern.search(box_title)
            if match != None:
                date = match.group(1)
                real_title = match.group(2)
                content = (h2_title, real_title.strip(), href, date)
                # print(content)
                rows.append(content)
header = ['title', 'real_title', 'href', 'date']

with open('../datas/tables/gct.csv', 'a') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(header)
    f_csv.writerows(rows)