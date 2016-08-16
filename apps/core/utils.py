from apps.clips.models import Clip
from datetime import datetime
from bs4 import BeautifulSoup
from django.core.cache import cache
import traceback
import requests
import re
import json

#######################################################################################
#######################################################################################
#######################################################################################
# Auto get frame with list domain

LIST_ACCEPT_DOMAIN = ['sportingvideo.net', 'mythethao.com', 'linktructiepbongda.com', '1xbet.com']
LIST_DENIDED_DOMAIN = ['youtube', 'dailymotion']


def check_if_auto(url):
    if "AUTO$" in url:
        for domain in LIST_ACCEPT_DOMAIN:
            if domain in url:
                return url.replace('AUTO$', '')
    return False


def get_body(url):
    try:
        root_url = check_if_auto(url)
        if root_url:
            r = requests.get(root_url)
            return r.text
        return False
    except:
        print(traceback.format_exc())
        return False


# parse url and call function
def get_frame(url):
    if 'sportingvideo.net' in url:
        return get_frame_1(url)
    elif 'mythethao.com' in url:
        return get_frame_2(url)
    elif 'linktructiepbongda.com' in url:
        return get_frame_3(url)
    elif '1xbet.com' in url:
        return get_frame_4(url)


# sportingvideo.net
def get_frame_1(url):
    try:
        body = get_body(url)
        if body:
            soup = BeautifulSoup(body)
            table = soup.find('table')
            td = str(table.find('td', style="padding:0px 15px 15px 0px;"))
            td = td.replace('<td style="padding:0px 15px 15px 0px;">', '').replace('</td>', '')
            if 'ads_video' in td:
                return False
            return td
        return False
    except:
        print(traceback.format_exc())
        return False


# mythethao.com
def get_frame_2(url):
    try:
        body = get_body(url)
        if body:
            soup = BeautifulSoup(body)
            content = soup.find('div', {'class': 'football_live_frame'}, style="display: block")
            if 'Đang cập nhật' in content.text:
                return False
            content = str(content).replace('<div class="football_live_frame" style="display: block">', '').replace(
                '</div>', '')
            return content
        return False
    except:
        print(traceback.format_exc())
        return False


# linktructiepbongda.com
def get_frame_3(url):
    try:
        data = re.search(r"id=(.*)&", url)
        id = data.group().replace('&', '')
        t_url = "AUTO$http://linktructiepbongda.com/playLink.aspx?" + id
        body = get_body(t_url)
        if body:
            soup = BeautifulSoup(body)
            form = soup.find(id="form1")
            for decided in LIST_DENIDED_DOMAIN:
                if decided in str(form):
                    return False
        return str(form.contents[5])
    except:
        print(traceback.format_exc())
        return False


# 1xbet.com
def get_frame_4(url):
    try:
        sportstream365 = cache.get('sportstream365')
        # print('sportstream', sportstream365)
        key = url.replace("AUTO$http://1xbet.com/", "")
        # print('key', key)
        sport_id = sportstream365.get(key)
        # print('sportid: ', sport_id)
        if sport_id:
            iframe = '<iframe scrolling="no" width="680" height="375" src="http://sportstream365.com/viewer/frame?game=' + str(sport_id) + \
                     '&header=1&autoplay=1&width=680&height=375" frameborder="0" allowfullscreen=""></iframe>'
            return iframe
        else:
            return False
    except:
        print(traceback.format_exc())
        return False


def get_xbet_line(url):
    try:
        root_url = check_if_auto(url)
        if root_url:
            if 'live' in url:
                data = re.findall(r"\/(\d+)-", url)
                champ = data[1]
                request_url = 'https://www.1xbet.com/LiveFeed/GetGame?id=' + champ + '&lng=en&cfview=0'

                r = requests.get(request_url)
                json_data = json.loads(r.text)
                data_server = json_data['Value']

                frame = '<iframe scrolling="no" width="680px" height="375px" src="http://sportstream365.com/viewer/frame?game=' + champ + \
                         '&header=1&autoplay=1&width=680&height=375" frameborder="0" allowfullscreen=""></iframe>'
                js_data = {
                    "type": "live",
                    "url": "AUTO$http://1xbet.com/" + data_server['Opp1Eng'] + " - " + data_server["Opp2Eng"],
                    "frame": frame
                }
                return js_data
            elif 'line' in url:
                data = re.findall(r"\/(\d+)-", url)
                champ = data[1]
                request_url = 'https://www.1xbet.com/LineFeed/GetGame?id=' + champ + '&lng=en&cfview=0'

                r = requests.get(request_url)
                json_data = json.loads(r.text)
                data_server = json_data['Value']
                if data_server:
                    js_data = {
                        "type": "line",
                        "url": "AUTO$http://1xbet.com/" + data_server['Opp1Eng'] + " - " + data_server["Opp2Eng"]
                    }
                    return js_data
        return False
    except:
        print(traceback.format_exc())
        return False


#######################################################################################
#######################################################################################
#######################################################################################
# Auto data from sportstream365.com
def get_data_sport_stream():
    try:
        url = 'http://sportstream365.com/LiveFeed/GetLeftMenuShort?sports=1&lng=en&partner=24&_=' + str(datetime.now())
        r = requests.get(url)
        json_data = json.loads(r.text)
        data = json_data['Value']
        cache_obj = {}
        for item in data:
            key = item['Opp1'] + ' - ' + item['Opp2']
            cache_obj[key] = item['FirstGameId']
        cache.set('sportstream365', cache_obj)
    except:
        print(traceback.format_exc())


#######################################################################################
#######################################################################################
#######################################################################################
# Auto data b from sportstream365.com
def get_data_full_sport_stream():
    try:
        url = 'http://sportstream365.com/LiveFeed/GetLeftMenuShort?sports=1,3&lng=en&partner=24&_=' + str(datetime.now())
        r = requests.get(url)
        json_data = json.loads(r.text)
        data = json_data['Value']
        cache_obj = {
            'football': [],
            'basketball': [],
        }

        for item in data:
            if item['SportId'] == 1:
                cache_obj['football'].append(item)
            elif item['SportId'] == 3:
                cache_obj['basketball'].append(item)

        cache.set('full_sportstream365', cache_obj)
    except:
        print(traceback.format_exc())


#######################################################################################
#######################################################################################
#######################################################################################
# Auto get video from footyroom

def get_list_clip_ball():
    try:
        root_url = "http://footyroom.com/api/2.0/posts.php?page=1"
        r = requests.get(root_url)
        if r.text:
            soup = BeautifulSoup(r.text)
            list_video = soup.find_all("div", {"class": "vid"})
            for video in list_video:
                vidTop = video.find('header')
                vidThumb = video.find('div', {'class': 'vidthumb'})

                data = {
                    'name': vidTop.text,
                    'tournament': video.find('span', {'class': 'vid_category'}).text,
                    'slug': str(vidTop.next.attrs['href']).replace('/', ''),
                    'url': "http://footyroom.com" + vidTop.next.attrs['href'],
                    'image': vidThumb.find('img').get('src', '')
                }
                if not Clip.objects.filter(url=data['url']):
                    get_detail_clip_ball(data)
    except:
        print(traceback.format_exc())


def get_detail_clip_ball(data):
    try:
        r = requests.get(data['url'])
        if r.text:
            list_match_id = re.findall(r"videos\\/v2\\/(\d+?)\\/zeus.json\\", r.text)
            if list_match_id:
                frame = '<iframe width="680px" allowfullscreen="true" scrolling="no" height="375px"  frameborder="no" ' \
                        'src="http://cdn.phoenix.intergi.com/14907/videos/' + list_match_id[
                            0] + '/video-sd.mp4?hosting_id=14907"' \
                                 ' title="kplus"></iframe>'
                data['frame'] = frame

                Clip.objects.create(name=data['name'], slug=data['slug'], tournament=data['tournament'],
                                    frame=data['frame'], url=data['url'], image=data['image'])
    except:
        print(traceback.format_exc())


def remove_special(str_input):
    str_input = str_input.lower().strip()
    str_input = re.sub(r'à|á|ạ|ả|ã|â|ầ|ấ|ậ|ẩ|ẫ|ă|ằ|ắ|ặ|ẳ|ẵ',"a", str_input)
    str_input = re.sub(r'À|Á|Ạ|Ả|Ã|Â|Ầ|Ấ|Ậ|Ẩ|Ẫ|Ă|Ằ|Ắ|Ặ|Ẳ|Ẵ',"a", str_input)
    str_input = re.sub(r'è|é|ẹ|ẻ|ẽ|ê|ề|ế|ệ|ể|ễ',"e", str_input)
    str_input = re.sub(r'È|É|Ẹ|Ẻ|Ẽ|Ê|Ề|Ế|Ệ|Ể|Ễ',"e", str_input)
    str_input = re.sub(r'ì|í|ị|ỉ|ĩ',"i", str_input)
    str_input = re.sub(r'Ì|Í|Ị|Ỉ|Ĩ',"i", str_input)
    str_input = re.sub(r'ò|ó|ọ|ỏ|õ|ô|ồ|ố|ộ|ổ|ỗ|ơ|ờ|ớ|ợ|ở|ỡ',"o", str_input)
    str_input = re.sub(r'Ò|Ó|Ọ|Ỏ|Õ|Ô|Ồ|Ố|Ộ|Ổ|Ỗ|Ơ|Ờ|Ớ|Ợ|Ở|Ỡ',"o", str_input)
    str_input = re.sub(r'ù|ú|ụ|ủ|ũ|ư|ừ|ứ|ự|ử|ữ',"u", str_input)
    str_input = re.sub(r'Ù|Ú|Ụ|Ủ|Ũ|Ư|Ừ|Ứ|Ự|Ử|Ữ',"u", str_input)
    str_input = re.sub(r'ỳ|ý|ỵ|ỷ|ỹ',"y", str_input)
    str_input = re.sub(r'Ỳ|Ý|Ỵ|Ỷ|Ỹ',"y", str_input)
    str_input = re.sub(r'đ|Đ',"d", str_input)
    str_input = re.sub(r'!|@|\$|%|\^|\*|\(|\)|\+|=|\&lt;|\&gt;|\?|\/|,|\.|\:|\'| |\"|\&amp;|\#|\[|\]|~',"-", str_input)
    str_input = re.sub(r'_',"-", str_input)
    str_input = re.sub(r'“',"", str_input)
    str_input = re.sub(r'”',"", str_input)
    str_input = re.sub(r' ',"-", str_input)
    str_input = re.sub(r'-+-',"-", str_input)
    str_input = str_input.strip('- ')
    str_input = ''.join(e for e in str_input if e.isalnum() or e == '-')
    return str_input.strip()