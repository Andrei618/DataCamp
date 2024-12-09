### Cleaning Data in Python

#### Chapter 1: Data Type Constraints

##### Common Data Problems:
1. **Why Clean Data?**
   - Garbage In, Garbage Out: Errors in data propagate to analytics and models.
   - Consistent, accurate data is crucial for meaningful insights.

2. **Data Types:**
   - Examples:
     - Text: First name, address (Python type: `str`).
     - Integers: Subscribers, products sold (Python type: `int`).
     - Decimals: Exchange rates, temperature (Python type: `float`).
     - Binary: Yes/No, new customer (Python type: `bool`).
     - Dates: Order dates, birthdates (Python type: `datetime`).
     - Categories: Gender, marital status (Python type: `category`).

3. **Converting Strings to Numbers:**
   - Example Dataset:
     ```
     SalesOrderID    Revenue    Quantity
     43659           23153$    12
     43660           1457$     2
     ```
   - Code:
     ```python
     import pandas as pd
     sales = pd.read_csv('sales.csv')
     sales['Revenue'] = sales['Revenue'].str.strip('$').astype('int')
     assert sales['Revenue'].dtype == 'int'
     ```

4. **Assert Statements:**
   - Ensure conditions are met during cleaning:
     ```python
     assert 1 + 1 == 2  # Passes
     assert 1 + 1 == 3  # Fails
     ```

5. **Categorical Data:**
   - Converting numerical encodings to categories:
     ```python
     df['marriage_status'] = df['marriage_status'].astype('category')
     print(df.describe())
     ```

---

#### Chapter 2: Membership Constraints

##### Categorical Data Problems:
1. **Finite Set of Categories:**
   - Example: Marital status (unmarried, married).
   - Problem: Values like `"Z+"` in blood types.

2. **Identifying Inconsistencies:**
   ```python
   inconsistent_categories = set(data['blood_type']).difference(categories['blood_type'])
   inconsistent_rows = data['blood_type'].isin(inconsistent_categories)
   consistent_data = data[~inconsistent_rows]
   ```

3. **Correcting Categories:**
   - Use mappings to standardize text fields (e.g., `married` -> `Married`).
   ```python
   data['marriage_status'] = data['marriage_status'].str.capitalize()
   ```

4. **Collapsing Categories:**
   - Map multiple categories into fewer ones:
     ```python
     mapping = {'Microsoft': 'DesktopOS', 'Android': 'MobileOS'}
     devices['operating_system'] = devices['operating_system'].replace(mapping)
     ```

---

#### Chapter 3: Uniformity

##### Common Uniformity Issues:
1. **Unit Conversion:**
   - Example: Celsius to Fahrenheit.
     ```python
     data.loc[data['Temperature'] > 40, 'Temperature'] = (data['Temperature'] - 32) * (5/9)
     assert data['Temperature'].max() < 40
     ```

2. **Date Formats:**
   - Converting inconsistent formats:
     ```python
     data['date'] = pd.to_datetime(data['date'], infer_datetime_format=True, errors='coerce')
     ```

3. **Cross-Field Validation:**
   - Ensure consistency between related fields.
     ```python
     flights['sum_classes'] = flights[['economy', 'business', 'first']].sum(axis=1)
     assert flights['sum_classes'].equals(flights['total_passengers'])
     ```

---

#### Chapter 4: Comparing Strings

##### String Matching Techniques:
1. **Edit Distance:**
   - Measures similarity based on operations (insertion, deletion, substitution).
   - Algorithms:
     - Levenshtein
     - Damerau-Levenshtein
     - Hamming

2. **String Comparison Tools:**
   - Example:
     ```python
     from thefuzz import fuzz
     score = fuzz.WRatio('Reeding', 'Reading')
     print(score)
     ```

3. **Collapsing Categories Using Similarity:**
   - Identify similar strings to standardize data:
     ```python
     for state in categories['state']:
         matches = process.extract(state, survey['state'], limit=survey.shape[0])
         for match in matches:
             if match[1] >= 80:
                 survey.loc[survey['state'] == match[0], 'state'] = state
     ```

4. **Record Linkage:**
   - Match records across datasets:
     ```python
     import recordlinkage
     indexer = recordlinkage.Index()
     indexer.block('state')
     pairs = indexer.index(data1, data2)
     compare = recordlinkage.Compare()
     compare.exact('date_of_birth', 'date_of_birth')
     matches = compare.compute(pairs, data1, data2)
     ```

---

### Summary:
This document consolidates all details from the provided slides on cleaning data in Python, including techniques for handling data type constraints, membership constraints, uniformity issues, and string comparisons. With practical examples and code snippets, it serves as a comprehensive reference for preparing data for analysis.

