There are 3 different versions for Day 5's solution in Python.
* `main_list_deletion.py` uses a list, and deletes items from it.
* `main_list_concat.py` uses a list, and splits + concats it.
* `main_string_concat.py` uses a string, and splits + concats it.

Additionally, the list versions use list comprehension for removal of all instances of an item, while the string version uses `string.replace()`.

Testing results on my machine (i7-8750H, 16GB RAM):
* `time ./main_list_deletion.py`
  ```
  real    0m6.127s
  user    0m6.121s
  sys     0m0.003s
  ```
* `time ./main_list_concat.py`
  ```
  real    0m2.072s
  user    0m2.050s
  sys     0m0.020s
  ```
* `time ./main_string_concat.py`
  ```
  real    0m0.145s
  user    0m0.138s
  sys     0m0.007s
  ```
