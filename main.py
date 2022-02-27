#!/usr/bin/env python3
import holder
import argparse
def demo():
    val = holder.Placeholder("demo/README.md").substitute("demo/content.txt")
    with open("demo/rel.md","w") as fd:
        fd.write(val)
    print(val)
def getArgparser()->argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('source')
    parser.add_argument('content')
    parser.add_argument('-o','--output',action='store',help="Specify the output file(output to console as default)")
    parser.add_argument('-i',action='store_true',help="In-place modification")
    return parser

if __name__=="__main__":
    parser = getArgparser()
    arg = parser.parse_args()
    val = holder.Placeholder(arg.source).substitute(arg.content)
    out = False
    if arg.i:
        out = True
        holder.save(val,arg.source)
    if arg.output:
        out = True
        holder.save(val,arg.output)
    if not out:
        print(val)