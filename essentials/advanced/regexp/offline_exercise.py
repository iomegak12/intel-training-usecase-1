import re

webserver_log_entry = '[Fri Sep 09 10:42:29.902022 2011] [core:error] [pid 35708:tid 4328636416] [client 72.15.99.187] File does not exist: /usr/local/apache2/htdocs/favicon.ico'

pattern = r'^\[(?P<timestamp>[\w\s.:]+)]\s\[(?P<logtype>[\w:]+)]\s\[(?P<details>[\w:\s]+)]\s\[(?P<ip>[\w\s.]+)]\s(?P<message>[\w\s]+):\s*(?P<path>[\w\/]+)'

compiled_pattern = re.compile(pattern)

match_result = compiled_pattern.match(webserver_log_entry)


if match_result:
    print(match_result.groupdict())
    