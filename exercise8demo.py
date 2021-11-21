# author: Tiffany Timbers
# date: 2020-01-15

"""This script prints out docopt args.
Usage: demo.py <arg1> --arg2=<arg2> [<arg4>] [--arg3=<arg3>]

Options:
<arg1>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[<arg4>]           Takes any value (this is an optional positional argument)
[--arg3=<arg3>]   Takes any value (this is an optional option)
""" 

from docopt import docopt
opt = docopt(__doc__)

def main(opt):
  print(opt)
  print(type(opt))
  print(opt["<arg4>"])


if __name__ == "__main__":
  main(opt)
