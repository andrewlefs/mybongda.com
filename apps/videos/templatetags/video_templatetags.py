from django import template
from apps.teams.models import Team
from django.utils import timezone
from apps.core import utils
from apps.fixtures.models import FrameAuto
from datetime import datetime
from django.core.cache import cache
import random

register = template.Library()


@register.filter
def minfilter(num):
    return int(num - 4)


@register.filter
def maxfilter(num):
    return int(num + 4)


@register.filter
def check_greater_time(start_date):
    now = timezone.now()
    now = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
    start_date = datetime(start_date.year, start_date.month, start_date.day, start_date.hour, start_date.minute, start_date.second)
    if start_date <= now:
        return True
    return False


@register.filter
def get_team_name(id):
    try:
        team = Team.objects.get(id=id)
        return team.name
    except:
        return ''


@register.filter
def get_auto_frame(url):
    try:
        if utils.check_if_auto(url):
            auto = FrameAuto.objects.get(url=url)
            if auto.frame:
                return auto.frame
            else:
                frame = utils.get_frame(url)
                if frame:
                    auto.frame = frame
                    auto.save()
                    return frame
        if 'AUTO$' in url:
            return ''
        return url
    except:
        return ''


@register.filter
def get_simulation(url):
    try:
        if 'AUTO$http://1xbet.com/' in url:
            match_string = url.replace('AUTO$http://1xbet.com/', '')
            # print("match_string: ", match_string)
            sportstream365 = cache.get('sportstream365')
            sport_id = sportstream365.get(match_string)
            # print("sport_id: ", sport_id)
            if sport_id:
                iframe = '<object id="playZonePlayer" width="100%" height="300" type="application/x-shockwave-flash" data="https://1xzone.com/Zone.swf?max=0.765873372554779" style="visibility: visible;"><param name="menu" value="false"><param name="wmode" value="opaque"><param name="allowFullScreen" value="false"><param name="scale" value="exactFit"><param name="AllowScriptAccess" value="always"><param name="flashvars" value="ZonePlayGameId=' + str(sport_id) +'&amp;scaleMode=scaleAll&amp;gameId=' + str(sport_id) +'&amp;lng=vi&amp;sport=1"></object>'
                # print('iframe: ', iframe)
                return iframe
            #print("Khong co")
        return False
    except Exception as e:
        # print("get_simulation: ")
        return False


@register.filter
def generator_keyword(title):
    try:
        txt_remove = utils.remove_special(title)
        arr_symbol = title.split(" ")
        arr_slug = txt_remove.split("-")
        str_keyword = ', '.join(arr_slug)

        #for i in range(5):
        #    ri = random.randint(1, 3)
        #    arr_group = random.sample(set(arr_slug), ri)
        #    str_group = ' '.join(arr_group)
        #    str_keyword = str(str_keyword) + str(str_group)

        #    arr_group = random.sample(set(arr_symbol), ri)
        #    str_group = ' '.join(arr_group)
        #    str_keyword = str(str_keyword) + str(str_group)

        return str_keyword
    except Exception as e:
        print(e)
        return ''
