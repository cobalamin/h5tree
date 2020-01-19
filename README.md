# h5tree
Prints an HDF5 file like the GNU utility `tree`

```
usage: h5tree.py [-h] [-d max_depth] [-c max_children] [-a max_attr_length] [-i indent] file

Prints the structural tree of an HDF5 file.

positional arguments:
  file                The filename of the HDF5 file to print.

optional arguments:
  -h, --help          show this help message and exit
  -d max_depth        Maximum depth to print starting from the root.
  -c max_children     Maximum number of children to print at each node.
  -a max_attr_length  The maximum length of the attribute values to be printed.
  -i indent           The indentation level.
```

# Example call and output
```
$ ./h5tree.py test.h5 -c 5 -d 3 -i 2                                                                                                       
.
* dimensions = 2
* time_step = 1e-05
├ detector_hits
│ ├ 0 (7168, 8)
│ ├ 1 (4388, 8)
│ ├ 2 (2532, 8)
│ ├ 3 (2495, 8)
│ └ 4 (2228, 8)
└ particles
  ├ 0
  │ ├ final_position (4,)
  │ ├ initial_position (4,)
  │ └ trajectory (447, 5)
  ├ 1
  │ ├ final_position (4,)
  │ ├ initial_position (4,)
  │ └ trajectory (2, 5)
  ├ 10
  │ ├ final_position (4,)
  │ ├ initial_position (4,)
  │ └ trajectory (581, 5)
  ├ 100
  │ ├ final_position (4,)
  │ ├ initial_position (4,)
  │ └ trajectory (413, 5)
  ├ 1000
  │ ├ final_position (4,)
  │ ├ initial_position (4,)
  │ └ trajectory (143, 5)
  ⋮ (9995 more)
```
