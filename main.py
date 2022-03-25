import pandas as pd
from colors import cprint
import argparse
import constants

parser = argparse.ArgumentParser()
parser.add_argument('--csv-report-file', type=str, dest='csv_report_file',
                    default=constants.DEFAULT_CSV_REPORT_FILE)
parser.add_argument('--query-list', type=str, dest='query_list',
                    default=constants.DEFAULT_QUERY_LIST_FILE)
parser.add_argument('--only-show-problem',
                    action=argparse.BooleanOptionalAction,
                    dest='only_show_problem', default=False)
args = parser.parse_args()


df = pd.read_csv(args.csv_report_file)


def getDataResult(queryName, category):
    res = df[(df['Category'] == category) & (df['QueryName'] == queryName)]
    if len(res) == 1:
        return res['Result'].item()
    if len(res) == 0:
        return 'Not found'
    return ",".join(res['Result'].unique())


def getColorPrint(result):
    if result == 'Pass':
        return 'success'
    elif result == 'Fail':
        return 'error'
    return 'warning'


file = open(args.query_list, "r")
lines = file.readlines()

for line in lines:
    queryName, category = line.strip().split("\t")
    result = getDataResult(queryName, category)
    if args.only_show_problem:
        if result != 'Pass':
            cprint("{} - {}: {}".format(category, queryName, result),
                   getColorPrint(result))
    else:
        cprint("{} - {}: {}".format(category, queryName, result),
               getColorPrint(result))
