# -*- coding: utf-8 -*-

import json
import csv
from argparse import ArgumentParser


def main():
    parser = ArgumentParser(
        description='Export a Json log into a csv'
    )
    parser.add_argument(
        'jsonlog', help="The jsonlog file"
    )
    parser.add_argument(
        '-f', '--filter', help="Filter: <attribute>=<value>"
    )
    parser.add_argument(
        'columns', help="The attributes to export"
    )
    parser.add_argument(
        'csvfile', help="The destination scv file"
    )

    options = parser.parse_args()
    if options.filter is not None:
        use_filter = options.filter.split("=")
        use_filter[0] = '{%s}' % use_filter[0]

    with open(options.jsonlog) as jsonlog:
        with open(options.csvfile, 'wb') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(options.columns.split(','))
            for line in jsonlog:
                log = json.loads(line)
                if 'bbox' in log and 'bbox_center' not in log and \
                        isinstance(log['bbox'], list) and len(log['bbox']) == 4:
                    bbox = log['bbox']
                    log['bbox_center'] = [
                        (bbox[0] + bbox[2]) / 2,
                        (bbox[1] + bbox[3]) / 2,
                    ]

                row = []

                try:
                    if options.filter is not None and \
                            use_filter[0].format(**log) != use_filter[1]:
                        continue
                except AttributeError:
                    continue
                except KeyError:
                    continue

                for column in options.columns.split(','):
                    try:
                        row.append(('{%s}' % column).format(**log))
                    except AttributeError:
                        row.append(None)
                    except KeyError:
                        row.append(None)

                csvwriter.writerow(row)
