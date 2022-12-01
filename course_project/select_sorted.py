import csv
from itertools import islice

csv_file = open('../all_stocks_5yr.csv')
reader = csv.DictReader(csv_file)


def select_sorted(**kwargs):
    cache = []
    x = kwargs['sort_columns']
    if 'sort_columns' in list(kwargs.keys()) and kwargs['order'] == 'desc':
        sorted_list = sorted(reader, key=lambda row: row[x[0]], reverse=False)
    if 'sort_columns' in list(kwargs.keys()) and kwargs['order'] == 'asc':
        sorted_list = sorted(reader, key=lambda row: row[x[0]], reverse=True)
    if 'limit' in list(kwargs.keys()):
        limited_sorted_list = list(islice(sorted_list, 0, kwargs['limit']))
    if 'filename' in list(kwargs.keys()):
        f = open(f'../{kwargs["filename"]}', 'w')
        if limited_sorted_list in cache:
            return limited_sorted_list
        else:
            cache.append(limited_sorted_list)
            f.write(str(limited_sorted_list))
            f.close()
            return limited_sorted_list
    return sorted_list


def get_by_date(**kwargs):
    srt_lst = select_sorted(sort_columns=['high'], order='asc')
    for d in srt_lst:
        if kwargs['date'] == d['date'] and kwargs['name'] == d['Name']:
            f = open(f'../{kwargs["filename"]}', 'w')
            f.write(str(d))
            f.close()
            return d


data = select_sorted(sort_columns=['high'], order='asc', limit=10, filename='dump1.csv')
for i in data:
    print(i)
csv_file.close()