# findpaws

### 簡介：
使用框架Django製作一個簡單的流浪動物網站，希望讓民眾可以輕鬆地瀏覽流浪動物資料，看到喜歡的動物就可以進一步聯絡動物連絡人
***
### 技術：
* django
* python
* mariadb
* pipenv（建立專案環境）
***
### 功能需求：
第一階段 (finish)
1. 能瀏覽目前收容所、送養、走失公告的動物簡介資料。
2. 點擊連結進入動物詳細資料頁面
    1. 照片、基本資料（品種性別毛色體型各種特徵描述）、聯絡人、地點

第二階段
1. 寫爬蟲爬下各大收容所網站資料，塞入db
2. 動物頁面增加條件搜尋：地點、年齡、體型、（品種）（未完成）

第三階段
1. 會員註冊、會員認證
2. 會員資料頁、資料修改
3. 收藏動物功能
4. 留言系統（會員認證後）
5. 送養、走失刊登功能（會員認證後）
***
### 網頁外觀
https://drive.google.com/open?id=1WBx6DMhmOKLFV-wX-SjD4Yhw_fT91MDPkljD6f4s4q8
***
### 建立專案
1. 安裝python  
   `（略）`
2. 安裝pipenv  
    `$ pip3 install pipenv`
3. cd至想要的目錄後，初始一個專案  
   `$ pipenv --python 3.7 # 本專案用python3.7`
4. 根據pipfile安裝必要的套件  
   `$ pipenv install`
5. 安裝mysql/mariadb、並建立database  
   `（略）`
6. 設定setting.py內的db如下  
 ```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'findpaws',   #database name
        'USER': 'root',       #mysql user name
        'PASSWORD':'12345',   #mysql user password
        'HOST': 'localhost', 
        'PORT': '3306'
    }
}
 ```
### 啟用步驟
1. enter pipenv environment  
 `$ pipenv shell`

2. do the table migration  
 `$ python3 manage.py migrate ` 
3. run server  
`$ python3 manage.py runserver`  
`註：我是用django admin後台建立資料並存在local的db，所以直接開啟網頁後不會有資料`
1. 刪除專案  
   `pipenv --rm`


