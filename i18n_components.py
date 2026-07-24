import os, re

BASE = r"D:\Git\frontend\src"

# Read each file, apply t() to visible text
files = [
    # Home.vue
    ("views/jiuyou/Home.vue", [
        ("JIUYOU \u00b7 \u59cb\u4e8e2001", "{{ t('hero_badge') }}"),
        ("\u4e45\u53cb\u7535\u5668<br><span class=\"gold\">\u667a\u9020\u54c1\u8d28\u751f\u6d3b</span>", "{{ t('hero_title1') }}<br><span class=\"gold\">{{ t('hero_title2') }}</span>"),
        ("\u4e13\u6ce8\u7535\u98ce\u6247\u4e0e\u53d6\u6696\u5668 \u00b7 \u8ba9\u6bcf\u4e2a\u5bb6\u5ead\u4eab\u53d7\u79d1\u6280\u5e26\u6765\u7684\u8212\u9002\u4e0e\u4fbf\u6377", "{{ t('hero_desc') }}"),
        ("\u63a2\u7d22\u4ea7\u54c1", "{{ t('hero_btn1') }}"),
        ("\u4e86\u89e3\u4e45\u53cb", "{{ t('hero_btn2') }}"),
        ("\u516c\u53f8\u6210\u7acb", "{{ t('home_stats_1l') }}"),
        ("\u51fa\u53e3\u56fd\u5bb6", "{{ t('home_stats_2l') }}"),
        ("\u56fd\u5185\u7701\u5e02", "{{ t('home_stats_3l') }}"),
        ("\u56fd\u9645\u8ba4\u8bc1", "{{ t('home_stats_4l') }}"),
        ("\u4f53\u7cfb\u8ba4\u8bc1", "{{ t('home_stats_5l') }}"),
        ("\u59cb\u4e8e2001 \u00b7 \u4e13\u6ce8\u7535\u98ce\u6247\u4e0e\u53d6\u6696\u5668", "{{ t('home_about_title') }}"),
        ("\u4e86\u89e3\u66f4\u591a", "{{ t('home_about_btn') }}"),
        ("\u4ea7\u54c1\u7cfb\u5217", "{{ t('home_pro_title') }}"),
        ("\u7535\u98ce\u6247\u4e0e\u53d6\u6696\u5668\u4e24\u5927\u7cfb\u5217\uff0c\u54c1\u8d28\u5353\u8d8a", "{{ t('home_pro_desc') }}"),
        ("\u9009\u62e9\u4e45\u53cb\u7684\u7406\u7531", "{{ t('home_why_title') }}"),
        ("\u65b0\u95fb\u52a8\u6001", "{{ t('home_news_title') }}"),
        ("\u5173\u6ce8\u4e45\u53cb\u6700\u65b0\u8d44\u8baf", "{{ t('home_news_desc') }}"),
        ("\u67e5\u770b\u66f4\u591a\u65b0\u95fb", "{{ t('home_news_btn') }}"),
        ("\u6253\u9020\u54c1\u8d28\u751f\u6d3b \u00b7 \u4ece\u4e45\u53cb\u5f00\u59cb", "{{ t('home_cta_title') }}"),
        ("\u5728\u7ebf\u7559\u8a00", "{{ t('home_cta_btn') }}"),
    ]),
    # About.vue
    ("views/jiuyou/About.vue", [
        ("\u5173\u4e8e\u4e45\u53cb", "{{ t('about_hero') }}"),
        ("\u4e13\u6ce8\u7535\u98ce\u6247\u4e0e\u53d6\u6696\u5668 \u00b7 \u521b\u65b0\u9a71\u52a8\u54c1\u8d28", "{{ t('about_hero_desc') }}"),
        ("\u59cb\u4e8e2001 \u00b7 \u667a\u9020\u672a\u6765", "{{ t('about_hero_title') }}"),
        ("\u7ecf\u8425\u7406\u5ff5", "{{ t('about_phil_title') }}"),
        ("\u8d44\u8d28\u8363\u8a89", "{{ t('about_honor_title') }}"),
        ("\u4f01\u4e1a\u8d23\u4efb", "{{ t('about_resp_title') }}"),
    ]),
    # Culture.vue
    ("views/jiuyou/Culture.vue", [
        ("\u4f01\u4e1a\u6587\u5316", "{{ t('culture_hero') }}"),
        ("\u4ee5\u6587\u5316\u51dd\u805a\u529b\u91cf \u00b7 \u7528\u521b\u65b0\u5f15\u9886\u672a\u6765", "{{ t('culture_hero_desc') }}"),
        ("\u4f01\u4e1a\u6838\u5fc3\u7406\u5ff5", "{{ t('culture_title') }}"),
    ]),
    # Products.vue
    ("views/jiuyou/Products.vue", [
        ("\u4ea7\u54c1\u4e2d\u5fc3", "{{ t('pro_hero') }}"),
        ("\u56db\u5927\u4ea7\u54c1\u77e9\u9635\uff0c\u5168\u9762\u8986\u76d6\u667a\u6167\u5bb6\u5ead\u6240\u9700", "{{ t('pro_hero_desc') }}"),
        ("\u641c\u7d22\u4ea7\u54c1\u540d\u79f0\u6216\u5173\u952e\u8bcd...", "{{ t('pro_search') }}"),
        ("\u6b3e\u4ea7\u54c1", "{{ t('pro_count') }}"),
        ("\u67e5\u770b\u8be6\u60c5", "{{ t('pro_detail') }}"),
        ("\u4e0a\u4e00\u9875", "{{ t('pro_prev') }}"),
        ("\u4e0b\u4e00\u9875", "{{ t('pro_next') }}"),
        ("\u4ea7\u54c1\u76ee\u5f55", "{{ t('pro_catalog') }}"),
    ]),
    # News.vue
    ("views/jiuyou/News.vue", [
        ("\u65b0\u95fb\u4e2d\u5fc3", "{{ t('news_hero') }}"),
        ("\u4e45\u53cb\u7535\u5668\u6700\u65b0\u8d44\u8baf\u4e0e\u884c\u4e1a\u52a8\u6001", "{{ t('news_hero_desc') }}"),
        ("\u67e5\u770b\u8be6\u7ec6", "{{ t('news_btn') }}"),
    ]),
    # Downloads.vue
    ("views/jiuyou/Downloads.vue", [
        ("\u4e0b\u8f7d\u4e2d\u5fc3", "{{ t('dl_hero') }}"),
        ("\u4ea7\u54c1\u8d44\u6599\u3001\u6280\u672f\u6587\u6863\u4e00\u7ad9\u5f0f\u4e0b\u8f7d", "{{ t('dl_hero_desc') }}"),
        ("\u5168\u90e8", "{{ t('dl_all') }}"),
        ("\u4e0b\u8f7d", "{{ t('dl_btn') }}"),
    ]),
    # Contact.vue
    ("views/jiuyou/Contact.vue", [
        ("\u5728\u7ebf\u7559\u8a00", "{{ t('contact_hero') }}"),
        ("<h2>\u7559\u8a00\u54a8\u8be2</h2>", "<h2>{{ t('contact_form_title') }}</h2>"),
        ("\u6b22\u8fce\u7559\u4e0b\u60a8\u7684\u9700\u6c42\u4e0e\u5efa\u8bae\uff0c\u4e45\u53cb\u5ba2\u670d\u5c06\u572824\u5c0f\u65f6\u5185\u4e0e\u60a8\u8054\u7cfb\u3002", "{{ t('contact_form_desc') }}"),
        ("\u63d0\u4ea4\u7559\u8a00", "{{ t('contact_submit') }}"),
    ]),
]

for path, replacements in files:
    fp = os.path.join(BASE, path)
    if not os.path.exists(fp):
        print(f"SKIP: {fp}")
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
        else:
            print(f"  MISS: {old[:30]}... in {path}")
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"OK: {path}")

print("ALL DONE")