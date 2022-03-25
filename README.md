## Introduction

This repo will validate whether your backend API services (REST/GQL/GRPC) execute well (pass/fail/disabled).
It requires you to download the [csv report file](####CSV_REPORT_FILE) and identify the [query path services](####QUERY_LIST_FILE) from your team.

## How to Use

```bash
python main.py [--csv-report-file {CSV_REPORT_FILE}] [--query-list {QUERY_LIST_FILE}] [--only-show-problem]
```

You need to install several dependencies first. You can run the following code.

```bash
pip install -r requirements.txt
```

#### CSV_REPORT_FILE

By default, the **CSV_REPORT_FILE** is referred in the file `constants.py`.

To override the file in `constants.py`, you could use arguments in running the file.

You can use any of the hourly CSV file logs that you obtained from the following slack channels:

- test-report-api-production
- test-report-gql-production
- test-report-grpc-production

#### QUERY_LIST_FILE

By default, the **QUERY_LIST_FILE** is referred in the file `constants.py`.

To override the file in `constants.py`, you could use arguments in running the file.

You can easily create a new txt file, open your REST/GQL/GRPC test field lists on Google sheet and copy only the column value of _QueryName_ and _ServiceName_ to the file.

Copy it as is, so you would get the tab-seperated file right away.

Example file:

```txt
GetTickerWithNulluserID	mojito
GetTickerWithInvalidUserID	mojito
GetChannel	mojito
GetChannelWithInvalidUserID	mojito
GetRecommendationProduct	mojito
```

#### only-show-problem

Use this argument if you want to only see the result that is not pass (either fail or not found).
The default value is False (or displaying all result from the **QUERY_LIST_FILE**)
