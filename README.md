# json2geojson4ikoma
## 2019.10.7 初版 


# json2geojson4ikoma
## 生駒市オープンデータポータルサイトにあるjsonファイルのうち、緯度経度情報を含むものをgeojson形式に変換します。

 [生駒市オープンデータポータルサイト](https://data.city.ikoma.lg.jp/)



《使い方》

json2geojson4ikoma XXX.json

XXX.json: 生駒市オープンデータポータルサイトよりダウンロードしてきたjsonファイル(緯度経度情報を含むもの)

同じディレクトリにXXX.geojsonとう名前のファイルを作成します。


[GeoJSONフォーマット仕様]( https://s.kitazaki.name/docs/geojson-spec-ja.html)



ここで変換されたGeoJSON形式のファイルは、たとえば下記ハンズオンで行われているように
Tellus OSで取り込みことが可能です。

[TELLUS OS](https://www.tellusxdp.com/ja/)
（ユーザ登録(初回)、ログインが必要です)


【前編】Tellusとオープンデータで子育てしやすい地域を探してみよう(鎌倉市編）
https://qiita.com/ueki_kensuke/items/b7581123aa13765f02da

【後編】Tellusとオープンデータで子育てしやすい地域を探してみよう(鎌倉市編）
https://qiita.com/ueki_kensuke/items/e51c227d488449df64b0

## 作成者
- Takao Ikoma tikoma@gmail.com

ライセンスについて
このソフトウェアは、MITライセンスでのもとで公開されています。LICENSE.txtを見てください。

