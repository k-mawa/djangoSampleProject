# djangoSampleProject
django Sample Project
django製のサンプルプロジェクトです。
徐々に機能拡張していきます。

# アーキテクチャ

カスタムしやすいようにDjangoローカル初期設定です。

 - DB:sqlite3
 - 静的ファイルストレージ:ローカル(非アップロードファイルなど：```static_in_environment/static_root```・```static_in_produciton/our_static```・アップロードファイルなど：```static_in_environment/media_root```)

# 実装済み機能
 - 会員属性DB定義
 - ログイン・ログアウト

# how to use

下記コマンドを入力したらローカルで挙動確認できます。

```
git clone git@github.com:k-mawa/djangoSampleProject.git
cd djangoSampleProject
cd src
python manage.py migrate
python manage.py runserver
```
そのあと、webブラウザで127.0.0.1:8000を確認ください。

then see 127.0.0.1:8000

インデックスページ：IndexPage
![スクリーンショット 2020-10-21 0 05 32](https://user-images.githubusercontent.com/18301772/96605903-ac4d3b80-1331-11eb-8ed7-07f80cbfa986.png)

ログインページ：Login
![スクリーンショット 2020-10-21 0 06 35](https://user-images.githubusercontent.com/18301772/96605914-aeaf9580-1331-11eb-85a7-5ab2f03ebaf0.png)

ログアウトページ：Logout
![スクリーンショット 2020-10-21 0 07 25](https://user-images.githubusercontent.com/18301772/96605918-b0795900-1331-11eb-9e7b-380904f4754a.png)
