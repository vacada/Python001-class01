"""
__author__:'vacada'
__description__:'请将以下的 SQL 语句翻译成 pandas 语句'
__mtime__:2020/7/19
"""

import pandas as pd
import numpy as np


# 1. SELECT * FROM data;
data

# 2. SELECT * FROM data LIMIT 10;
data.head(10)

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
data['id']

# 4. SELECT COUNT(id) FROM data;
data['id'].value_counts()

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
data[(data['id'] < 1000) & (data['age'] > 30)]

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
table1.groupby('id').agg({'order_id':pd.Series.nunique}

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
data = pd.merge(table1, table2, on='id')

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
pd.concat([table1, table2]).drop_duplicates()

# 9. DELETE FROM table1 WHERE id=10;
table1.loc[table1['id'] != 10]

# 10. ALTER TABLE table1 DROP COLUMN column_name;
table1.drop(['column_name'], inplace=True, axis=1)







