#!/usr/bin/python3
"""
Color of a range of universities
"""

import sys


def rgb2hex(r, g, b):
    return "#%02X%02X%02X" % (r, g, b)


def main(argc, argv):
    if argc != 2:
        print("Usage: %s <uni>" % argv[0], file=sys.stderr)
        return 1

    uni = argv[1]

    uni_aliases_map = {
        'th': 'Tsinghua',
        'pk': 'Peking',
        'xm': 'Xmu',
        'rc': 'Ruc',
        'hv': 'Harvard',
        'ya': 'Yale',
        'ox': 'Oxford',
        'cb': 'Cambridge',
        'zb': 'ZhedaBlue',
        'zr': 'ZhedaRed',
        'ag': 'ArmyGreen',
        'bk': 'Black',
        'we': 'White'
    }

    if len(uni) == 2:
        uni_key = uni_aliases_map.get(uni, None)
        if uni_key is None:
            uni_key = uni
    else:
        uni_key = uni

    # http://www.360doc.com/content/18/1226/12/20431251_804573810.shtml
    # XMU: https://baijiahao.baidu.com/s?id=1686310048127145564
    colors_map = {
        "Tsinghua"  : [102,   8, 116],
        "Peking"    : [139,   0,  18],
        "Xmu"       : [  0,  60, 136],
        "Ruc"       : [174,  11,  42],
        "Harvard"   : [165,  28,  48],
        "Yale"      : [  0,  53, 107],
        "Oxford"    : [  0,  33,  71],
        "Cambridge" : [163, 193, 173],
        "ZhedaBlue" : [  0,  63, 136],
        "ZhedaRed"  : [176,  31,  36],
        "ArmyGreen" : [ 51,  76,  43],
        "Black"     : [  0,   0,   0],
        "White"     : [255, 255, 255]
    }

    rgb = colors_map.get(uni_key, None)
    if rgb is None:
        print(f"Oops, key `{uni}` not found", file=sys.stderr)
        print(f"Supported keys:\n{' ' * 4}{','.join(colors_map.keys())}", file=sys.stderr)
        return 1

    print(f"{uni_key}: {rgb2hex(rgb[0], rgb[1], rgb[2])}")
    return 0


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv))
