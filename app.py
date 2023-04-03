import argparse
from generate_json import GenerateJSON, JSONPersistence
from store_in_azure import upload_blob_file


def collect_args():
    """ Collect args from command line to start processing data. """

    parser = argparse.ArgumentParser(description=__doc__, add_help=True)
    parser.add_argument("--row_count", help="Number of rows to generate", type=int)
    parser.add_argument("--file_name", help="Provide name for the file", type=str)
    parser.add_argument("--user_count", help="Number of user ids to generate", type=int)

    return parser.parse_args()


if __name__ == "__main__":
    # generate file and save it on the local system
    file_writer = JSONPersistence(collect_args())
    file_writer.save_lines_to_file()

    # move file to Azure blob storage
    path = file_writer.return_file_path()
    name = file_writer.return_file_name()
    upload_blob_file(path, name)




