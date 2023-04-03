import argparse
import json
from faker import Faker
import uuid
import random
import os


class GenerateJSON:
    """Class that generates social media data in JSON format. """

    def __init__(self, args: argparse.Namespace):
        self.args_dict = vars(args)
        self.row_count = self.args_dict["row_count"]
        self.file_name = self.args_dict["file_name"]
        self.user_count = self.args_dict["user_count"]
        self.fake = Faker()

    def generate_regular_line(self):
        json_dict = dict()
        json_dict['action_id'] = str(uuid.uuid4())
        json_dict['user_id'] = random.randint(1, self.user_count)
        json_dict['action'] = random.choice(['like', 'dislike', 'comment', 'post', 'repost', 'delete'])
        json_dict['action_desc'] = f"{json_dict['user_id']} performed {json_dict['action']} " \
                                   f"for item {random.randint(1, 1000000)}"
        json_dict['timestamp'] = self.fake.date_time_between(start_date='-1y', end_date='now').\
            strftime('%Y-%m-%d %H:%M:%S')
        json_dict['device_type'] = random.choice(['mobile', 'computer', 'tablet', 'desktop', 'smartwatch'])
        json_dict['user_ip'] = self.fake.ipv4()

        return json_dict

    def add_suspicious_line(self):

        suspicious_data = list()
        same_timestamp = self.fake.date_time_between(start_date='-1y', end_date='now').\
            strftime('%Y-%m-%d %H:%M:%S')
        same_ip = self.fake.ipv4()

        # Replace few lines to add the same values for timestamp and IP
        for i in range(random.randint(6, 15)):
            dict_to_change = self.generate_regular_line()
            dict_to_change['timestamp'] = same_timestamp
            dict_to_change['user_ip'] = same_ip
            suspicious_data.append(dict_to_change)

        return suspicious_data


class JSONPersistence(GenerateJSON):
    def __init__(self, args):
        super().__init__(args)

    def save_lines_to_file(self):
        json_data_list = list()

        with open(f"{self.file_name}.json", "w") as current_opened_file:
            for j in range(int(self.row_count * 0.9)):
                line = self.generate_regular_line()
                json_data_list.append(line)

            for k in range(int(self.row_count * 0.1)):
                line = self.add_suspicious_line()
                json_data_list.append(line)

            json.dump(json_data_list, current_opened_file)

    def return_file_name(self):
        return self.file_name + ".json"

    @staticmethod
    def return_file_path():
        current_directory = os.getcwd()
        return current_directory







