## How to Use

```
python main.py --csv-report-file [CSV_REPORT_FILE] --query-list [QUERY_LIST_FILE]
```

#### CSV_REPORT_FILE

The default `CSV_REPORT_FILE` is TestExecutionReport.csv.

You can use any of the hourly CSV file logs that you obtained from the following slack channels:

- test-report-api-production
- test-report-gql-production
- test-report-grpc-production

#### QUERY_LIST_FILE

The default `QUERY_LIST_FILE` is list_automate.txt.
You can easily create a new txt file, open your REST/GQL/GRPC test field lists on Google sheet and copy only the data of `QueryName` and `ServiceName` to the file.

Example file:

```
GetTickerWithNulluserID	mojito
GetTickerWithInvalidUserID	mojito
GetChannel	mojito
GetChannelWithInvalidUserID	mojito
GetRecommendationProduct	mojito
```
