# django Sample Project 
  
[en]  
django Sample Project This is a sample project made by django. We will gradually expand the functions.It is an MIT license. Feel free to use.
  
# django製のサンプルプロジェクト
  
[日本語]  
django Sample Project
django製のサンプルプロジェクトです。
徐々に機能拡張していきます。MITライセンスですご自由にお使いください
  
# architecture アーキテクチャ 
  
[en]  
Django local defaults for easy customization.

 - DB: sqlite3
 - Static file storage: Local (non-upload files, etc .: `` `static_in_environment / static_root``` ・ ``` static_in_produciton / our_static``` ・ Upload files, etc .: `` `static_in_environment / media_root```)
  
[日本語]  
カスタムしやすいようにDjangoローカル初期設定です。

 - DB:sqlite3
 - 静的ファイルストレージ:ローカル(非アップロードファイルなど：```static_in_environment/static_root```・```static_in_produciton/our_static```・アップロードファイルなど：```static_in_environment/media_root```)
  
# Implemented features 実装済み機能
  
[en]  

 - Member attribute DB definition
 - Login / Logout

[日本語]  
 - 会員属性DB定義
 - ログイン・ログアウト

# Features to be implemented 実装予定の機能
  
[en]  
 - Member registration email authentication
 - Web API by DjangoRESTFramework
 - Web API token authentication by JWT
 - Map display by leaflet.js

[日本語]  
 - 会員登録メール認証
 - DjangoRESTFramework によるWeb API
 - JWTによるWebAPIトークン認証
 - leaflet.jsによる地図表示

# how to use 使い方
  
[en]    
You can check the behavior locally by entering the following command.
  
```
git clone git@github.com:k-mawa/djangoSampleProject.git
cd djangoSampleProject
cd src
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
then see ```127.0.0.1:8000```  
  
[日本語]  
下記コマンドを入力したらローカルで挙動確認できます。

```
git clone git@github.com:k-mawa/djangoSampleProject.git
cd djangoSampleProject
cd src
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
そのあと、webブラウザで```127.0.0.1:8000```を確認ください。

# ScreenShot Photo スクリーンショット

インデックスページ：IndexPage
![スクリーンショット 2020-10-21 0 05 32](https://user-images.githubusercontent.com/18301772/96605903-ac4d3b80-1331-11eb-8ed7-07f80cbfa986.png)

ログインページ：Login
![スクリーンショット 2020-10-21 0 06 35](https://user-images.githubusercontent.com/18301772/96605914-aeaf9580-1331-11eb-85a7-5ab2f03ebaf0.png)

ログアウトページ：Logout
![スクリーンショット 2020-10-21 0 07 25](https://user-images.githubusercontent.com/18301772/96605918-b0795900-1331-11eb-9e7b-380904f4754a.png)
