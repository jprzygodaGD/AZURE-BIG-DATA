import argparse
from generate_json import GenerateJSON, JSONPersistence


def collect_args():
    """ Collect args from command line to start processing data. """

    parser = argparse.ArgumentParser(description=__doc__, add_help=True)
    parser.add_argument("--row_count", help="Number of rows to generate", type=int)
    parser.add_argument("--file_name", help="Provide name for the file", type=str)
    parser.add_argument("--user_count", help="Number of user ids to generate", type=int)

    return parser.parse_args()


if __name__ == "__main__":
    file_writer = JSONPersistence(collect_args())
    file_writer.save_lines_to_file()



