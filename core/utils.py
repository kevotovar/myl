import collections


def get_duplicates_from_list(list_to_be_checked):
    print(list_to_be_checked)
    return [
        item for item, count in collections.Counter(list_to_be_checked) if count > 1
    ]


def count_duplicates(list_to_be_counted):
    return len(list_to_be_counted) - len(set(list_to_be_counted))
