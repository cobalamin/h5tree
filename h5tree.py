#!/usr/bin/env python3

import h5py

def print_tree(t, max_depth=None, max_children=None, max_attr_length=None, indent=4):
    assert indent >= 1
    s_linedown = '│' + (indent-1) * ' '
    s_empty = indent * ' '
    s_child = '├' + (indent-2) * '─' + ' '
    s_last_child = '└' + s_child[1:]
    
    print('.')
    prev_line = None
    def _print_tree(tree, depth=0):
        nonlocal prev_line
        if not hasattr(tree, 'keys') or (max_depth is not None and depth >= max_depth):
            return
        
        # Print attributes
        attrs = list(tree.attrs) if hasattr(tree, 'attrs') else []
        for idx, attr in enumerate(attrs):
            line = ''.join([
                s_linedown
                if prev_line and prev_line[j*indent] == '|' else
                s_empty
                for j in range(depth)
            ])
            val = str(tree.attrs[attr])
            if max_attr_length is not None and len(val) > max_attr_length:
                val = val[:max_attr_length] + ' […]'

            line += '* '
            line += f'{attr} = {val}'
            print(line)

        # Print children
        keys = list(tree.keys())
        n_k = len(keys)
        for idx, key in enumerate(keys):
            child = tree[key]
            is_first = idx == 0
            is_last = idx == n_k-1
            
            line = ''.join([
                s_linedown if prev_line and prev_line[j*indent] in ('│', '├') else
                s_empty
                for j in range(depth)
            ])
            if max_children is not None and idx >= max_children:
                # 
                print(f'{line}⋮ ({n_k - max_children} more)')
                break
            
            if is_last:
                line += s_last_child
            else:
                line += s_child          
            line += key
            
            if isinstance(child, h5py.Dataset):
                line += f' {child.shape}'
            
            print(line)
            prev_line = line
            if isinstance(child, h5py.Group):
                _print_tree(child, depth=depth+1)
    _print_tree(t)


def print_tree_from_file(filename, *args, **kwargs):
    with h5py.File(filename, 'r') as h5f:
        print_tree(h5f, *args, **kwargs)



if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Prints the structural tree of an HDF5 file.")
    parser.add_argument('file', type=str, help='The filename of the HDF5 file to print.')
    parser.add_argument('-d', metavar='max_depth',
                        type=int, default=None,
                        help='Maximum depth to print starting from the root.')
    parser.add_argument('-c', metavar='max_children',
                        type=int, default=None,
                        help='Maximum number of children to print at each node.')
    parser.add_argument('-a', metavar='max_attr_length',
                        type=int, default=None,
                        help='The maximum length of the attribute values to be printed.')
    parser.add_argument('-i', metavar='indent',
                        type=int, default=4,
                        help='The indentation level.')

    args = parser.parse_args()
    print_tree_from_file(
        args.file,
        max_depth=args.d, max_children=args.c,
        max_attr_length=args.a, indent=args.i
    )
