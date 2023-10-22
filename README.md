# 如何使用腳本檔
## 如果你是使用 Linux
進入該資料夾，打開 Terminal，接著輸入 `bash [sh]`

## 如果你是使用 Windows
進入該資料夾，打開 git bash，接著輸入 `sh [sh]`



| 名稱     | 描述                                                     | 數值                                                                                       |   |   |
|----------|----------------------------------------------------------|--------------------------------------------------------------------------------------------|---|---|
| action   | Specify how an argument should be handled                | 'store', 'store_const', 'store_true', 'append', 'append_const', 'count', 'help', 'version' |   |   |
| choices  | Limit values to a specific set of choices                | ['foo', 'bar'], range(1, 10), or Container instance                                        |   |   |
| const    | Store a constant value                                   |                                                                                            |   |   |
| default  | Default value used when an argument is not provided      | Defaults to None                                                                           |   |   |
| dest     | Specify the attribute name used in the result namespace  |                                                                                            |   |   |
| help     | Help message for an argument                             |                                                                                            |   |   |
| metavar  | Alternate display name for the argument as shown in help |                                                                                            |   |   |
| nargs    | Number of times the argument can be used                 | int, '?', '*', or '+'                                                                      |   |   |
| required | Indicate whether an argument is required or optional     | True 或 False                                                                              |   |   |
| type     | Automatically convert an argument to the given type      | int、float、argparse.FileType('w') 或可呼叫的函式                                          |   |   |


## 參考的網站:
https://realpython.com/command-line-interfaces-python-argparse/