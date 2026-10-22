# SITE = ite(
#     name="名人引文",                                  # ① 文档标题
#     base_url="https://quotes.toscrape.com/",          # ② 列表页第一页网址
#     item_selector="div.quote",                        # ③ "一条数据"的容器
#     fields=[                                          # ④ 你要抓哪些列
#         Field(header="作者", selector="small.author", width_cm=2.8),
#         Field(header="引文内容", selector="span.text", width_cm=8.0),
#         Field(header="标签", selector="div.tags a.tag", width_cm=4.0),
#     ],
# )