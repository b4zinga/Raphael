# author: myc

import argparse


def cmdline_parser():
    parser = argparse.ArgumentParser(formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=30))

    parser.add_argument("-u", "--host", dest="host", help="target host or file")
    parser.add_argument("-k", "--plugin", dest="plugin", help="filter plugins by keyword")
    parser.add_argument("-l", "--list", action="store_true", help="list all exist plugins")

    parser.add_argument("-p", "--port", dest="port", help="target port")

    parser.add_argument("-t", "--thread", dest="thread", type=int, default=5, help="number of thread, default 5")
    
    parser.add_argument("-e", "--error", action="store_true", help="show error message of plugins")
    parser.add_argument("-o", "--output", dest="output", default="output", help="report dir")
    parser.add_argument("-f", "--format", dest="format", default="html", help="report format, html/json/csv")

    args = parser.parse_args()

    return args
