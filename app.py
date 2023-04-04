import argparse
from generate_data import GenerateDict, JSONPersistence, CSVPersistence
from store_in_azure import upload_blob_file
import os
import sys
import logging


def collect_args():
    """ Collect args from command line to start processing data. """

    parser = argparse.ArgumentParser(description=__doc__, add_help=True)
    parser.add_argument("--row_count", help="Number of rows to generate", type=int)
    parser.add_argument("--file_name", help="Provide name for the file", type=str)
    parser.add_argument("--user_count", help="Number of user ids to generate", type=int)
    parser.add_argument("--filetype", help="Can be either JSON or CSV", choices=["JSON", "CSV"])

    return parser.parse_args()


if __name__ == "__main__":

    args = collect_args()
    logging.getLogger()

    # Check what file should be generated
    if args.filetype.upper() == "CSV":
        data_writer = CSVPersistence(args)
        data_writer.save_csv()
    elif args.filetype.upper() == "JSON":
        data_writer = JSONPersistence(args)
        data_writer.save_json()
    else:
        logging.error("Invalid file type")
        sys.exit(1)

    # Check if Azure key is exported
    azure_key = os.getenv('AZURE_KEY')
    if azure_key is None:
        logging.error("Azure key is missing...")
        sys.exit(2)
    else:
        path = os.getcwd()
        name = data_writer.return_file_name()
        upload_blob_file(path, name, azure_key)




