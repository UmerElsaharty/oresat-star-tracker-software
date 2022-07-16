'''Star Tracker App'''

from os.path import dirname, abspath
from enum import IntEnum
from argparse import ArgumentParser

from olaf import app_args_parser, parse_app_args, App

from .star_tracker_resource import StarTrackerResource


def main():
    # add the parent ArgumentParser for standard OreSat app args
    parser = ArgumentParser(prog='oresat-star-tracker', parents=[app_args_parser])
    args = parser.parse_args()
    parse_app_args(args)  # parse the standard app args

    eds_file = dirname(abspath(__file__)) + '/data/star_tracker.dcf'

    app = App(eds_file, args.bus, args.node_id, args.mock_hw)

    app.add_resource(StarTrackerResource)

    app.run()


if __name__ == '__main__':
    main()
