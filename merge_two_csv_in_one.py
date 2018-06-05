import csv
import argparse


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'csv_first',
        type=str,
        help='File path to first csv file',
        nargs='?',
        default='first.csv'
    )
    parser.add_argument(
        'csv_second',
        type=str,
        help='File path to second csv file',
        nargs='?',
        default='second.csv'
    )
    parser.add_argument(
        'csv_output',
        type=str,
        help='File path to output csv file',
        nargs='?',
        default='output.csv'
    )
    return parser.parse_args()


def read_csv(file_path):
    csv_list = []
    reader = csv.DictReader(file_path)
    for row in reader:
        csv_list.append(row)
    return csv_list, reader.fieldnames


def writer_csv(field_names, data, file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as output_csv:
        writer = csv.DictWriter(
            output_csv,
            delimiter=',',
            fieldnames=field_names,
        )
        writer.writeheader()
        for row in data:
            writer.writerow(row)


if __name__ == '__main__':
    args = arg_parse()
    csv_first = args.csv_first
    csv_second = args.csv_second
    csv_output = args.csv_output
    print('Open and read {} file'.format(csv_first))
    with open(csv_first, 'r', encoding='utf-8') as one_csv:
        csv_list_first, field_names_first = read_csv(one_csv)
    print('Open and read {} file'.format(csv_second))
    with open(csv_second, 'r', encoding='utf-8') as two_csv:
        csv_list_second, field_names_second = read_csv(two_csv)
    id_product_key = field_names_first[0]
    url_field = field_names_second[1]
    field_name_list = field_names_first + [url_field]
    for first_csv_row in csv_list_first:
        for second_csv_row in csv_list_second:
            if first_csv_row.get(
                id_product_key
            ) == second_csv_row.get(
                id_product_key
            ):
                first_csv_row.update(
                    {url_field: second_csv_row.get(url_field)}
                )
    print('Merge and write {} file'.format(csv_output))
    writer_csv(field_name_list, csv_list_first, csv_output)
