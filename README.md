# RSS Reborn

> 🍰 万物皆可 RSS

**rssreborn** is a reborn version of rsshub in python. By using **rssreborn**, one can controll all wesbites updates that you like at hand.

For instance, listening the updates from 财联社:


![](https://gitcode.net/godofgodofgod/gerg/-/raw/main/pictures/2024/09/21_14_30_5_202409211430193.png)


![](https://gitcode.net/godofgodofgod/gerg/-/raw/main/pictures/2024/09/21_14_29_41_202409211429342.png)

by simply call: `http://127.0.0.1:5000/cls/telegraph/`.

As you can see, now that you can get *almost* everything within your python code, or request from your domain, you can play with these informations as you want.

RSSHub 是一个轻量、易于扩展的 RSS 生成器，可以给任何奇奇怪怪的内容生成 RSS 订阅源

本项目是[原RSSHub](https://github.com/DIYgod/RSSHub)的Python实现。


## Install

To use **rssreborn**, simply:

```
pip install rssreborn
```

then, you can run:

```
rssreborn 
```

On your server, you will have a server setup ready for requesting on any supported website updates.

Open browser navigate to http://127.0.0.1:5000/cls/telegraph/ you'll the result.


## Plan

I wish you can help intergate more websites to here, so that we can have a more robust, consistant python rsshub!

Future plans:

- [ ] support background services request all hub one by one and save to sqlite;
- [ ] Broadcast the updates to anyone subscribed;
- [ ] Maybe a new RSS read client.


