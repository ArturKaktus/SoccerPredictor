import requests, bs4

id_match = input("Enter id: ")
site_way = 'https://www.myscore.ru/match/'+str(id_match)+'/#standings;table;overall'
site = requests.get (str(site_way))
pars = bs4.BeautifulSoup(site.text, "html.parser")

hm_html = pars.select('.team .team-primary-content .home-box.logo-enable .team-text.tname-home .tname .tname__text .participant-imglink')
hm_name = hm_html[0].getText()
