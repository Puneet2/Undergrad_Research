import os

class FPAA:
    def __init__(self):
        pass

    def run_file(self, file):
        """Places the FPAA in run mode and uploads a program from the specified file."""
        os.system("sudo tclsh /home/ubuntu/rasp30/prog_assembly/libs/tcl/run_new.tcl -speed 115200 " + file)

    def program_file(self, file):
        """Places the FPAA in program mode and uploads a program from the specified file."""
        os.system("sudo tclsh /home/ubuntu/rasp30/prog_assembly/libs/tcl/program.tcl -speed 115200 " + file) 

    def write_mem_file(self, file, addr, release=False):
        """Writes the contents of a file to memory at the specified address. This does not release the FPAA unless release=True is specified."""
        rel = ("_NoRelease", "")[release]
        os.system("sudo tclsh /home/ubuntu/rasp30/prog_assembly/libs/tcl/write_mem2" + rel + ".tcl -start_address " + hex(addr)[2:] + " -input_file_name " + file)

    def read_mem_file(self, file, addr, to=None, len=None, release=False):
        """Reads the contents of memory to a file between the specified addresses or to the specified length. This does not release the FPAA unless release=True is specified."""
        if len == None:
            if to == None:
                raise ValueError("You must specify a length or an end address")
            len = to - addr
        rel = ("_NoRelease", "")[release]
        os.system("sudo tclsh /home/ubuntu/rasp30/prog_assembly/libs/tcl/read_mem2" + rel + ".tcl -start_address " + hex(addr)[2:] + " -length " + hex(len)[2:] +" -output_file_name " + file)   

    def run_experiment(self, file):
        """Runs a specified casdp experiment package and stores the results in ??"""
        pass