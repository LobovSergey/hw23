from collections import Counter


def data_processing(command, value, data):
    if command == "filter":
        return filter(lambda string_data: value in string_data, data)
    elif command == "map":
        return map(lambda string_data: string_data.split(' ')[int(value) - 1], data)
    elif command == "unique":
        return
    elif command == "sort":
        if value == "desc":
            return map(lambda x: x, sorted(data, reverse=True))
        else:
            return map(lambda x: x, sorted(data, reverse=False))
    elif command == "limit":
        data_counter = Counter(data)
        return map(lambda string: string[0], data_counter.most_common(int(value)))





