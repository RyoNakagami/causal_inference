# 効果検証入門勉強会
## Purpose and Goals
- 因果推論の基本的フレームワークを身に着ける
- ビジネスシーンにどのように因果推論フレームワークを適用するかを学ぶ
- 安井翔太著，株式会社ホクソエム監修，「効果検証入門～正しい比較のための因果推論／計量経済学の基礎」，技術評論社，2020をPythonで実践してみる

### sub-goals
- RからPythonへの翻訳
- 統計量算出の仮定など、明示されていない前提条件とそのインパクトを理解する
- 可読性の高いコードの書き方を身につける（コードをみるだけで意図が伝わる形を目指す）

## Frequency
- Lectures: 2 sessions / week, 1 hours / session
- AM 8:00 ~ (planned)

## Textbook
- [安井翔太著，株式会社ホクソエム監修，「効果検証入門～正しい比較のための因果推論／計量経済学の基礎」，技術評論社，2020.](https://www.amazon.co.jp/%E5%8A%B9%E6%9E%9C%E6%A4%9C%E8%A8%BC%E5%85%A5%E9%96%80%E3%80%9C%E6%AD%A3%E3%81%97%E3%81%84%E6%AF%94%E8%BC%83%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E5%9B%A0%E6%9E%9C%E6%8E%A8%E8%AB%96-%E8%A8%88%E9%87%8F%E7%B5%8C%E6%B8%88%E5%AD%A6%E3%81%AE%E5%9F%BA%E7%A4%8E-%E5%AE%89%E4%BA%95-%E7%BF%94%E5%A4%AA/dp/4297111179)

## Description
- statistical inference, regression, generalized least squares, instrumental variables, simultaneous equations models, and programm evaluation, difference-in-differences, synthetic control method
- テキストのRコードサンプルを読み込んだうえで、それをPythonで再現する

## Computation
- Python (primary)
- R
- (C, SQL etc)

Computationという観点では、主にPythonを用いる予定。今回取り扱うテキスト「効果検証入門」がRを用いており、それをPythonに翻訳するのがこのコースの目的の一つであるため、Rが読める程度のスキルがあると好ましい。C, SQLは、なくても困らない。

## Prerequisites
### Mathematics
- 線形代数の入門コースを受講したことある（computationでnumpyを用いた行列演算際に役に立つ）
- [MIT MathCamp](https://stellar.mit.edu/S/project/mathprefresher/materials.html)
- 参考資料(ここまで必要ないが紹介)：[Greene Mathematical Appendix](http://pages.stern.nyu.edu/~wgreene/Text/Greene-EA-7&8ed-Appendices.pdf)

### Probability and statistics
- 参考資料(読む必要ないが紹介)：[統計学のための数学入門30講 ](https://www.amazon.co.jp/%E7%B5%B1%E8%A8%88%E5%AD%A6%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%95%B0%E5%AD%A6%E5%85%A5%E9%96%8030%E8%AC%9B-%E7%A7%91%E5%AD%A6%E3%81%AE%E3%81%93%E3%81%A8%E3%81%B0%E3%81%A8%E3%81%97%E3%81%A6%E3%81%AE%E6%95%B0%E5%AD%A6-%E6%B0%B8%E7%94%B0-%E9%9D%96/dp/4254116330)

### Programming skills
- わからないことあったらまず公式documentを読む精神の持ち主

## 実行環境
- リポジトリの Jupyter Notebook は Google Colab 上で実行されることを想定

## 参考文献
- Angrist, J. D., and J. S. Pischke. Mostly Harmless Econometrics: An Empiricist's Companion. Princeton University Press, 2009. ISBN: 9780691120355. 