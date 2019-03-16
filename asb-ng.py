#!/usr/bin/env python

import tools.log as lg
import cli


def main():

    mylog = lg.asblog()
    mylog.config('asb-ng.log')

    mycli = cli.Cli()
    mycli.cmdloop()


if __name__ == '__main__':
    main()
