import datetime
import traceback

from utils import constants
from utils import excel_utils
from utils import folder_utils
from utils import random_utils

"""
This script will generate syntetic data in a csv format containing the following fields:

interaction_id : STRING, 
user_id: STRING,
product_id: STRING
action: INTEGER
timestamp: isotimestamp
"""

class Randomdatagenerator:
    def __init__(self):
        self.users_list = [random_utils.get_unique_random_string(10) for i in range(25)] # Creating a pool of 25 users, length of each user_id=10
        self.products_list = [random_utils.get_unique_random_string(10) for i in range(25)] # Creating a pool of 25 products, length of each product_id=10
        self.action_list = [each for each in range(1, 6)]
        folder_utils.create_folder(constants.data_folder, overwrite=True)

    def create_data(self):
        data_list = []
        for i in range(constants.total_data_points):
            try:
                data_point = {
                                "interaction_id": random_utils.get_unique_random_string(10),
                                "user_id": random_utils.get_random_choice_from_list(self.users_list),
                                "product_id": random_utils.get_random_choice_from_list(self.products_list),
                                "action": random_utils.get_random_choice_from_list(self.action_list),
                                "timestamp": int(random_utils.get_random_timestamp(datetime.datetime(2024, 1, 1, 0, 0, 0), datetime.datetime.now()))
                            }
                data_list.append(data_point)
            except Exception as e:
                print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
        return data_list

    def main(self):
        data_list = self.create_data()
        data_df = excel_utils.convert_list_into_dataframe(data_list)
        write_status = excel_utils.dump_csv_file(data_df, constants.synthetic_data_file)
        print("File dump status - {0} at {1}".format(write_status, constants.synthetic_data_file))

if __name__ == '__main__':
    cls_obj = Randomdatagenerator()
    cls_obj.main()