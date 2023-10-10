```sql
UPDATE fifaDB SET 
        country=country_A, 
        confederation=
        AAAAA,
        population_share=5.0, 
        tv_audience_share=5.0, 
        gdp_weighted_share=5.0,
        WHERE id=3;
```

```sql
DELETE FROM fifaDB WHERE id=1;
```

```sql
UPDATE fifaDB SET 
        country=country_B, 
        confederation=
        BBBBB,
        population_share=5.0, 
        tv_audience_share=5.0, 
        gdp_weighted_share=5.0,
        WHERE id=4;
```

```sql
SELECT * FROM fifaDB;
```

```sql
UPDATE fifaDB SET 
        country=country_A, 
        confederation=
        AAAAA,
        population_share=5.0, 
        tv_audience_share=5.0, 
        gdp_weighted_share=5.0,
        WHERE id=3;
```

```sql
DELETE FROM fifaDB WHERE id=1;
```

```sql
UPDATE fifaDB SET 
        country=country_B, 
        confederation=
        BBBBB,
        population_share=5.0, 
        tv_audience_share=5.0, 
        gdp_weighted_share=5.0,
        WHERE id=4;
```

```sql
SELECT * FROM fifaDB;
```

```sql
UPDATE fifaDB SET 
        country=country_A, 
        confederation=
        AAAAA,
        population_share=5.0, 
        tv_audience_share=5.0, 
        gdp_weighted_share=5.0,
        WHERE id=3;
```

```sql
DELETE FROM fifaDB WHERE id=1;
```

```sql
UPDATE fifaDB SET 
        country=country_B, 
        confederation=
        BBBBB,
        population_share=5.0, 
        tv_audience_share=5.0, 
        gdp_weighted_share=5.0,
        WHERE id=4;
```

```sql
SELECT * FROM fifaDB;
```

```sql
UPDATE fifaDB SET 
        country=country_A, 
        confederation=
        AAAAA,
        population_share=5.0, 
        tv_audience_share=5.0, 
        gdp_weighted_share=5.0,
        WHERE id=3;
```

```sql
DELETE FROM fifaDB WHERE id=1;
```

```sql
UPDATE fifaDB SET 
        country=country_B, 
        confederation=
        BBBBB,
        population_share=5.0, 
        tv_audience_share=5.0, 
        gdp_weighted_share=5.0,
        WHERE id=4;
```

```sql
SELECT * FROM fifaDB;
```

```sql
SELECT * FROM fifaDB;
```

```sql
UPDATE fifaDB SET 
        country=country_A, 
        confederation=
        AAAAA,
        population_share=5.0, 
        tv_audience_share=5.0, 
        gdp_weighted_share=5.0,
        WHERE id=3;
```

```sql
DELETE FROM fifaDB WHERE id=1;
```

```sql
UPDATE fifaDB SET 
        country=country_B, 
        confederation=
        BBBBB,
        population_share=5.0, 
        tv_audience_share=5.0, 
        gdp_weighted_share=5.0,
        WHERE id=4;
```

```sql
SELECT * FROM fifaDB;
```

```sql
UPDATE fifaDB SET 
        country=country_A, 
        confederation=
        AAAAA,
        population_share=5.0, 
        tv_audience_share=5.0, 
        gdp_weighted_share=5.0,
        WHERE id=3;
```

```sql
DELETE FROM fifaDB WHERE id=1;
```

```sql
UPDATE fifaDB SET 
        country=country_B, 
        confederation=
        BBBBB,
        population_share=5.0, 
        tv_audience_share=5.0, 
        gdp_weighted_share=5.0,
        WHERE id=4;
```

```sql
SELECT * FROM fifaDB;
```

```sql
UPDATE fifaDB SET 
        country=country_A, 
        confederation=
        AAAAA,
        population_share=5.0, 
        tv_audience_share=5.0, 
        gdp_weighted_share=5.0,
        WHERE id=3;
```

```sql
DELETE FROM fifaDB WHERE id=1;
```

```sql
UPDATE fifaDB SET 
        country=country_B, 
        confederation=
        BBBBB,
        population_share=5.0, 
        tv_audience_share=5.0, 
        gdp_weighted_share=5.0,
        WHERE id=4;
```

```sql
SELECT * FROM fifaDB;
```

```sql
UPDATE fifaDB SET 
        country=country_A, 
        confederation=
        AAAAA,
        population_share=5.0, 
        tv_audience_share=5.0, 
        gdp_weighted_share=5.0,
        WHERE id=3;
```

```sql
DELETE FROM fifaDB WHERE id=1;
```

```sql
UPDATE fifaDB SET 
        country=country_B, 
        confederation=
        BBBBB,
        population_share=5.0, 
        tv_audience_share=5.0, 
        gdp_weighted_share=5.0,
        WHERE id=4;
```

```sql
SELECT * FROM fifaDB;
```

```sql
UPDATE fifaDB SET 
        country=country_A, 
        confederation=
        AAAAA,
        population_share=5.0, 
        tv_audience_share=5.0, 
        gdp_weighted_share=5.0,
        WHERE id=3;
```

```sql
DELETE FROM fifaDB WHERE id=1;
```

```sql
UPDATE fifaDB SET 
        country=country_B, 
        confederation=
        BBBBB,
        population_share=5.0, 
        tv_audience_share=5.0, 
        gdp_weighted_share=5.0,
        WHERE id=4;
```

```sql
SELECT * FROM fifaDB;
```

```sql
UPDATE fifaDB SET 
        country=country_A, 
        confederation=
        AAAAA,
        population_share=5.0, 
        tv_audience_share=5.0, 
        gdp_weighted_share=5.0,
        WHERE id=3;
```

```sql
DELETE FROM fifaDB WHERE id=1;
```

```sql
UPDATE fifaDB SET 
        country=country_B, 
        confederation=
        BBBBB,
        population_share=5.0, 
        tv_audience_share=5.0, 
        gdp_weighted_share=5.0,
        WHERE id=4;
```

```sql
SELECT * FROM fifaDB;
```

```sql
SELECT t1.server, t1.opponent, AVG(t1.seconds_before_next_point) as avg_seconds_before_next_point, COUNT(*) as total_matches_played FROM default.servetimesdb t1 JOIN default.eventtimesdb t2 ON t1.id = t2.id GROUP BY t1.server, t1.opponent ORDER BY total_matches_played DESC LIMIT 10
```

```response from databricks
[Row(server='Nick Kyrgios', opponent='Andy Murray', avg_seconds_before_next_point=14.157894736842104, total_matches_played=19), Row(server='Roger Federer', opponent='Damir Dzumhur', avg_seconds_before_next_point=16.25, total_matches_played=16), Row(server='Andy Murray', opponent='Joao Sousa', avg_seconds_before_next_point=23.7, total_matches_played=10), Row(server='Benoit Paire', opponent='Tomas Berdych', avg_seconds_before_next_point=14.333333333333334, total_matches_played=9), Row(server='Nicolas Almagro', opponent='Rafael Nadal', avg_seconds_before_next_point=21.625, total_matches_played=8), Row(server='Carlos Berlocq', opponent='Richard Gasquet', avg_seconds_before_next_point=28.875, total_matches_played=8), Row(server='Bernard Tomic', opponent='Thanasi Kokkinakis', avg_seconds_before_next_point=20.857142857142858, total_matches_played=7), Row(server='Borna Coric', opponent='Tommy Robredo', avg_seconds_before_next_point=26.714285714285715, total_matches_played=7), Row(server='Lukas Rosol', opponent='Teymuraz Gabashvili', avg_seconds_before_next_point=17.285714285714285, total_matches_played=7), Row(server='Rafael Nadal', opponent='Nicolas Almagro', avg_seconds_before_next_point=28.833333333333332, total_matches_played=6)]
```

```sql
SELECT t1.server, t1.opponent,
                AVG(t1.seconds_before_next_point) as avg_seconds_before_next_point,
                COUNT(*) as total_matches_played
            FROM default.servetimesdb t1
            JOIN default.eventtimesdb t2 ON t1.id = t2.id
            GROUP BY t1.server, t1.opponent
            ORDER BY total_matches_played DESC
            LIMIT 10
```

```response from databricks
[Row(server='Nick Kyrgios', opponent='Andy Murray', avg_seconds_before_next_point=14.157894736842104, total_matches_played=19), Row(server='Roger Federer', opponent='Damir Dzumhur', avg_seconds_before_next_point=16.25, total_matches_played=16), Row(server='Andy Murray', opponent='Joao Sousa', avg_seconds_before_next_point=23.7, total_matches_played=10), Row(server='Benoit Paire', opponent='Tomas Berdych', avg_seconds_before_next_point=14.333333333333334, total_matches_played=9), Row(server='Nicolas Almagro', opponent='Rafael Nadal', avg_seconds_before_next_point=21.625, total_matches_played=8), Row(server='Carlos Berlocq', opponent='Richard Gasquet', avg_seconds_before_next_point=28.875, total_matches_played=8), Row(server='Bernard Tomic', opponent='Thanasi Kokkinakis', avg_seconds_before_next_point=20.857142857142858, total_matches_played=7), Row(server='Borna Coric', opponent='Tommy Robredo', avg_seconds_before_next_point=26.714285714285715, total_matches_played=7), Row(server='Lukas Rosol', opponent='Teymuraz Gabashvili', avg_seconds_before_next_point=17.285714285714285, total_matches_played=7), Row(server='Rafael Nadal', opponent='Nicolas Almagro', avg_seconds_before_next_point=28.833333333333332, total_matches_played=6)]
```

```sql
SELECT t1.server, t1.opponent,
                AVG(t1.seconds_before_next_point) as avg_seconds_before_next_point,
                COUNT(*) as total_matches_played
            FROM default.servetimesdb t1
            JOIN default.eventtimesdb t2 ON t1.id = t2.id
            GROUP BY t1.server, t1.opponent
            ORDER BY total_matches_played DESC
            LIMIT 10
```

```response from databricks
[Row(server='Nick Kyrgios', opponent='Andy Murray', avg_seconds_before_next_point=14.157894736842104, total_matches_played=19), Row(server='Roger Federer', opponent='Damir Dzumhur', avg_seconds_before_next_point=16.25, total_matches_played=16), Row(server='Andy Murray', opponent='Joao Sousa', avg_seconds_before_next_point=23.7, total_matches_played=10), Row(server='Benoit Paire', opponent='Tomas Berdych', avg_seconds_before_next_point=14.333333333333334, total_matches_played=9), Row(server='Nicolas Almagro', opponent='Rafael Nadal', avg_seconds_before_next_point=21.625, total_matches_played=8), Row(server='Carlos Berlocq', opponent='Richard Gasquet', avg_seconds_before_next_point=28.875, total_matches_played=8), Row(server='Bernard Tomic', opponent='Thanasi Kokkinakis', avg_seconds_before_next_point=20.857142857142858, total_matches_played=7), Row(server='Borna Coric', opponent='Tommy Robredo', avg_seconds_before_next_point=26.714285714285715, total_matches_played=7), Row(server='Lukas Rosol', opponent='Teymuraz Gabashvili', avg_seconds_before_next_point=17.285714285714285, total_matches_played=7), Row(server='Rafael Nadal', opponent='Nicolas Almagro', avg_seconds_before_next_point=28.833333333333332, total_matches_played=6)]
```

