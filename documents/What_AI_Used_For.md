# What Generative AI Was Used For

Throughout this project from time to time Generative AI was used to help in certain situations, where no amount of critical
thinking, pondering or the consumption of thinking biscuits could provide an answer.

This document highlights the areas where Generative AI was used and what it was used for, by providing a "before" and "after" showing what the issue was and what Generative AI proposed, or the original code and the suggested replacement.

Most common use is with CoPilot in VS Code, particularly for changing code when I rename variables, not too reliant on
the code suggestions as they don't always work and sometimes it will happily suggest properties that do not exist!
If it suggests something that is accurate in the current code flow will select it such as creating new columns in a DataFrame  
and it suggests the next line of code. Usually that works fine.

**Scenario One:**

Pandas would not read the csv file as it was not in UTF-8 format!

Gave chatGPT this instruction:

Pandas error reading fle encoding not utf-8 how can i detect and use correct encoding?

chatGPT responded with:

_pip install charset-normalizer_
_from charset_normalizer import from_path_
_result = from_path("your filename").best()_
_df = pd.read_csv("your filename", encoding=objEncoding.encoding)_

Adapted code and added to funcReadFileReturnDataFrame in my ETl library

**Scenario Two:**

Was stumped on how to run a Kruskal-Wallis test on the InvoiceAmt column by TerritoryCodes column

Gave chatGPT this instruction:

How do I run a Kruskal-Wallis test on the InvoiceAmt column by TerritoryCodes column in a pandas DataFrame?

chatGPT responded with:

_groups = [_
_ group["InvoiceAmt"].dropna()_
_ for _, group in dfSales*DataSet_Work.groupby("TerritoryCodes")*
_]_

_fltStat, fltPValue = kruskal(\*groups)_

_print(f"Statistic: {fltStat:.3f}")_
_print(f"p-value: {fltPValue:.5f}")_

Does work so copied and amended as necessary
