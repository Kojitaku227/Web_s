# coding:utf-8
import urllib3
from bs4 import BeautifulSoup
import certifi

# アクセスするURL
url = "https://www.nikkei.com/markets/kabu/"

# httpsの証明書検証を実行している
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())
r = http.request('GET', url)

soup = BeautifulSoup(r.data, 'html.parser')

# タイトル要素を取得する → <title>経済、株価、ビジネス、政治のニュース:日経電子版</title>
title_tag = soup.title

# 要素の文字列を取得する → 経済、株価、ビジネス、政治のニュース:日経電子版
title = title_tag.string

# タイトルを文字列を出力
print(title)

# span要素全てを摘出する→全てのspan要素が配列に入ってかえされます→[<span class="m-wficon triDown"></span>, <span class="l-h...
span = soup.find_all("span")

# print時のエラーとならないように最初に宣言しておきます。
nikkei_heikin = ""
nikkei_heikin_diff = ""

# for分で全てのspan要素の中からClass="mkc-stock_prices"となっている物を探します
for tag in span:
    # classの設定がされていない要素は、tag.get("class").pop(0)を行うことのできないでエラーとなるため、tryでエラーを回避する
    try:
        # tagの中からclass="n"のnの文字列を摘出します。複数classが設定されている場合があるので
        # get関数では配列で帰ってくる。そのため配列の関数pop(0)により、配列の一番最初を摘出する
        # <span class="hoge" class="foo">  →   ["hoge","foo"]  →   hoge
        string_ = tag.get("class").pop(0)

        # 摘出したclassの文字列にmkc-stock_pricesと設定されているかを調べます
        if string_ in "mkc-stock_prices":
            # mkc-stock_pricesが設定されているのでtagで囲まれた文字列を.stringであぶり出します
            nikkei_heikin = tag.string
            # 摘出が完了したのでfor分を抜けます
            break
    except:
        # パス→何も処理を行わない
        pass

# Tag_2変数にspan要素を代入
for tag_2 in span:
    # classの設定がされていない要素は、tag.get("class").pop(0)を行うことのできないでエラーとなるため、tryでエラーを回避する
    try:
        # tagの中からclass="n"のnの文字列を摘出します。複数classが設定されている場合があるので
        # get関数では配列で帰ってくる。そのため配列の関数pop(0)により、配列の一番最初を摘出する
        # <span class="hoge" class="foo">  →   ["hoge","foo"]  →   hoge
        string_ = tag_2.get("class").pop(0)

        # 摘出したclassの文字列にmkc-stock_pricesと設定されているかを調べます
        if string_ in "cmn-plus":
            # mkc-stock_pricesが設定されているのでtagで囲まれた文字列を.stringであぶり出します
            nikkei_heikin_diff = tag_2.string
            # 摘出が完了したのでfor分を抜けます
            break
    except:
        # パス→何も処理を行わない
        pass


# 摘出した日経平均株価を出力します。
print (nikkei_heikin)
print (nikkei_heikin_diff)
print ("test branch!!!!")