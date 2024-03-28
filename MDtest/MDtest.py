from zhipuai import ZhipuAI
import json
import pandas as pd
from io import StringIO

markdown_table = """
| Theme | 中文 | Author | Preview |
| --- | --- | --- | --- |
| github | \- | [sindresorhus/github-markdown-css](https://github.com/sindresorhus/github-markdown-css) | [Preview](https://markdown-theme.vercel.app/#github) |
| shanchui | 山吹 | [#66CCFF](https://github.com/elyhg) | [Preview](https://markdown-theme.vercel.app/#shanchui) |
| shanyue | 山月 | [shanyue](https://github.com/shfshanyue) | [Preview](https://npm.devtool.tech/lodash) |
| condensed-night-purple | 凝夜紫 | [童欧巴](https://github.com/Geekhyt) | [Preview](https://markdown-theme.vercel.app/#condensed-night-purple) |
"""
question='sahnchu的中文名字和Preview分别是什么'
client = ZhipuAI(api_key="6e2bbde6def454ee8eaf6bf86450312b.a2DOXtB2jmWgZGeA") # 填写您自己的APIKey
response = client.chat.completions.create(
    model="glm-3-turbo",  # 填写需要调用的模型名称
    messages=[
        {"role": "user", "content":  f"根据markdonw的中内容，理解其中的表格并回答问题：{markdown_table}，{question}"},],)
print(response.choices[0].message.content)




