# medalgame_simulation

### 本アプリの目的

**メダルゲームのシミュレーション**を、streamlit 上で気軽に行えるようにする。

### リポジトリ構造

<pre>

├───lib : pagesで利用する関数の格納先フォルダ
│   ├───simulation_funcs : シミュレーションの際に動作する関数の格納先フォルダ
│   └───widget_funcs : pagesのwidgetに関係する関数を管理するフォルダ
│
└───pages : シミュレーションを行うページの格納先フォルダ
│    └───__pycache__ : 無視しておk
|
├───README.md : 本ページの記載情報
└───アプリ情報.py : 本アプリについて説明を行うページのタブ
