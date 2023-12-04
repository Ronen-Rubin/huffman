# import numpy as np
# import sys
# print(sys.argv[1])
# @TotalOrdering. python totalordering decorator
# could put decorator on class, clalled @dataclass
from functools import reduce
from node import Node


# with open(sys.argv[1]) as stream:
# with open("test_text.txt") as stream:


# txt file -> symbol:enc_symbol dictionary
def huffman(txt):
    txt_hist = {}
    for i in txt:
        if i in txt_hist:
            txt_hist[i] += 1
        else:
            txt_hist[i] = 1
    # txt_hist = sorted(txt_hist)
    # print(txt_hist.items())
    symbols = sorted(txt_hist.items(), key=lambda x: x[1])
    nodes = [Node(x[0], x[1]) for x in symbols]
    # sorted_freq =  dict(symbols)

    for i in range(len(nodes) - 1):
        left = nodes.pop(0)  # unshift? pop from begining
        right = nodes.pop(0)
        nodes.insert(
            0,
            Node(
                left.src_symbol + right.src_symbol, left.freq + right.freq, left, right
            ),
        )
        nodes.sort()  # in place

    root = nodes.pop()
    # print(root.dfs_encode())
    return {leaf.src_symbol: leaf.enc_symbol for leaf in root.dfs_encode()}
    # print(''.join([encoder[char] for char in list(txt)]))

    # print(Node.get_count())


# recieves symbol:enc_symbol dictionary + text file -> encoded file
def encode(encoder, txt):
    return "".join([encoder[char] for char in list(txt)])


def fold_encoded(acc, x, decoder):
    concatted = acc["buffer"] + x

    if concatted in decoder:
        return {"buffer": "", "output": acc["output"] + decoder[concatted]}

    return {"buffer": concatted, "output": acc["output"]}


# recieves encoder + encoded file -> text string
def decode(encoder, compressed):
    decoder = {v: k for k, v in encoder.items()}
    # compressed_lst = list(compressed)
    # reduce(function, list, initial)
    folded = reduce(
        lambda acc, x: fold_encoded(acc, x, decoder),
        list(compressed),
        {"buffer": "", "output": ""},
    )

    return folded["output"]

    # txt_out = ''
    # iter = ''
    # while compressed_lst: #better to do while len(compressed_lst) > 0 #because what is a T/F list?
    #     if compressed_lst[0] in decoder:#if it is a key, add char to text and remove first element of compressed_lst
    #         txt_out += decoder[compressed_lst[0]]
    #         del compressed_lst[0]
    #     else: #combine the first two elements of compressed_lst
    #         compressed_lst[0] = compressed_lst[0] + compressed_lst[1]
    #         del compressed_lst[1]
    # return txt_out


# if I run this code it will run this, but if I import anything from the module it wont.
if __name__ == "__main__":
    with open("test_text.txt") as stream:
        txt = stream.read()
    encoder = huffman(txt)
    # print(encoder)
    compressed = encode(encoder, txt)
    # print(compressed)
    # print(len(compressed)/(8*len(txt)))
    decoded = decode(encoder, compressed)
    # print(decoded == txt)
    # print(decode(encoder,compressed))
