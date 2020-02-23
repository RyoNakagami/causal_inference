# INTRODUCTION

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Dataの種類](#data%E3%81%AE%E7%A8%AE%E9%A1%9E)
  - [Microeconomic data](#microeconomic-data)
  - [Macroeconomic data](#macroeconomic-data)
  - [Financial data](#financial-data)
- [Data分析の種類](#data%E5%88%86%E6%9E%90%E3%81%AE%E7%A8%AE%E9%A1%9E)
- [Statistical Data types](#statistical-data-types)
  - [Cross-sectional Data](#cross-sectional-data)
  - [Time Series Data](#time-series-data)
  - [Panel (or Longitudinal) data](#panel-or-longitudinal-data)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Dataの種類

Dataは様々な尺度で集められる。経済学でよく用いられるデータを大きく分けると、(1) Microeconomic data, (2) Macroeconomic data, (3) Financial dataに分けられる。

### Microeconomic data

- Company/Business/Industry data - sales, expenses, supply, etc.
- Individual-specific (i.e. household) data - income, employment, education, family members, age, gender, etc.

### Macroeconomic data

- Population census data - unemployment rate, income percentiles etc.;
- Inflation rate;
- Housing market data (home ownership, rent percentage, etc.);
- Supply of oil, wood, water, electricity and metal, etc.;

### Financial data

- the trading volume and value of specific stocks or commodities (gold and other metals, food, energy, etc.)

## Data分析の種類

データから何かしらのインサイトを得てそれを施策に反映させるのがデータ分析の存在理由だが、この作業のためには (1) Dataをシステム化及び整備する, (2) データを分析する、というそれぞれのタスクを実施する必要がある。

データ分析には統計的及び計量経済学的手法にフォーカスしてデータを分析するような解釈性（causality）を重視する手法や、機械学習アルゴリズムをデータにアプライして予測性を重視する手法などある。Data scientistの必要条件として、どちらの手法にも精通しているとしておく。


## Statistical Data types
### Cross-sectional Data

Cross-sectional Dataとは、index (unit of observation) がindividual unit (people, companies, countries, etc.)で特徴付けられるデータのこと。timeはindexに絡まず、Cross-sectional Dataは一つの時系列の断面で収集されたデータであると扱われる。

- Student grades at the end of the current semester;
- Household data of the previous year - expenditure on food, unemployment, income, etc.
- Car data - average speed, horsepower, color, etc.

Cross-sectional Dataではindexのorderingは意味を有してはいない。PythonでCross-sectional dataの例を取得したい場合は、

```python
import statsmodels.api as sm
#
cars = sm.datasets.get_rdataset("cars", "datasets")
print(cars.data.head())
```

Then,

```
##    speed  dist
## 0      4     2
## 1      4    10
## 2      7     4
## 3      7    22
## 4      8    16
```

### Time Series Data

Time Series Dataとはdataのindexがtimeとなっているデータのことを指す。データ対象の主体は基本的には全て同一のindividual unitであるとされる。

- stock prices
- interest rates
- exchange rates
- product prices
- GDP, etc.

Cross-sectional Dataと異なりindexの順序が意味を有している。PythonでのTime Series Dataのサンプルは

```python
money = sm.datasets.get_rdataset("Money", "Ecdat")
print(money.data.head(6))
```

Then, quarterly observations of Money, GDP and Interest Rate in Canada, where m is the log of the real money supply, y is the log of GDP in 1992 dollars, seasonally, adjusted; p is the log of the price level and r is the 3-month treasury till rate.

```
##           m         y        p        r
## 0  11.21111  12.62052 -1.49969  4.46333
## 1  11.21075  12.64173 -1.48955  4.17333
## 2  11.20382  12.64643 -1.48414  4.47333
## 3  11.17621  12.65076 -1.47146  5.45333
## 4  11.14330  12.65842 -1.45747  6.69000
## 5  11.11438  12.68715 -1.45569  6.83333
```

### Panel (or Longitudinal) data

このrepositoryではPanel dataという用語で統一する。Panel dataとはunit of observaionが `(individual unit, time)` で特徴付けられているデータのことを指す。一般的には、それぞれのindividual unitに対して同じ期間の長さでデータが取得されている`balanced panel`というデータ形式が取り扱われる。

Grunfeld Investment Data - a panel of 10 observations from 1935 to 1954 in the US, where firm is the firm ID, year is the date, inv is the gross investment, value is the value of the firm and capital is the stock of plant and equipment.

```python
grunfeld = sm.datasets.get_rdataset("Grunfeld", "plm")
print(grunfeld.data.head(40))
```

Then,

```
##     firm  year     inv   value  capital
## 0      1  1935   317.6  3078.5      2.8
## 1      1  1936   391.8  4661.7     52.6
## 2      1  1937   410.6  5387.1    156.9
## 3      1  1938   257.7  2792.2    209.2
## 4      1  1939   330.8  4313.2    203.4
## 5      1  1940   461.2  4643.9    207.2
## 6      1  1941   512.0  4551.2    255.2
## 7      1  1942   448.0  3244.1    303.7
## 8      1  1943   499.6  4053.7    264.1
## 9      1  1944   547.5  4379.3    201.6
## 10     1  1945   561.2  4840.9    265.0
## 11     1  1946   688.1  4900.9    402.2
## 12     1  1947   568.9  3526.5    761.5
## 13     1  1948   529.2  3254.7    922.4
## 14     1  1949   555.1  3700.2   1020.1
## 15     1  1950   642.9  3755.6   1099.0
## 16     1  1951   755.9  4833.0   1207.7
## 17     1  1952   891.2  4924.9   1430.5
## 18     1  1953  1304.4  6241.7   1777.3
## 19     1  1954  1486.7  5593.6   2226.3
## 20     2  1935   209.9  1362.4     53.8
## 21     2  1936   355.3  1807.1     50.5
## 22     2  1937   469.9  2676.3    118.1
## 23     2  1938   262.3  1801.9    260.2
## 24     2  1939   230.4  1957.3    312.7
## 25     2  1940   361.6  2202.9    254.2
## 26     2  1941   472.8  2380.5    261.4
## 27     2  1942   445.6  2168.6    298.7
## 28     2  1943   361.6  1985.1    301.8
## 29     2  1944   288.2  1813.9    279.1
## 30     2  1945   258.7  1850.2    213.8
## 31     2  1946   420.3  2067.7    132.6
## 32     2  1947   420.5  1796.7    264.8
## 33     2  1948   494.5  1625.8    306.9
## 34     2  1949   405.1  1667.0    351.1
## 35     2  1950   418.8  1677.4    357.8
## 36     2  1951   588.2  2289.5    342.1
## 37     2  1952   645.5  2159.4    444.2
## 38     2  1953   641.0  2031.3    623.6
## 39     2  1954   459.3  2115.5    669.7
```

