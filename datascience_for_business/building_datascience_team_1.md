# データサイエンスチーム構築にあたってのメモ その１
## Agenda

- Datascience teamがDurable Valueを発揮するためのplatformをどのように構築するか
- Agileでdata science projectを回すためには？

## 参考
- [Is Your Data Science Team Agile?](https://blog.rstudio.com/2020/06/09/is-your-data-science-team-agile/)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [1. Collaboration Through a Centralized Data and Analytics Platform](#1-collaboration-through-a-centralized-data-and-analytics-platform)
  - [課題認識](#%E8%AA%B2%E9%A1%8C%E8%AA%8D%E8%AD%98)
  - [環境構築の必要条件](#%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89%E3%81%AE%E5%BF%85%E8%A6%81%E6%9D%A1%E4%BB%B6)
  - [Why](#why)
- [2. Agileでdata science projectを回すためには？](#2-agile%E3%81%A7data-science-project%E3%82%92%E5%9B%9E%E3%81%99%E3%81%9F%E3%82%81%E3%81%AB%E3%81%AF)
  - [Obstacle](#obstacle)
  - [Solution](#solution)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## 1. Collaboration Through a Centralized Data and Analytics Platform
### 課題認識

Data science teamがdataからvaluable insightやtoolを導き出したとしても、Business Valueに結びつかない場合は多々ある。その要因例として、

- Lack of reuse: 毎回毎回from scratchでコードを書かなくてはならず労働生産効率が悪い。分析時間がかかってしまいBusiness decision makerが求めるタイミングでの分析insightの提出ができなくなる
- Lack of reproducibility: 再現性がなければ信用できない
- Stale insights and repetitive work：データが更新されず、古いデータを何回も使いまわして分析し、その結果を伝えなくてはならない

### 環境構築の必要条件

Data science teamがbusiness valueを発揮するための必要条件として、

- 適切な分析環境が与えられている
- Project-basedで各Data scientistが同じ分析環境を共有して、その中で分析業務を遂行している
- 分析環境がcloud上で構築されていること
- 分析者がビジネスモデルを理解できるようにthe sales and marketing strategyを担当している方とのコミュニケーション環境を構築する

ことがあげられる。

### Why

1. 一人が構築したpackageを他のdata scientistがminimum effortで(1)各自の分析業務に反映, (2) （広い意味でconflict問題の検討など）collaborationを実行できるようにするため
2. Version controlが容易になる
3. Hardware maintenance costを低減させることができる（エンジニアはエンジニア、分析者は分析に集中）
4. remote workが可能となる

(1), (2)点目は`virtualenv`などの環境構築コマンドを用いても達成することはできる。

## 2. Agileでdata science projectを回すためには？
### Obstacle

1. Training on new tools
2. Monolithic applications: Implementationに数ヶ月かかってしまう
3. Slow exploratory development：Good data science requires the ability to rapidly explore many approaches to solving a problem and to revise proposed solutions with colleagues and stakeholders.
4. Difficult to share and access results:

### Solution

1. Use tools many data scientists already know (業界マジョリティを使いましょう)
2. Focus on small prototypes to prove value, using tools that integrate with your existing frameworks（Agile開発として）
3. Rapid, code-based development：Feedbackを効率的に得られる仕組みを作る（workshopやビジネス意思決定者とのコミュニケーションの機会など）
4. BI dashboardや分析結果共有を円滑化する環境を構築する

<img src = 'https://github.com/RyoNakagami/omorikaizuka/blob/master/データ分析基盤/agile_datascience.jpg?raw=true'>