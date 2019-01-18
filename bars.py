import json
import argparse
import os


class BadBarsData(Exception):
    pass


def try_open_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')


def get_arg_parser():
    default_file_path = './bars.json'
    arg_parser = argparse.ArgumentParser(description='Choose the best bar for the evening :)')
    arg_parser.add_argument('-c',
                            '--coordinate',
                            metavar='L',
                            type=float,
                            nargs=2,
                            help='longitude and latitude to find closest bar')
    arg_parser.add_argument('-f',
                            '--data_file',
                            default=default_file_path,
                            help='path to file with JSON data of bars')
    return arg_parser


def get_data_file_path():
    args = get_arg_parser().parse_args()
    return args.data_file


def get_position_from_args():
    args = get_arg_parser().parse_args()
    return args.coordinate


def get_position_from_keyboard():
    position_point = None
    try_to_input_count = 3
    print("Tell please longitude and latitude to find closest bar")
    for try_number in range(try_to_input_count):
        try:
            longitude = float(input('longitude: '))
            latitude = float(input('latitude: '))
            position_point = longitude, latitude
            break
        except ValueError:
            ask_again = ', please, try again. Example: 55.754285' if try_number < try_to_input_count-1 else ''
            print('Bad format {}\n'.format(ask_again))
    return position_point


def get_bar_position(bar):
    try:
        bar_position = bar['geometry']['coordinates']
    except (TypeError, KeyError):
        raise BadBarsData
    else:
        return bar_position


def load_serializable_object_from_file(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        json_data = file.read()
        serializable_object = None
        try:
            serializable_object = json.loads(json_data)
        except json.decoder.JSONDecodeError:
            raise BadBarsData
    return serializable_object


def get_distance_in_square_between_points(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2


def get_bar_size(bar):
    try:
        bar_size = bar['properties']['Attributes']['SeatsCount']
    except (TypeError, KeyError):
        raise BadBarsData
    else:
        return bar_size


def get_biggest_bar(bars):
    return max(bars, key=get_bar_size)


def get_smallest_bar(bars):
    return min(bars, key=get_bar_size)


def get_closest_bar(bars, longitude, latitude):
    my_point = [longitude, latitude]
    return min(bars, key=lambda bar: get_distance_in_square_between_points(get_bar_position(bar), my_point))


def get_bars():
    path_to_file_with_bars_data = get_data_file_path()
    bars_data = load_serializable_object_from_file(path_to_file_with_bars_data)
    try:
        bars = bars_data['features']
    except (TypeError, KeyError):
        raise BadBarsData
    else:
        return bars


def add_country_code_to_number(phone):
    country_code = '+7 '
    return (country_code if phone[1].isdigit() else '') + phone


def get_list_of_phone_numbers(phones):
    return list(map(lambda phone: add_country_code_to_number(phone['PublicPhone']), phones))


def show_bar(bar):
    bar_info = '\t\t"{name}"\n\t{address}\n\t{tel}\n'
    try:
        bar_title = bar['properties']['Attributes']['Name']
        bar_address = bar['properties']['Attributes']['Address']
        bar_phones = get_list_of_phone_numbers(bar['properties']['Attributes']['PublicPhone'])
    except (TypeError, KeyError):
        raise BadBarsData
    tel = '\n'.join(bar_phones)
    return bar_info.format(name=bar_title, address=bar_address, tel=tel)


def main():
    try:
        bars_list = get_bars()
        position_to_find_closest = get_position_from_args() or get_position_from_keyboard()

        biggest_bar = get_biggest_bar(bars_list)
        print('Biggest bar: ')
        print(show_bar(biggest_bar))

        smallest_bar = get_smallest_bar(bars_list)
        print('Smallest bar: ')
        print(show_bar(smallest_bar))

        if position_to_find_closest:
            closest_bar = get_closest_bar(bars_list, *position_to_find_closest)
            print('Closest bar: ')
            print(show_bar(closest_bar))

    except BadBarsData:
        error_message = 'Data from {file} has format mistakes. Check and try again, please'
        print(error_message.format(file=get_data_file_path()))


if __name__ == '__main__':
    main()
