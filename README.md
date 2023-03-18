# ChatReviewer

<div style="font-size: 1.5rem;">
  <a href="./README.md">中文</a> |
  <a href="./readme_en.md">English</a>
</div>
</br>


近年来人工智能领域的论文数量爆发增长，而这也需要大量的审稿人来进行审稿。

作为青年教师、科研人员以及博士研究生们平时的工作和学习已经很繁忙了。

各种会议和期刊的审稿需求很大，一个个字，一篇篇的敲审稿意见，十分费时间和精力。

基于之前ChatPaper的启发，因此本人在周末开发了这款ChatReviewer，并且开源给大家。

**ChatPaper是一款基于ChatGPT3.5的API接口的论文自动审稿AI助手。**

如果对您有帮助，一个Star和Fork就是对本人的肯定和鼓励了。

欢迎大家转发，以及任何问题和改进意见！

**注意：ChatReviewer开发的目的是帮助人们提高审稿的效率，而不是完全代替人独立审稿。**

## 主要更新：
**我更新了ChatResponse，这个是根据审稿人的审稿意见生成作者回复的AI助手。（ChatResponse和ChatReviewer有点左右互博的意思...）**

## 使用步骤：
Windows, Mac和Linux系统应该都可，python版本最好是3.8或3.9，因为低于3.8就不支持tiktoken这个包。
1. 在apikey.ini中填入你的openai key（sk开头的那串）。
![image](https://user-images.githubusercontent.com/56249874/226109398-42671901-280f-481f-b56d-dc169823428b.png)
2. 使用过程要使用VPN而且保证全局代理（因为ChatGPT把中国ban了）。
3. 在ReviewFormat.txt中输入你想要的审稿格式(不然就是默认格式)。
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
python chat_reviewer.py --pdf_path "input_file/demo1.pdf"
```
对本地的论文进行批量审稿： 运行chat_reviewer.py， 比如：
```python
python chat_reviewer.py --pdf_path "input_file_path"
```
## 例子：
![98652a676f49578be84e4bb51299d90](https://user-images.githubusercontent.com/56249874/226108616-e9e5fe36-350e-4991-9ece-2259a9af3ac3.png)

## 使用ChatResponse
对本地的论文进行审稿： 运行chat_response.py， 比如：
```python
python chat_response.py --pdf_path "review_comments.txt"
```
![image](https://user-images.githubusercontent.com/56249874/226114965-9a2b91e5-3766-42e8-b17f-05d9abb2191b.png)

## 致谢：
- 感谢OpenAI提供的强大ChatGPT-API；
- 感谢[kaixindelele](https://github.com/kaixindelele)同学的[ChatPaper](https://github.com/kaixindelele/ChatPaper)和开源精神 ，ChatReviewer的代码是基于ChatPaper修改而来。



