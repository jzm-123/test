# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

import scrapy


class UserInfo(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()  # 用户id
    username = scrapy.Field()  # 用户名
    biography = scrapy.Field()  # 简介
    posts_num = scrapy.Field()  # 投稿数
    follower_num = scrapy.Field()  # 粉丝数
    following_num = scrapy.Field()  # 追随数
    is_verified = scrapy.Field()    # 是否已验证
    external_url = scrapy.Field()   # 用户的外部链接（facebook,youtube等）
    is_private = scrapy.Field()
    external_url_linkshimmed = scrapy.Field()
    is_business_account = scrapy.Field()
    is_joined_recently = scrapy.Field()
    profile_pic_url = scrapy.Field()
    business_account = scrapy.Field()
    site = scrapy.Field()
    pass


class Followers(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()  # 粉丝id
    follower_name = scrapy.Field()  # 粉丝名
    user_id = scrapy.Field()  # 是谁的粉丝
    pass


class Followings(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()  # 被追随人id
    following_name = scrapy.Field()  # 被追随人用户名
    user_id = scrapy.Field()  # 追随人id
    pass


class Posts(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()  # 稿件id
    url = scrapy.Field()  # 图片(视频)url
    content = scrapy.Field()  # 稿件文字内容
    time = scrapy.Field()  # 投稿时间
    likes = scrapy.Field()  # 点赞数
    comment_num = scrapy.Field()  # 评论数
    user_id = scrapy.Field()  # 作者id
    is_video = scrapy.Field()  # 是否是视频
    shortcode = scrapy.Field() # 类似稿件id，两个都可以作为主码
    picture_id = scrapy.Field()       # 图片id，若为帖子第一张图片，图片id=帖子id
    picture_url = scrapy.Field()      # 图片下载url
    picture_content = scrapy.Field()  # 图片内容
    post_id = scrapy.Field()  # 帖子id
    son_id = scrapy.Field()  # 子图片(视频)id
    son_url = scrapy.Field()  # 子图片(视频)url
    son_is_video = scrapy.Field()  # 是否是视频
    pass



class Comments(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()     # 评论id
    user_id = scrapy.Field()    # 评论人id
    username = scrapy.Field()  # 评论人昵称
    content = scrapy.Field()  # 评论内容
    time = scrapy.Field()   # 评论时间戳
    likes = scrapy.Field()  # 评论点赞数
    son_comments = scrapy.Field()   # 子评论数
    post_shortcode = scrapy.Field()  # 稿件shortcode
    pass


class SonComments(scrapy.Item):
    id = scrapy.Field()  # 评论id
    user_id = scrapy.Field()  # 评论人id
    username = scrapy.Field()  # 评论人昵称
    content = scrapy.Field()  # 评论内容
    time = scrapy.Field()  # 评论时间戳
    likes = scrapy.Field()  # 评论点赞数
    parent_id = scrapy.Field()  # 父评论id
    pass


