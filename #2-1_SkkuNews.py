from bs4 import BeautifulSoup
import requests
import re
from kiwipiepy import Kiwi
from krwordrank.sentence import summarize_with_sentences
from krwordrank.hangle import normalize
from gtts import gTTS

url='https://www.skku.edu/skku/campus/skk_comm/news01.do'
resp=requests.get(url)
print(resp)
soup=BeautifulSoup(resp.content,'lxml')

url_list=soup.find('div','board-wrap board-qa').find_all('a')
news_url_list=[]
for url in url_list:
    if "mode" in url['href']:
       news_url_list.append('https://www.skku.edu/skku/campus/skk_comm/news01.do'+url['href'])
print(len(news_url_list))

for idx in range(0, len(news_url_list)):
    print(news_url_list[idx])

#뉴스기사 본문 추출하는 함수
def get_news_by_url(url):

    headers={
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ko,en;q=0.9,en-US;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'
    }
    res=requests.get(url,headers=headers)
    bs=BeautifulSoup(res.content,'html.parser')

    #제목 찾아오기 (html 분석하여 기사 제목 담고 있는 html tag  지정)
    title=bs.find('div','mg50').find('em').string
    title=re.sub('\t|\r|\n|','',title)

    #본문 찾아오기 (html 분석하여 기사 본문 담고 있는 html tag  지정)
    content=bs.find('div','fr-view')
  

    content = content.text
    
    content=re.sub('\u200b|\xa0|\t|\r|\n|[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]','',content)

    return '제목'+' '+title+' '+content


#10개의 url을 통해 각 뉴스기사 페이지의 본문을 가져온다.
news_content = []
for url in news_url_list:
    news_content.append(get_news_by_url(url))

#10개의 뉴스기사 본문에서 요약문장을 추출한다.
sentences=[]
stopword = {'제목', '제작', '학생', '교수'}

kiwi= Kiwi()

for idx in range(0, len(news_content)):
    sentences = kiwi.split_into_sents(news_content[idx])
    texts = []
    idx1=0

    for idx1 in range(0, len(sentences)):
        texts.append(sentences[idx1].text)


    sents1 = [normalize(text, english=True, number=True) for text in texts]
    keywords, sents = summarize_with_sentences(sents1, stopwords = stopword, num_keysents=2, scaling=lambda x:0.5, verbose=False)


    tts_ko = gTTS(text=' '.join(sents), lang='ko')
    tts_ko.save("news"+str(idx+1)+".mp3")

