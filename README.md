# ChatReviewer & ChatResponse

<div style="font-size: 1.5rem;">
  <a href="./README.md">中文</a> |
  <a href="./readme_en.md">English</a>
</div>
</br>

**ChatReviewer是一款基于ChatGPT-3.5的API接口的论文自动审稿AI助手。用途如下：**

1. 对论文进行批量总结和评论，提高科研人员的文献阅读和理解的效率。
2. 对自己的论文进行评估，根据ChatReviewer生成的审稿意见进行查漏补缺，进一步提高自己的论文质量。
3. 辅助论文审稿，给出参考的审稿意见，提高审稿效率和审稿质量。（⭐️禁止复制粘贴！）

**ChatResponse是一款根据审稿人的评论自动生成作者回复的AI助手。用途如下：**
1. 根据收到的审稿意见，ChatResponse自动提取其中各个审稿人的问题和担忧，并生成点对点的回复。

基于之前ChatPaper的启发，本人在周末开发了这款ChatReviewer，并且开源给大家。

如果对您有帮助，一个Star和Fork就是对本人的肯定和鼓励了。

欢迎大家转发，以及任何问题和改进意见！

**⭐️⭐️⭐️ 声明：请对审稿的论文负责，不要直接复制粘贴ChatReviewer生成的任何审稿意见！！！**

## 主要更新：
- **Todo: 做一个网页版本的ChatReviewer和ChatResponse**（太忙...不确定什么时候做）
- 重写了section split的逻辑, fix了可能抓不到固定标题的问题；修改prompt机制：先询问chatgpt 它感兴趣的章节, 随后再发送相应的章节。
- **更新了ChatResponse，这个是根据审稿人的评论自动生成作者回复的AI助手。**（ChatResponse和ChatReviewer有点左右互博的意思...）


## 使用步骤：
Windows, Mac和Linux系统应该都可，python版本最好是3.8或3.9，因为低于3.8就不支持tiktoken这个包。
1. 在apikey.ini中填入你的openai的api key（sk开头的那串，[如何获取Api Key](https://chatgpt.cn.obiscr.com/blog/posts/2023/How-to-get-api-key/)）。
![image](https://user-images.githubusercontent.com/56249874/226109398-42671901-280f-481f-b56d-dc169823428b.png)
2. 使用过程要使用VPN而且保证全局代理（因为ChatGPT把中国ban了）。
3. 在ReviewFormat.txt中输入你想要的特殊审稿格式（不然就是默认格式）。
![image](https://user-images.githubusercontent.com/56249874/226108813-dc44924f-5528-4644-aed2-475d23ccdd84.png)
4. 安装依赖：使用VPN。
``` bash
pip install -r requirements.txt
```
或者使用国内镜像：
```bash
pip install -r requirements.txt -i  http://pypi.douban.com/simple  --trusted-host pypi.douban.com
```
5. 对本地的论文进行审稿： 运行chat_reviewer.py， 比如：
```python
python chat_reviewer.py --paper_path "input_file/demo1.pdf"
```
对本地的论文进行批量审稿： 运行chat_reviewer.py， 比如：
```python
python chat_reviewer.py --paper_path "input_file_path"
```
## 例子：
![image](https://user-images.githubusercontent.com/56249874/226351967-ef0e6f61-457a-4a77-b78f-84bde47ac38c.png)

## 使用ChatResponse
对本地的审稿评论review_comments.txt进行回复： 运行chat_response.py， 比如：
```python
python chat_response.py --comment_path "review_comments.txt"
```
例子：
![image](https://user-images.githubusercontent.com/56249874/226114965-9a2b91e5-3766-42e8-b17f-05d9abb2191b.png)

## 致谢：
- 感谢OpenAI提供的强大ChatGPT-API；
- 感谢[kaixindelele](https://github.com/kaixindelele)同学的[ChatPaper](https://github.com/kaixindelele/ChatPaper)和开源精神 ，ChatReviewer的代码是基于ChatPaper修改而来。



