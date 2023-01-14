# 新・明解Pythonで学ぶアルゴリズムとデータ構造

## Chapter 1
### 決定木
パターン網羅の証明方法として少数の組み合わせの場合は**決定木**を活用できる
- 決定木の例: `a, b, c`の大小関係
``` plantuml
@startmindmap
* a >= b
** a > b 
*** b >= c
**** b > c
*****[#lightgreen] a > b > c
*****[#lightgreen] a > c = b

**** a >= c
***** a > c
******[#lightgreen] a > c >b
******[#lightgreen] a = c > b

*****[#lightgreen] c > a > b

*** b >= c
**** b > c
*****[#lightgreen] a = b > c
*****[#lightgreen] a = b = c

****[#lightgreen] c > a = b

** a >= c
*** a > c
****[#lightgreen] b > a > c
****[#lightgreen] b > a = c

*** b >= c
**** b > c
*****[#lightgreen] b > c > a
*****[#lightgreen] b = c > a

****[#lightgreen] c > b > a
@endmindmap
```

### アルゴリズムの処理負荷低減の考え方
1. ループ分の中で判定を行う場合は外に出せないか検討する。  
-> アルゴリズムの世界では柔軟性より高速化が重要
2. 入力受付や処理ごとに変化しない要素については最初から除外してアルゴリズムを考える。

## 書籍情報
- [Amazon](https://www.amazon.co.jp/%E6%96%B0%E3%83%BB%E6%98%8E%E8%A7%A3Python%E3%81%A7%E5%AD%A6%E3%81%B6%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0%E3%81%A8%E3%83%87%E3%83%BC%E3%82%BF%E6%A7%8B%E9%80%A0-%E6%9F%B4%E7%94%B0-%E6%9C%9B%E6%B4%8B-ebook/dp/B0834JWWZG/ref=sr_1_3?adgrpid=77416719506&gclid=Cj0KCQiA_P6dBhD1ARIsAAGI7HA79R_2OQ8WQ0o9-dILqQ8235FRWC7JbTzHTfa7oG7J8EK2GlOSsD0aAgvEEALw_wcB&hvadid=611397546140&hvdev=c&hvlocphy=1009285&hvnetw=g&hvqmt=e&hvrand=8745269407030564082&hvtargid=kwd-846364573423&hydadcr=4077_13255612&jp-ad-ap=0&keywords=python%E3%81%A7%E5%AD%A6%E3%81%B6%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0&qid=1673581721&sr=8-3)
