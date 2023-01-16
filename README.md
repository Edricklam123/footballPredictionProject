# Football Match Prediction Project

## Literature review

1. [Better Trading Video](https://youtu.be/OJx8gX4bKI0)
2. [Predicting the winning team in basketball: A novel approach](https://www.researchgate.net/publication/366160941_Predicting_the_winning_team_in_basketball_A_novel_approach)
    - Cluster the players into different categories and position using K-means
    - Analyze how the different combination can play against each other

## Goal

- Able to sort the data
- Replicate the Better Trading model to achieve a >75% accuracy
- Applying the player statistics and past trend information, investigate the highest accuracy possible to achieve

## Other ideas

- 前鋒 VS 後衛 成功率等數據
- simulate matches
1. Past 對賽成績
2. Past 5 matches result (trend)
3. 積分榜位置
- 高命中率都未必贏到錢，因為爆冷可以令你輸好多。i.e. 莊家有多過你既Information
- 一定是限投注額而不是限本金，因為要盡可能參與多的賽事才可以讓數據統計學幫助自己

## Datasets details
|                              |                          | start_year | code_name |
|------------------------------|--------------------------|------------|-----------|
| England Football Results     | Premier League           | 9394       | E0        |
| England Football Results     | Championship             | 405        | E1        |
| England Football Results     | League 1                 | 405        | E2        |
| England Football Results     | League 2                 | 405        | E3        |
| England Football Results     | Conference               | 506        | EC        |
| England Football Results     | Division 1               | 9394       | E1        |
| England Football Results     | Division 2               | 9394       | E2        |
| England Football Results     | Division 3               | 9394       | E3        |
| Scotland Football Results    | Premier League           | 9495       | SC0       |
| Scotland Football Results    | Division 1               | 9495       | SC1       |
| Scotland Football Results    | Division 2               | 9798       | SC2       |
| Scotland Football Results    | Division 3               | 9798       | SC3       |
| France Football Results      | Division 2               | 9697       | F2        |
| France Football Results      | Le Championnat           | 9394       | F1        |
| Germany Football Results     | Bundesliga 1             | 9394       | D1        |
| Germany Football Results     | Bundesliga 2             | 9394       | D2        |
| Italy Football Results       | Serie A                  | 9394       | I1        |
| Italy Football Results       | Serie B                  | 9798       | I2        |
| Spain Football Results       | La Liga Primera Division | 9394       | SP1       |
| Spain Football Results       | La Liga Segunda Division | 9697       | SP2       |
| Netherlands Football Results | Eredivisie               | 9394       | N1        |
| Belgium Football Results     | Jupiler League           | 9596       | B1        |
| Portugal Football Results    | Liga I                   | 9495       | P1        |
| Turkey Football Results      | Futbol Ligi 1            | 9495       | T1        |
| Greece Football Results      | Ethniki Katigoria        | 9495       | G1        |
| Argentina Football Results   | ARG                      | new        | ARG       |
| Austria Football Results     | AUT                      | new        | AUT       |
| Brazil Football Results      | BRA                      | new        | BRA       |
| China Football Results       | CHN                      | new        | CHN       |
| Denmark Football Results     | DNK                      | new        | DNK       |
| Finland Football Results     | FIN                      | new        | FIN       |
| Ireland Football Results     | IRL                      | new        | IRL       |
| Japan Football Results       | JPN                      | new        | JPN       |
| Mexico Football Results      | MEX                      | new        | MEX       |
| Norway Football Results      | NOR                      | new        | NOR       |
| Poland Football Results      | POL                      | new        | POL       |
| Romania Football Results     | ROU                      | new        | ROU       |
| Russia Football Results      | RUS                      | new        | RUS       |
| Sweden Football Results      | SWE                      | new        | SWE       |
| Switzerland Football Results | SWZ                      | new        | SWZ       |
| USA Football Results         | USA                      | new        | USA       |