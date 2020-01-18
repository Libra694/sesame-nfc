# sesame-nfc
スマートロックSESAMEをNFCで開閉します。<br>
以下のコードを自分用に少し変えています。<br>
[CANDYHOUSE- SuicaでSESAME(セサミ)を解錠 【ラズパイ】](https://jp.candyhouse.co/blogs/how-to/suica%E3%81%A7%E3%82%BB%E3%82%B5%E3%83%9F%E3%82%92%E8%A7%A3%E9%8C%A0-with-%E3%83%A9%E3%82%BA%E3%83%91%E3%82%A4)

## 使い方
0. NFCリーダ ([SONY PaSoRi RC-S380](https://www.amazon.co.jp/gp/product/B00948CGAG)) を購入
1. このレポジトリをクローン/ダウンロード
1. params.jsonに各種設定を書き込む
    1. SESAME ID: [CANDYHOUSE - APIキー取得方法とセサミIDの確認方法](https://jp.candyhouse.co/blogs/how-to/api%E3%82%AD%E3%83%BC%E5%8F%96%E5%BE%97%E6%96%B9%E6%B3%95%E3%81%A8%E3%82%BB%E3%82%B5%E3%83%9Fid%E3%81%AE%E7%A2%BA%E8%AA%8D%E6%96%B9%E6%B3%95)を参考に設定
    1. API Key: 同上
    1. IDm: 設定しないまま実行しNFCをかざすと確認できます
1. `sudo python main.py`
1. sudoなしで実行する方法は[CANDYHOUSE- SuicaでSESAME(セサミ)を解錠 【ラズパイ】](https://jp.candyhouse.co/blogs/how-to/suica%E3%81%A7%E3%82%BB%E3%82%B5%E3%83%9F%E3%82%92%E8%A7%A3%E9%8C%A0-with-%E3%83%A9%E3%82%BA%E3%83%91%E3%82%A4)を参照
