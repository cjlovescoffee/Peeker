# Peeker
A class to iterate over a sequence/iterable with the option to look behind/ahead at size elements.

## Usage

```python
from peeker import Peeker


sequence = range(1000, 1050, 2)

for element in Peeker(sequence, 2):
    if element.is_first:
        print("Starting Peeker!")

    print("[{}] {}: chunk={}".format(element.index, element.value, element.chunk))
    # print(element.previous)  # prints the previous elements in the sequence
    # print(element.future)  # prints the future elements in the sequence

    if element.is_last:
        print("Peeking complete!")

```

Outputs:

```
Starting Peeker!
[1] 1000: chunk=[None, None, 1000, 1002, 1004]
[2] 1002: chunk=[None, 1000, 1002, 1004, 1006]
[3] 1004: chunk=[1000, 1002, 1004, 1006, 1008]
[4] 1006: chunk=[1002, 1004, 1006, 1008, 1010]
[5] 1008: chunk=[1004, 1006, 1008, 1010, 1012]
[6] 1010: chunk=[1006, 1008, 1010, 1012, 1014]
[7] 1012: chunk=[1008, 1010, 1012, 1014, 1016]
[8] 1014: chunk=[1010, 1012, 1014, 1016, 1018]
[9] 1016: chunk=[1012, 1014, 1016, 1018, 1020]
[10] 1018: chunk=[1014, 1016, 1018, 1020, 1022]
[11] 1020: chunk=[1016, 1018, 1020, 1022, 1024]
[12] 1022: chunk=[1018, 1020, 1022, 1024, 1026]
[13] 1024: chunk=[1020, 1022, 1024, 1026, 1028]
[14] 1026: chunk=[1022, 1024, 1026, 1028, 1030]
[15] 1028: chunk=[1024, 1026, 1028, 1030, 1032]
[16] 1030: chunk=[1026, 1028, 1030, 1032, 1034]
[17] 1032: chunk=[1028, 1030, 1032, 1034, 1036]
[18] 1034: chunk=[1030, 1032, 1034, 1036, 1038]
[19] 1036: chunk=[1032, 1034, 1036, 1038, 1040]
[20] 1038: chunk=[1034, 1036, 1038, 1040, 1042]
[21] 1040: chunk=[1036, 1038, 1040, 1042, 1044]
[22] 1042: chunk=[1038, 1040, 1042, 1044, 1046]
[23] 1044: chunk=[1040, 1042, 1044, 1046, 1048]
[24] 1046: chunk=[1042, 1044, 1046, 1048, None]
[25] 1048: chunk=[1044, 1046, 1048, None, None]
Peeking complete!
```
