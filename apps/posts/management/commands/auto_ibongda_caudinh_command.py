from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup, Tag
from apps.posts.models import Post
from apps.categories.models import Category
from apps.core import utils
import requests
import traceback
import re


class Command(BaseCommand):
    def __init__(self, stdout=None, stderr=None, no_color=False):
        super().__init__(stdout, stderr, no_color)

        self.requests = requests.session()

        self.headers = {
            "Host": "ibongda.vn",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
        }

    def add_arguments(self, parser):
        parser.add_argument('params1', nargs='?', type=int)

    def handle(self, *args, **options):
        # Using parameters:
        # print('params1:', options['params1']
        self.stdout.write('[#] Begin execute...')
        try:
            self.get_list_ibongda_news()
        except Exception as e:
            print('Error:', e)
        self.stdout.write('[#] DONE!')

    def get_list_ibongda_news(self):
        try:
            root_url = "http://ibongda.vn/tin-tuc/tran-cau-dinh"
            r = self.requests.get(root_url, headers=self.headers)
            if r.text:
                soup = BeautifulSoup(r.text.encode('utf8'))
                list_new = soup.find("div", {"id": "wapper-body-left-content"})
                list_new = list_new.find_all("div", {"class": "catalog-list-news"})
                for new in list_new:
                    a_info = new.find('a', {'class': 'tt-news'})
                    url = 'http://ibongda.vn' + a_info.attrs['href']
                    name = a_info.text.strip()

                    image = new.find('img', {'class': 'news-content-img'})
                    image = image.attrs['src']

                    description = new.find('p', {'class': 'news-sapo'}).text.strip()

                    data = {
                        'name': name,
                        'url': url,
                        'description': description,
                        'image': image,
                        'slug': utils.remove_special(name)
                    }
                    if not Post.objects.filter(url=data['url']):
                        self.get_detail_ibongda_news(data)
        except:
            print(traceback.format_exc())

    def get_detail_ibongda_news(self, data):
        try:
            r = self.requests.get(data['url'], headers=self.headers)
            ctn = r.content.decode('utf-8')
            if r.text:
                soup = BeautifulSoup(ctn)
                content = soup.find("div", {"id": "wapper-body-left-content"})
                content = content.find("div", {"class": "info-ct-news"})

                # remove ads
                content_ads = content.find("div", {"id": "predict-news-sms-ads"})
                del content_ads

                # remove href a
                for a in soup.find_all('a'):
                    del a['href']

                # join to string
                content = ''.join(map(str, content.contents))
                content = content.replace('<strong style="color:#0360A6;">IBONGDA.VN</strong>', '<strong style="color:#0360A6;">MYBONGDA.COM</strong>')
                content = content.replace('ibongda dự đoán', 'mybongda dự đoán')
                data['content'] = content.strip()

                category = Category.objects.get(id=3)
                Post.objects.create(name=data['name'], slug=data['slug'], content=data['content'],
                                    url=data['url'], image_source=data['image'], category=category,
                                    description=data['description'])
        except:
            print(traceback.format_exc())

