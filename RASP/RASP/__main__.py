#! /usr/bin/env python
import argparse, sys
import RASP

fpaa = RASP.FPAA()
parser = argparse.ArgumentParser(description="CLI Interface to RASP family FPAAs", prog="python -m RASP")
commands = parser.add_subparsers(required=True, dest="command")

c_readmem = commands.add_parser("readmem", help="read from memory and store in provided file")
c_writemem = commands.add_parser("writemem", help="write file to memory at address")
c_run = commands.add_parser("run", help="Load the given program and put the FPAA in run mode")
c_program = commands.add_parser("program", help="Load the given program and put the FPAA in program mode")
c_casdp = commands.add_parser("casdp", help="run a experment file from CASDP tools")

for c_parser in [c_casdp, c_readmem, c_writemem, c_run, c_program]:
    c_parser.add_argument("file")

def hexint(input):
    return int(input, 16)

for c_parser in [c_readmem, c_writemem]:
    c_parser.add_argument("addr", type=hexint)
    c_parser.add_argument("--release", dest="release", action="store_true", help="Release the FPAA when done")
    c_parser.add_argument("--no-release", dest="release", action="store_false", help="Don't release the FPAA when done")

c_readmem.add_argument("length", type=hexint)

args = parser.parse_args(sys.argv[1:])

if args.command == "readmem":
    print("Reading memory from " + hex(args.addr) + " to " + hex(args.addr - args.length))
    fpaa.read_mem_file(args.file, args.addr, len=args.length, release=args.release)

elif args.command == "writemem":
    print("Writing " + args.file + " to " + hex(args.addr))
    fpaa.write_mem_file(args.file, args.addr, args.release)

elif args.command == "run":
    print("running file: " + str(args.file))
    fpaa.run_file(args.file)

elif args.command == "program":
    print("programming with file " + str(args.file))
    fpaa.program_file(args.file)

elif args.command == "casdp":
    print("starting experiment: " + args.file)
    fpaa.run_experiment(args.file)