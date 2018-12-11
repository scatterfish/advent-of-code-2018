Decided to test the performance of each of the solutions using `time`. For Crystal and Rust, built binaries with the `--release` flag.

Testing results on my machine (i7-8750H, 16GB RAM):
* Python
  ```
  real    0m0.985s
  user    0m0.978s
  sys     0m0.007s
  ```
* Crystal
  ```
  real    0m0.077s
  user    0m0.104s
  sys     0m0.043s
  ```
* Rust
  ```
  real    0m0.013s
  user    0m0.010s
  sys     0m0.004s
  ```
