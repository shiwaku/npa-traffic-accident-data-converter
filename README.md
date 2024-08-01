# npa-traffic-accident-data-converter
- 本プログラムは、警察庁が公開している、[交通事故統計情報のオープンデータ（2019年、2020年、2021年）の本票](https://www.npa.go.jp/publications/statistics/koutsuu/opendata/index_opendata.html)を[コード表](https://www.npa.go.jp/publications/statistics/koutsuu/opendata/index_opendata.html)を元に読みやすいデータ（GISデータ）に変換するプログラムになります。
- Pythonで構築

## プログラムについて

### csvfile-merge.py
- 本票CSVファイル（2019年、2020年、2021年）をマージするプログラムになります。
- 文字コードをUTF-8に変換します。

#### 使用データ
- `https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/data/honhyo_2019.csv`,66.5MB
- `https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/data/honhyo_2020.csv`,54.0MB
- `https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/data/honhyo_2021.csv`,53.3MB

#### 出力結果
- `https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2021.csv`,173.8MB

### csvfile-to-degree.py
- マージした本票CSVファイル（2019～2021年）の「地点　緯度（北緯）」と「地点　経度（東経）」を十進法度単位に変換するプログラムになります。

#### 使用データ
- `https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2021.csv`,173.8MB

#### 出力結果
- `https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2021_to-degree.csv`,207.4MB  

### csvfile-convert.py
- 十進法度単位に変換した本票CSVファイル（2019～2021年）をコード表を元に読みやすいデータに変換するプログラムになります。

#### 使用データ
- `https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2021_to-degree.csv`,207.4MB  
- コード表`https://github.com/shi-works/traffic-accident-converter/tree/main/code`

hit.csv is based on https://github.com/code4fukui/traffic-accident Thanks!

#### 出力結果
##### csv形式
- `https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2021_convert_v2.csv`,722.4MB  
##### FlatGeobuf形式
- `https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2021_convert_v2.fgb`,1.1GB
##### GeoParquet形式
- `https://xs489works.xsrv.jp/pmtiles-data/traffic-accident/honhyo_2019-2021_convert_v2.parquet`,67.3MB

### 使用データ及び出力結果のライセンスについて
本データセットは[CC-BY-4.0](https://pmtiles-data.s3.ap-northeast-1.amazonaws.com/traffic-accident/LICENSE)で提供されます。使用の際には本レポジトリへのリンクを提示してください。

また、本データセットは交通事故統計情報のオープンデータ（2019年、2020年、2021年）の本票を加工して作成したものです。本データセットの使用・加工にあたっては、[警察庁Webサイトの利用規約](https://www.npa.go.jp/rules/index.html)を必ずご確認ください。

### 免責事項
利用者が当該データを用いて行う一切の行為について何ら責任を負うものではありません。
