# 制作单词本

# 步骤

1. 准备资料来源。这里以《场景词汇.txt》为例，其最初来自某PDF文档。
2. 提取文本。这里为了方便，使用Adobe Acrobat DC>>导出PDF>>纯文本，提取PDF中的文本。
3. 转换格式编码。默认导出后为ASCII编码，可以用自带的记事本打开，然后另存为，选择编码为UTF8。
4. 提取单词。使用`regex_split.py`脚本来提取，当前（2022.07.23）输入参数如下：
   ```python
    usage: regex_split.py [-h] [-f FILE]

    Clean word list

    optional arguments:
    -h, --help            show this help message and exit
    -f FILE, --file FILE  input file
   ```
5. 导出到欧陆词典。打开[欧路词典网页端](http://my.eudic.net/)，首页>>导入生字本，选择任意一种方式导入生词。
6. 查看生词本。导入成功后可以在[欧路词典网页端](http://my.eudic.net/), 或者APP上查看导入的生字本。
7. 打印生字本或导出生词本为CSV/HTML等格式。
   - 网页端不支持导出刚才的生词本为CSV，需要下载PC版客户端（https://www.eudic.net/v4/en/app/download）；
   - 然后学习笔记>>学习记录管理器，选择对应的生字本，导出。就可以导出包含单词，音标、释义在内的生字本为多种格式了。


# 安装

```python
pip install jieba
```

# 更新日志

## 2022.07.23 
- 增加：README；正则匹配来提取英文单词并输出。


# 证书

MIT