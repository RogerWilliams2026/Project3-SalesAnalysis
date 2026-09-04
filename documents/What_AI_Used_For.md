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

**Scenario Three:**

Been developing an ETL library and wanted to use it in this project, however have no idea how to
do it, so asked chatGPT for a solution with this question:

Am using jupyter notebook for a project and the notebook is in a subfolder. However I wish to
use some libraries in a another folder in the same project how can I import them?

I attempted using:

import modGlobal
import modETL_Library as modETL

It replied with a lot of code examples but the most important part was this:

_import sys_
_from pathlib import Path_

_project_root = Path.cwd().parent_
_if str(project_root / "assets" / "python_files") not in sys.path:_
_sys.path.insert(0, str(project_root / "assets" / "python_files"))_

_import modGlobal_  
_import modETL_Library as modETL_

This works so used it everywhere!

**Scenario Four:**

Had strange issue with ploty express where the x-axis was not in the correct order, even though the DataFrame was sorted correctly, the last 3 itesm were in the wrong order!

Asked chatGPT this question:

pandas created a plot showing one year values against anothers, however even though the x axis values are sorted in the dataframe the plot show 3 in the wrong order e.g: Tiel, Ledrada, Olten, Riva, why is this?

It replied with:

_The likely issue is Plotly, not pandas._

_Your DataFrame is sorted by Year, but your plot's x-axis is ProductFamily, and you never explicitly tell \_Plotly what order the product families should appear in._

_Plotly determines the category order from the data it receives. With two years and grouped data, that can_ _produce an order that isn't the same as the order you were expecting._
_The fix_

_Explicitly specify the x-axis category order._

_If you want the product families alphabetically:_

_fig.update_xaxes(_
_ type="category",_
_ categoryorder="category ascending"_
_)_

Works!
