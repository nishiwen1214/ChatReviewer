# ChatReviewer & ChatResponse

<div style="font-size: 1.5rem;">
  <a href="./README.md">中文</a> |
  <a href="./readme_en.md">English</a>
</div>
</br>

Based on the inspiration of ChatPaper, I developed this ChatReviewer over the weekend and open source it for everyone.

**ChatReviewer is an automatic paper review AI assistant based on ChatGPT-3.5's API interface. **

If it is helpful to you, a Star and Fork is a confirmation and encouragement to me.

Feel free to repost it, as well as any questions and improvement ideas!

⭐️⭐️⭐️**Warning: ChatReviewer was developed to help people improve review efficiency and review quality, not to completely replace people with independent review, please be responsible for the reviewed papers and do not directly copy and paste any generated review comments!!! **

## Major updates.
- ** Updated ChatResponse, an AI assistant that automatically generates author responses based on reviewers' comments. (ChatResponse and ChatReviewer are a bit left and right...) **

## Steps to use.
Windows, Mac and Linux systems should be available, python version 3.8 or 3.9 is preferred, because below 3.8 the package tiktoken is not supported.
1. Fill in your openai key (the string starting with sk) in apikey.ini.
2. Enter the review format you want in ReviewFormat.txt (otherwise it is the default format).
3. Installation requirements.
``` bash
pip install -r requirements.txt
```
4. To review a paper locally: run chat_reviewer.py, e.g.
```python
python chat_reviewer.py --paper_path "input_file/demo1.pdf"
```
To do a batch review of a local paper: run chat_reviewer.py, e.g.
```python
python chat_reviewer.py --paper_path "input_file_path"
```
## Example：
![98652a676f49578be84e4bb51299d90](https://user-images.githubusercontent.com/56249874/226108616-e9e5fe36-350e-4991-9ece-2259a9af3ac3.png)
## Use ChatResponse
To reply to a local review comment review_comments.txt: run chat_response.py, e.g.
```python
python chat_response.py --comment_path "review_comments.txt"
```
Example：
![image](https://user-images.githubusercontent.com/56249874/226114965-9a2b91e5-3766-42e8-b17f-05d9abb2191b.png)

## Acknowledgements.
- Thanks to OpenAI for the powerful ChatGPT-API.
- Thanks to [kaixindelele](https://github.com/kaixindelele) for [ChatPaper](https://github.com/kaixindelele/ChatPaper) and the spirit of open source , the code of ChatReviewer is based on ChatPaper modified.

