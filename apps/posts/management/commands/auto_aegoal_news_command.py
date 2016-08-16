from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from apps.posts.models import Post
from apps.categories.models import Category
from apps.core import utils
import requests
import traceback
import re


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('params1', nargs='?', type=int)

    def handle(self, *args, **options):
        # Using parameters:
        # print('params1:', options['params1']
        self.stdout.write('[#] Begin execute...')
        try:
            self.get_list_aegoal_news()
        except Exception as e:
            print('Error:', e)
        self.stdout.write('[#] DONE!')

    def get_list_aegoal_news(self):
        try:
            root_url = "http://www.bongda365.com.vn/tin-moi-nhat/"
            r = requests.get(root_url)
            if r.text:
                soup = BeautifulSoup(r.text)

                # First
                list_top = soup.find_all("article", {"class": "post"})
                post_first = list_top.pop(0)

                ################################################################
                # box_1 = list_top.find("div", {"class": "box1"})
                # a_href = box_1.find_all('a')[0]
                # image = a_href.find('img')
                # a_info = box_1.find_all('a')[1]

                # url = 'http://aegoal.com' + a_href.attrs['href']
                # image = 'http://aegoal.com' + image.attrs['src']
                # name = a_info.text.strip()

                # data = {
                #     'name': name,
                #     'url': url,
                #     'image': image,
                #     'slug': utils.remove_special(name)
                # }
                # if not Post.objects.filter(url=data['url']):
                #     self.get_detail_aegoal_news(data)
                ################################################################

                # Second
                for new in list_top:
                    a_href = new.find_all('a')[0]
                    image = new.find('img')
                    

                    url = a_href.attrs['href']
                    image = image.attrs['src']
                    name = a_href.text.strip()

                    data = {
                        'name': name,
                        'url': url,
                        'image': image,
                        'slug': utils.remove_special(name)
                    }

                    if not Post.objects.filter(url=data['url']):
                        self.get_detail_aegoal_news(data)
        except:
            print(traceback.format_exc())

    def get_detail_aegoal_news(self, data):
        try:
            r = requests.get(data['url'])
            if r.text:
                soup = BeautifulSoup(r.text)

                content = soup.find("div", {"id": "content"})
                content = content.find("div", {"class": "entry-content"})

                widget_top = content.find("div", {"class": "widget-top"})
                del widget_top
                
                widget_container = content.find("div", {"class": "widget-container"})
                del widget_container
                
                for a in content.find_all('a'):
                    del a['href']

                content = ''.join(map(str, content.contents))

                # content = content.replace('Bongda.com.vn', 'Mybongda.com')
                content = content.replace('BongDa.com.vn', 'Mybongda.com')
                # content = content.replace('bongda.com.vn', 'mybongda.com')

                data['content'] = content

                category = Category.objects.get(id=8)
                Post.objects.create(name=data['name'], slug=data['slug'], content=data['content'],
                                    url=data['url'], image_source=data['image'], category=category)
        except:
            print(traceback.format_exc())
