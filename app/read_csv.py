import csv


def read_csv(path):
  with open(path, newline='\n', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = dict(iterable)
      # country_dict = dict(iterable)
      data.append(country_dict)
    return data


if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data)
