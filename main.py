import pandas as pd
import numpy as np


names = np.array(["gitanshu","Uttu","popi"])
ages = np.array(["18","20","90"])


dict = {"name" :names,
        "age": ages}


df = pd.DataFrame(dict)
print (df)