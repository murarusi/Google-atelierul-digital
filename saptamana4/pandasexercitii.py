import pandas as pd

dataset = {
    "masini": ["bmw", "dacia", "ford"],
    "culoare": ["rosu", "negeru", "gri"]
}


var = pd.DataFrame(dataset)

print(var)
