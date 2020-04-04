# 因果推論とビジネス

||概要|
|---|----|
|更新日|2020-04-04 Saturday 17:54:45|
|目的|因果推論と機械学習はビジネスにおいてどのように使われるのか？|
|参考文献|EEconomists (and Economics) in Tech Companies, Susan Athey, Michael Luca, Journal of Economic Perspectives. December 2019, Vol. 33, Issue 1, Pages 209-230,  <br>経済セミナー 2020年4・5月号　通巻 713号|

## Economistのskill-set

- dataの解釈: causal relationship or not
- incentive design
- equilibrium behaviorの定式化

## どのようなBusiness fieldでEconomistは活躍しているのか？

- pricing
- policy変更の効果検証及び実験計画立案
- incentive design
- data handling

## 因果推論とMLは補完財

因果推論は次の意味でMLと補完財と考えることができる
 
- 機械学習を用いたサービスの導入は、最終的にはRCT、因果推論によってKPIに対する効果を検証される。
- 最終的に検証される因果効果を最大化する形でmodel learningを設計することで、ビジネス価値を最大化するMLサービスが作れる

## 実験計画とMetrics

Metricsはshort-term, long-termの軸で考えるべき

- short-term: clicks on an advertisement
- long-term: the lifetime value of a customer

## Appendix

|論文|説明|
|---|---|
|Blake and Coey (2014)|equilibirum effectとRCT|
|Athey, Eckles, and Imbens (2018)|Network effectとRCT|
|Hitsch and Misra (2018)|causal forest and targeted promotions|
|Athey and Imbens (2016) |causal forest and RCT|
|Edelman, Luca, and Svirsky (2017)|人種差別とAirbnb サービス機能とRCT|
|Cohen, Hahn, Hall, Levitt, and Metcalfe 2016|market design and Uber for ride|








