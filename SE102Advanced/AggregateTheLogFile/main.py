LOG_FILE_CONTENT = """*.amazon.co.uk    89
*.doubleclick.net    139
*.fbcdn.net    212
*.in-addr.arpa    384
*.l.google.com    317
1.client-channel.google.com    110
6.client-channel.google.com    45
a.root-servers.net    1059
apis.google.com    43
clients4.google.com    71
clients6.google.com    81
connect.facebook.net    68
edge-mqtt.facebook.com    56
graph.facebook.com    150
mail.google.com    128
mqtt-mini.facebook.com    47
ssl.google-analytics.com    398
star-mini.c10r.facebook.com    46
staticxx.facebook.com    48
www.facebook.com    178
www.google.com    162
www.google-analytics.com    127
www.googleapis.com    87
"""


def get_domain_and_logs(line):
    domain = ''
    logs = 0
    current_str = ''
    for i in range(len(line) - 1, 0, -1):
        if line[i] == ' ':
            logs = int(current_str)
            break
        else:
            current_str = line[i:]
    for i in range(len(line)):
        if line[i] == ' ':
            domain = current_str
            break
        else:
            current_str = line[:i + 1]
    return domain, logs


def get_extension(domain):
    extension = ''
    for i in range(len(domain) - 1, 0, -1):
        if domain[i] == '.':
            if i == len(domain) - 3:
                continue
            else:
                extension = domain[i:]
                break
    return extension


def format_domain(domain):
    name = ''
    extension = get_extension(domain)
    current_str = ''
    for i in range(len(domain) - len(extension) - 1, 0, -1):
        if domain[i] == '.':
            name = current_str
            break
        else:
            current_str = domain[i] + current_str
    return name + extension


def sort_registry(registry):
    sorted_registry = {}
    values = list(registry.values())
    values.sort(reverse=True)
    for value in values:
        for key, item in registry.items():
            if item == value:
                if key not in sorted_registry:
                    sorted_registry[key] = value
    return sorted_registry


def count_domains(log_file, min_hits=0):
    lines = []
    current_line = ''
    for char in log_file:
        if char == '\n':
            lines.append(current_line)
            current_line = ''
        else:
            current_line += char
    registry = {}
    for line in lines:
        domain, logs = get_domain_and_logs(line)
        domain = format_domain(domain)
        if domain in registry:
            registry[domain] += logs
        else:
            registry[domain] = logs
    registry = sort_registry(registry)
    result = ''
    for key, value in registry.items():
        if value > min_hits:
            result += f"{key} ({value})\n"
    return result


def main():
    print(count_domains(LOG_FILE_CONTENT, 500))


if __name__ == "__main__":
    main()
