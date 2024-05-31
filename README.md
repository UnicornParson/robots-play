# robots-play
logs parsing utils

## Modules:
### Common
common funtions
* `get_num_lines(file_path) -> int` returns count of file lines
* `first_not_null(l: list)` return first not 0 element (**comparation with 0. functiom created for numbers**)
* `not_null(l: list) -> list` remove all 0 from list
* `get_diff(l: list, r: list)`returns diff of two lists
* `normalize(l:list)->list:` normalize list of numbers
* `chunks(L, n)` split list to n parts
* `load_markers(fname: str, marker: str, extractor) -> list `loads and parses marked lines from file. extractor is a converter from string after marker to something that should be returned