import datetime
import re
import time

import bs4
from bs4 import BeautifulSoup
from urllib import parse
from scrapy.selector import Selector
import re
import html.entities
from bs4 import BeautifulSoup as bs
from urllib import parse
from scrapy.selector import Selector
import re
import html.entities
from bs4 import BeautifulSoup as bs
from urllib import parse
from scrapy.selector import Selector

def check_month(month):
    if month == "January" or month == "Jan":
        month = '1'
    elif month == "February" or month == "Feb":
        month = '2'
    elif month == "March" or month == "Mar":
        month = '3'
    elif month == "April" or month == "Apr":
        month = '4'
    elif month == "May" or month == "May":
        month = '5'
    elif month == "June" or month == "Jun":
        month = '6'
    elif month == "July" or month == "Jul":
        month = '7'
    elif month == "August" or month == "Aug":
        month = '8'
    elif month == "September" or month == "Sep":
        month = '9'
    elif month == "October" or month == "Oct":
        month = '10'
    elif month == "November" or month == "Nov":
        month = '11'
    elif month == "December" or month == "Dec":
        month = '12'
    return month


def check_day(day):
    day_int = -1
    if day == "Monday":
        day_int = 0
    elif day == "Tuesday":
        day_int = 1
    elif day == "Wednesday":
        day_int = 2
    elif day == "Thursday":
        day_int = 3
    elif day == "Friday":
        day_int = 4
    elif day == "Saturday":
        day_int = 5
    elif day == "Sunday":
        day_int = 6
    return day_int
def change_timestamp(timestamp):
    # September 25, 2018 at 7:08 PM || April 1, 2018 at 11:53 AM || November 5, 2018
    if len(timestamp.split(',')) == 2:
        year = timestamp.split(",")[1].split('at')[0].strip()
        month = check_month(timestamp.split(",")[0].split(" ")[0].strip())
        day = timestamp.split(",")[0].split(" ")[1].strip()
        if "at" in timestamp:
            hour = timestamp.split(",")[1].split('at')[1].split(":")[0].strip()
            minute = timestamp.split(",")[1].split('at')[1].split(":")[1].split(' ')[0].strip()
            zone = timestamp.split(",")[1].split('at')[1].split(":")[1].split(' ')[1].strip()
            if zone == "PM":
                hour = str(int(hour) + 12)
                if hour == "24":
                    hour = "00"
            timeInt = year + "-" + month + "-" + day + " " + hour + ":" + minute
        else:
            timeInt = year + "-" + month + "-" + day
    # April 15 at 12:17 PM
    elif len(timestamp.split('at')) == 2 and "Yesterday" not in timestamp:
        hour = timestamp.split('at')[1].split(":")[0].strip()
        minute = timestamp.split('at')[1].split(":")[1].split(" ")[0].strip()
        try:
            zone = timestamp.split('at')[1].split(":")[1].split(" ")[1].strip()
            if zone == "PM":
                hour = str(int(hour) + 12)
                if hour == "24":
                    hour = "00"
        except:
            pass
        year = time.strftime('%Y', time.localtime(time.time()))
        day_or_month = timestamp.split('at')[0].split(' ')[0].strip()
        check_day_or_month = check_day(day_or_month)
        if check_day_or_month > -1:
            day_sub = datetime.date.today().weekday() - check_day_or_month
            year_month_day = datetime.date.today() - datetime.timedelta(day_sub)
            timeInt = str(year_month_day) + " " + hour + ":" + minute
        else:
            try:
                int(day_or_month)
                # 2 July
                month = timestamp.split('at')[0].split(' ')[1].strip()
                month = check_month(month)
                day = timestamp.split('at')[0].split(' ')[0].strip()
            except:
                # July 23
                month = check_month(day_or_month)
                day = timestamp.split('at')[0].split(' ')[1].strip()
            timeInt = year + "-" + month + "-" + day + " " + hour + ":" + minute
    # 10 hrs
    elif 'hrs' in timestamp or 'hr' in timestamp:
        hour_temp = timestamp.split(' ')[0]
        timeInt = (datetime.datetime.now() - datetime.timedelta(hours=int(hour_temp))).strftime('%Y-%m-%d %H:%M')
    # 30 mins
    elif 'mins' in timestamp or 'min' in timestamp:
        minute = timestamp.split(' ')[0]
        timeInt = (datetime.datetime.now() - datetime.timedelta(minutes=int(minute))).strftime('%Y-%m-%d %H:%M')
    # Yesterday at 12:32 AM
    elif 'Yesterday' in timestamp:
        hour = timestamp.split('at')[1].split(':')[0].strip()
        if hour:
            if timestamp.split('at')[1].split(':')[1].split(' ')[1].strip() == 'PM':
                hour = str(int(hour) + 12)
                if hour == "24":
                    hour = "00"
            minute = timestamp.split('at')[1].split(':')[1].split(' ')[0].strip()
            timeInt = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime(
                '%Y-%m-%d') + " " + hour + ":" + minute
    # Apr 22 or July 2012 or 22 Apr
    elif len(timestamp.split(" ")) == 2:
        year = time.strftime('%Y', time.localtime(time.time()))
        month, day = timestamp.split(" ")
        try:
            int(day)
        except:
            temp = month
            month = day
            day = temp
        if re.match(r"[0-9]{4}", day):
            year = day
            day = "1"
        month = check_month(month)
        timeInt = year + "-" + month + "-" + day
    else:
        timeInt = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
    return timeInt
if __name__ == "__main__":

    f = open('mac_userinfo.html', 'r', encoding='utf-8')
    line = f.readline()
    string = ''
    while line:
        string += line
        line = f.readline()
    next_url_prefix = re.search(r'href:"(.+?)"', string).group(1)
    sel=Selector(text=string)
    name = sel.xpath("//head/title/text()").get()
    # print(name)
    soup = BeautifulSoup(open('zuck_content.html', encoding='utf-8'), features="html.parser")
    text = soup.find_all(string=lambda text: isinstance(text, bs4.element.Comment))
    index = 0
    for textItem in text:
        textItem = BeautifulSoup(textItem, features="html.parser")
        if textItem.find(attrs={"data-sigil": "scroll-area"}):
            break
        else:
            index +=1
    textSoup = BeautifulSoup(text[index], features="html.parser")
    articleItem = textSoup.find_all('article')
    for article in articleItem:

        selector=Selector(text=str(article))
        post_id_pattern = selector.xpath('.//@data-ft').get()
        # TimeStampInt = re.search('"publish_time":"(.+?)"', post_id_pattern).group(1)
        # print(TimeStampInt)
        if post_id_pattern:
            post_id=re.search('"tl_objid":"(.+?)"',post_id_pattern).group(1)
        else:
            post_id=''
        print(post_id)
        stamp_time = selector.xpath(".//div/a/abbr/text()").get()
        if stamp_time:
            timestamp = stamp_time
            TimeStamp = change_timestamp(timestamp)
            try:
                datetime_obj = datetime.datetime.strptime(TimeStamp, '%Y-%m-%d %H:%M')
            except:
                datetime_obj = datetime.datetime.strptime(TimeStamp, '%Y-%m-%d')
            TimeStampInt = int(time.mktime(datetime_obj.timetuple()) * 1000.0)
        else:
            timestamp = 'Now'
            TimeStamp = change_timestamp(timestamp)
            datetime_obj = datetime.datetime.strptime(TimeStamp, '%Y-%m-%d %H:%M')
            TimeStampInt = int(time.mktime(datetime_obj.timetuple()) * 1000.0)

        # location
        location = selector.xpath(".//div/div[2]/div[1]/a/text()").get()
        if location is None:
            location = ''
        # like_people_num
        like_relation_pattern = selector.xpath(".//footer")
        like_people_num = 0
        if len(like_relation_pattern) > 0:
            if like_relation_pattern.xpath(".//a/@href").get():
                comment_url = 'https://m.facebook.com' + like_relation_pattern.xpath(".//a/@href").get()
            else:
                comment_url = ""
            if like_relation_pattern.xpath(".//a//div/text()").get():
                like_people_num = like_relation_pattern.xpath(".//a//div/text()").get()
                if 'K' in like_people_num:
                    like_people_num = int(re.search('\d+', like_people_num).group(0)) * 1000
                else:
                    like_people_num = int(re.search('\d+', like_people_num).group(0))

            else:
                like_people_num = 0
            comment_num=like_relation_pattern.xpath('.//div[@class="_1fnt"]/span[@data-sigil="comments-token"]/text()')
            if comment_num:
                comments_people=comment_num.get()
                # print(comments_people)
                if 'Comments' in comments_people:
                    comments_people=(comments_people.split(' ')[0])
                    # print(comments_people_)
                    if 'K' in comments_people:
                        comments_people_num=float(re.search('\d+(\.\d+)?', comments_people).group(0))*1000
                        comments_people_num=int(comments_people_num)
                    else:
                        comments_people_num = int(re.search('\d+(\.\d+)?', comments_people).group(0))
                else:
                    comments_people_num=0
            else:
                comments_people_num=0
        # the title of post
        title = ""
        retweetFromName = ''
        isRetweet = False
        retweetContent = ''
        img_content = []
        screen_urp =selector.xpath('.//strong/a/@href').get()
        screen_name = screen_urp.split('?')[0].split('/')[1]
        screen_url = 'https://m.facebook.com' + screen_urp
        is_retweet_article = selector.xpath("//article")
        if len(is_retweet_article) == 2:
            is_retweet_article = is_retweet_article[-1]
            isRetweet = True
            retweetFromName = is_retweet_article.xpath(".//h3/strong/a/text()").get()
            retweetContent = is_retweet_article.xpath(".//p/text()").get()
            content = selector.xpath("string(.//div/div[1]/span/p)").get()
        else:
            content = selector.xpath(".//p/text()").get()
            # img_content = selector.xpath("//div/div[2]//img/@src").getall()
            post_images_array = []
            post_images = selector.xpath('.//div/div[2]//div//i/@style').get()
            if post_images:
                if 'static.xx' not in post_images:
                    post_images = post_images.replace('\'', '"')
                    post_images = post_images.replace("\\3a ", ":")
                    post_images = post_images.replace("\\3d ", "=")
                    post_images = post_images.replace("\\26 ", "&")
                    post_images = post_images.replace("\\", "")
                    post_images = re.search(r'url\("(.+?)"', post_images).group(1)
                    post_images_array.append(post_images)
    print('1')