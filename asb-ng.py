#!/usr/bin/env python

import logging
import cli

def main():
    logging.basicConfig(filename='asb-ng.log', level=logging.INFO, \
                        format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')
    logging.getLogger('MAIN')
    logging.info("Starting main process")

    cli.Cli().cmdloop()


if __name__ == '__main__':
    main()