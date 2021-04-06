import json

import numpy as np

ORDERED_KEYS = [
    'alc',
    'malic',
    'ash',
    'alcash',
    'mag',
    'tphen',
    'flav',
    'nflav',
    'poran',
    'color',
    'hue',
    'dil',
    'proline'
]

def json_to_row(data: bytes) -> np.ndarray:
    """Convert json data to valid row

    1. alc: Alcohol
 	2. malic: Malic acid
 	3. ash: Ash
	4. alcash: Alcalinity of ash  
 	5. mag: Magnesium
	6. tphen: Total phenols
 	7. flav: Flavanoids
 	8. nflav: Nonflavanoid phenols
 	9. poran: Proanthocyanins
	10. color: Color intensity
 	11. hue: Hue
 	12. dil: OD280/OD315 of diluted wines
 	13. proline: Proline            
    """
    data = json.loads(data)
    row = np.empty((1, len(ORDERED_KEYS)), dtype=float)
    for idx, key in enumerate(ORDERED_KEYS):
        row[0, idx] = data.get(key)
    return row
