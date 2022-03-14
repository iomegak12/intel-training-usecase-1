import re
import csv

log_entry = '27.59.104.166 - - [04/Oct/2019:21:15:54 +0000] "GET /users/login HTTP/1.1" 200 41716 "-" "okhttp/3.12.1"'

matches = [0 for i in range(1, 8)]

print(matches)

matches[0] = '^(?P<IP>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})'
matches[1] = '\s.*\[(?P<Timestamp>.*)]'
matches[2] = '\s"(?P<Verb>[A-Z]+)'
matches[3] = '\s(?P<Path>[\w\/]+)'
matches[4] = '\s(?P<Protocol>[\w\/.]+)'
matches[5] = '"\s(?P<StatusCode>\d+)'
matches[6] = '\s(?P<NoOfBytes>\d+).*'

pattern_clear = "".join(matches)

# pattern = r'^(?P<IP>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s.*\[(?P<Timestamp>.*)]\s"(?P<Verb>[A-Z]+)\s(?P<Path>[\w\/]+)\s(?P<Protocol>[\w\/.]+)"\s(?P<StatusCode>\d+)\s(?P<NoOfBytes>\d+).*'

compiled_pattern = re.compile(pattern_clear)

match_result = compiled_pattern.match(log_entry)

if match_result:
    print(match_result.groupdict())

    dict = match_result.groupdict()
    dict["StatusCode"] = 404

    print(dict)

    csv_data = f'{dict["IP"]},{dict["Timestamp"]},{dict["Verb"]},{dict["Path"]},{dict["Protocol"]},{dict["StatusCode"]},{dict["NoOfBytes"]}'

    print(csv_data)

    file_name = "./output.csv"

    with open(file_name, mode='w') as file:
        writer = csv.DictWriter(file, fieldnames=dict.keys())
        writer.writeheader()
        writer.writerow(dict)

    print('file writing completed!')
