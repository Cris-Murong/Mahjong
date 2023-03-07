# Mahjong Check Win

### Prerequisite

Python - 3.10 +


### Functionality

This script can check for three kinds of winning hands: 
- Mian Zi hand
- 7 double hand
- 13 head hand

The output will be whether `Win` or `Not win`.

### Executing
```
> python3 check_win.py
```

After running the python file, input the tiles in the hand. 


```
Tile Representation:
"1m", "2m", "3m", "4m", "5m", "6m", "7m", "8m", "9m",
"1s", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s",
"1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p",
"1z", "2z", "3z", "4z", "5z", "6z", "7z" (dong na xi bei zhong fa bai)
```

Spacing each tile by a space, for example:
```
Input your hands >>1m 1m 1m 2m 3m 2m 3m 4m 3m 4m 5m 5p 6p 7p
```

Output:
```
Win: mian zi hand
```

