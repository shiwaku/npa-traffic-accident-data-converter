# -*- coding: utf-8 -*-
# 地点の緯度経度を10進法度表記に変換する
import pandas as pd
import csv

def CsvFileConvert():
    # 出力CSVファイルオープン
    output_csvfile = "./honhyo_2019-2021_to-degree.csv"
    with open(output_csvfile, 'a', encoding='UTF-8') as f:
        # ヘッダー行出力
        fieldnames = ['資料区分', '都道府県コード', '警察署等コード', '本票番号', '事故内容', '死者数', '負傷者数', '路線コード', '上下線', '地点コード', '市区町村コード', '発生日時_年', '発生日時_月', '発生日時_日',
                      '発生日時_時', '発生日時_分', '昼夜', '天候', '地形', '路面状態', '道路形状', '環状交差点の直径', '信号機', '一時停止規制_標識（当事者A）', '一時停止規制_表示（当事者A）', '一時停止規制_標識（当事者B）', '一時停止規制_表示（当事者B）',
                      '車道幅員', '道路線形', '衝突地点', 'ゾーン規制', '中央分離帯施設等', '歩車道区分', '事故類型', '年齢（当事者A）', '年齢（当事者B）', '当事者種別（当事者A）', '当事者種別（当事者B）', '用途別（当事者A）', '用途別（当事者B）',
                      '車両形状（当事者A）', '車両形状（当事者B）', '速度規制（指定のみ）（当事者A）', '速度規制（指定のみ）（当事者B）', '車両の衝突部位（当事者A）', '車両の衝突部位（当事者B）', '車両の損壊程度（当事者A）', '車両の損壊程度（当事者B）',
                      'エアバッグの装備（当事者A）', 'エアバッグの装備（当事者B）', 'サイドエアバッグの装備（当事者A）', 'サイドエアバッグの装備（当事者B）', '人身損傷程度（当事者A）', '人身損傷程度（当事者B）', '地点_緯度（北緯）', '地点_経度（東経）', '曜日(発生年月日)', '祝日(発生年月日)',
                      '地点_緯度（北緯）_10進数', '地点_経度（東経）_10進数']
        csvfile_writer = csv.DictWriter(
            f, fieldnames=fieldnames, lineterminator='\n')
        csvfile_writer.writeheader()

        # CSVファイルをデータフレームに格納
        data = pd.read_csv("./honhyo_2019-2021.csv", dtype=object).values.tolist()

        print(len(data))
        for i in range(len(data)):
            # 緯度経度（60進数）を取得
            lat = str(data[i][54])  # 地点　緯度（北緯）ex)431412959
            lng = str(data[i][55])  # 地点　経度（東経）ex)1414947029
            # 緯度経度の文字数をチェック
            if len(lat) == 9 and len(lng) == 10:
                # 緯度経度を10進数に変換
                clat = float(lat[0:2]) + float(lat[2:4]) / \
                    60 + (float(lat[4:9]) / 1000) / 3600
                clng = float(lng[0:3]) + float(lng[3:5]) / \
                    60 + (float(lng[5:10]) / 1000) / 3600

                # 出力CSVファイルに書き込む
                csvfile_writer.writerow({
                    '資料区分': data[i][0], '都道府県コード': data[i][1], '警察署等コード': data[i][2], '本票番号': data[i][3], '事故内容': data[i][4], '死者数': data[i][5],
                    '負傷者数': data[i][6], '路線コード': data[i][7], '上下線': data[i][8], '地点コード': data[i][9], '市区町村コード': data[i][10],
                    '発生日時_年': data[i][11], '発生日時_月': data[i][12], '発生日時_日': data[i][13], '発生日時_時': data[i][14], '発生日時_分': data[i][15],
                    '昼夜': data[i][16], '天候': data[i][17], '地形': data[i][18], '路面状態': data[i][19], '道路形状': data[i][20],
                    '環状交差点の直径': data[i][21], '信号機': data[i][22], '一時停止規制_標識（当事者A）': data[i][23], '一時停止規制_表示（当事者A）': data[i][24], '一時停止規制_標識（当事者B）': data[i][25],
                    '一時停止規制_表示（当事者B）': data[i][26], '車道幅員': data[i][27], '道路線形': data[i][28], '衝突地点': data[i][29], 'ゾーン規制': data[i][30],
                    '中央分離帯施設等': data[i][31], '歩車道区分': data[i][32], '事故類型': data[i][33], '年齢（当事者A）': data[i][34], '年齢（当事者B）': data[i][35],
                    '当事者種別（当事者A）': data[i][36], '当事者種別（当事者B）': data[i][37], '用途別（当事者A）': data[i][38], '用途別（当事者B）': data[i][39], '車両形状（当事者A）': data[i][40],
                    '車両形状（当事者B）': data[i][41], '速度規制（指定のみ）（当事者A）': data[i][42], '速度規制（指定のみ）（当事者B）': data[i][43], '車両の衝突部位（当事者A）': data[i][44], '車両の衝突部位（当事者B）': data[i][45],
                    '車両の損壊程度（当事者A）': data[i][46], '車両の損壊程度（当事者B）': data[i][47], 'エアバッグの装備（当事者A）': data[i][48], 'エアバッグの装備（当事者B）': data[i][49], 'サイドエアバッグの装備（当事者A）': data[i][50],
                    'サイドエアバッグの装備（当事者B）': data[i][51], '人身損傷程度（当事者A）': data[i][52], '人身損傷程度（当事者B）': data[i][53], '地点_緯度（北緯）': data[i][54], '地点_経度（東経）': data[i][55],
                    '曜日(発生年月日)': data[i][56], '祝日(発生年月日)': data[i][57], '地点_緯度（北緯）_10進数': clat, '地点_経度（東経）_10進数': clng
                })

    print(u'処理終了')

CsvFileConvert()
