<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [因果推論と予測問題とIssue-Solving](#%E5%9B%A0%E6%9E%9C%E6%8E%A8%E8%AB%96%E3%81%A8%E4%BA%88%E6%B8%AC%E5%95%8F%E9%A1%8C%E3%81%A8issue-solving)
  - [はじめに](#%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB)
  - [天気の実証分析](#%E5%A4%A9%E6%B0%97%E3%81%AE%E5%AE%9F%E8%A8%BC%E5%88%86%E6%9E%90)
    - [予算管理と予測の違い](#%E4%BA%88%E7%AE%97%E7%AE%A1%E7%90%86%E3%81%A8%E4%BA%88%E6%B8%AC%E3%81%AE%E9%81%95%E3%81%84)
  - [Prediction and Causation (一般化)](#prediction-and-causation-%E4%B8%80%E8%88%AC%E5%8C%96)
  - [Bias-variance trade-off](#bias-variance-trade-off)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 因果推論と予測問題とIssue-Solving

||概要|
|---|---|
|更新日|2020-02-25 Tuesday 20:02:55|
|目的|どのような場面で因果推論、predictionが重視されるのかをまとめる|
|参考|[Prediction Policy Problems](https://www.aeaweb.org/articles?id=10.1257/aer.p20151023)|


<!-- START DOCTOC -->
<!-- END DOCTOC -->

## はじめに

Empirical researchの多くは因果推論にフォーカスしている。企業の投資判断なり、政府の新しい政策の判断は、そのPolicyを実施した時と実施しなかった時、意思決定主体が設定しているKPIに対する影響（因果）に基づいているはずなので自然なことと思われる。ただし、因果推論がメインでない実証分析も存在する。

## 天気の実証分析

以下の二つの天気の実証分析シナリオを考える：

- ある村では干ばつに見舞われ、あと一週間雨が降らないと村の農作物が全滅してしまうと考えられている。現在、村長は雨が降る確率を高めることを目的とした雨乞いダンスを実施するか否かを悩んでいる
- 会社員であるAさんが出社のため家を出ようとした際、遠く西の空にいかにも大雨を降らせそうな雲が漂っているのが見えた。Aさんは雨に濡れることが大嫌いであるが、荷物が増えることも嫌う人間。家の傘を持って出かけるべきか否かの意思決定をAさんは今しなくてはならない

どちらも天気の実証分析に関わる問題だが、前者のIssueは雨乞いダンスが雨を降らせる確率を高めるのか？という因果分析が重要である一方、後者のIssueは雨が今日降るのか降らないのか？の予測分析が重要となる。

|Main Issue|例|Skill||
|---|---|---|----|
|因果分析|値下げによる売り上げuplift|計量経済学、統計|paremeter推定のunbiasedness, consistency, efficiencyを重視|
|予測|一週間後の販売在庫数量管理|ML(non-parametricの一種)、統計|予測精度を重視|

### 予算管理と予測の違い

機械学習や計量経済学のスキルを用いて取り組む予測問題と予算管理の予算管理は主眼点が異なる。前者の予測問題は、$Y_t$を現在t期における売り上げだとすると$E[Y_{t+1}|Y_t]$の推定量を作成し、それを計算して来季t+1期の売り上げの推定値を得ることがメイン。一方、後者で取り組む予測問題は、季節調整や前期実績を踏まえた現実的な予測売り上げ（$E[Y_{t+1}|Y_t]$）を考慮した上で、組織の成長戦略からブレイクダウンされる数字をベースに売り上げ目標という形で数字を計算する。いわゆるOKR的側面が強い。

## Prediction and Causation (一般化)

- $Y$ : outcome variable, 売り上げや客数
- $X$ : treatment level, チラシ販売枚数や倉庫人員
- $\Pi(\cdot, \cdot)$: Payoff function, which should be maximized

$$
\frac{d\Pi(X, Y)}{d X} = \frac{\partial \Pi}{\partial X}\underbrace{(Y)}_{\text{prediction}} + \frac{\partial \Pi}{\partial Y}\underbrace{\frac{\partial Y}{\partial X}}_{\text{causation}}
$$

因果推論で扱うタームは$\frac{\partial Y}{\partial X}$。この項は、XがYをどれだけ押し上げるのか？に関連する項目。このパラメーターを出すことで、意思決定をサポートするのが因果推論分析の役割の一つ（Xという投資意思決定した方が良いのか？とか）。

もう一つの未知のパラメーター$\frac{\partial \Pi}{\partial X}\underbrace{(Y)}_{\text{prediction}}$はXがPayoff functionに与える影響がYの水準に依存する状況を示している。例として、来季HTが100枚売れるならば、Xを来季HT在庫数量とする時、$X = 100$がちょうど良さそうだが、一方1000枚売れる場合は、$X = 1000$にすべきという状況。

- causation重視：この打ち手が本当に正しかったのか検証したい場合
- prediction重視：状況に応じた打ち手は定式化されているが、どのような状況が到来するかわからない場合

## Bias-variance trade-off

- $D$: dataset of n points, $(y_i, x_i) \sim G$
- $F$: estimator set
- $F_{lin}$: linear estimator set

OLSがやっていることは

$$
\hat f_{OLS} = \argmin_{f_{\beta\in F_{lin}}\sum_{i= 1}^{n}(y_i - f(x_i))^2
$$

より具体的にここでのOLSは
$$
Y_i = \beta_1 + \beta_2 x_i + \epsilon_i
$$
を推定しているとする。この時、OLS estimatesが$\hat\beta_1 = 1(1 \pm 0.01)$, $\beta_2 = 4*(1\pm 0.04)$という値を出したとする。predictionを重視する分析を実施する場合、out-of-sampleでの予測精度を追求するので、$\hat\beta$のパラメーター推定誤差を考えると、$|\beta|$を小さくすることで予測誤差の範囲を小さくすることができる。

実際にこの方針はBias-variance decompositionで定式化して考えることができる。

$$
\begin{aligned}
\mathbb{E} \left[ \left( Y - \widehat{f}(X) \right)^2\right] &= \mathbb{E} \left[ \left( Y^2 + \widehat{f}^2(X) - 2 Y \widehat{f}(X) \right)\right]\\
&= \mathbb{E}\left[ Y^2\right] + \mathbb{E}\left[ \widehat{f}^2(X)\right] - 2 \mathbb{E}\left[ Y \widehat{f}(X)\right] \\
&= \mathbb{V}{\rm ar}\left[Y \right] + (\mathbb{E}[Y])^2 + \mathbb{V}{\rm ar}\left[\widehat{f}^2(X) \right] + \left(\mathbb{E}[\widehat{f}(X)] \right)^2 -2 \mathbb{E}\left[ Y \widehat{f}(X)\right] \\
&= \mathbb{V}{\rm ar}\left[Y \right] + \mathbb{V}{\rm ar}\left[\widehat{f}^2(X) \right] + \left( \mathbb{E}[Y] - \mathbb{E}\left[\widehat{f}(X)\right]\right)^2 \\
&= \sigma^2 + \mathbb{V}{\rm ar}\left[\widehat{f}^2(X) \right] + \left( \mathbb{E}\left[\widehat{f}(X)\right] - f(X)\right)^2 
\end{aligned}
$$

MLの手法はこの側面を重視しており、実際に線形回帰クラスの推定量でもLasso, Ridge regressionを用いている。

$$
\hat f_{ML} = \argmin_{f\in F}\sum_{i = 1}^n (y_i - f(x_i))^2 = \lambda R(f)
$$

- $R(f)$: regularizer, 推定値のvarianceを生み出す要因に対してペナルティを科している
- 一般的には$R(f_{\beta}) = ||\beta||^d$, $d = 1, 2$ならばそれぞれlasso, ridge
- OLSは$\lambda = 0$で推定していると理解できる
- $\lambda$の値の導出の仕方はcross-validationという手法を用いる（dataをf個のfoldsと呼ばれるsubsetに分けて、f-1のfoldsを用いて推定アルゴリズムを回し、その結果を用いてf fold用の$\lambda$を推定して、パラメーターを計算する）
- LassoとridgeはIFV対策に有効（Inflating variance factor）
