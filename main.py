import pandas as pd
from colors import cprint
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--csv-report-file', type=str, dest='csv_report_file',
                    default='TestExecutionReport.csv')
parser.add_argument('--query-list', type=str, dest='query_list',
                    default='list_automate.txt')
args = parser.parse_args()


df = pd.read_csv(args.csv_report_file)

file = open(args.query_list, "r")
lines = file.readlines()


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


for line in lines:
    queryName, category = line.strip().split("\t")
    result = getDataResult(queryName, category)
    cprint("{} - {}: {}".format(category, queryName, result),
           getColorPrint(result))
