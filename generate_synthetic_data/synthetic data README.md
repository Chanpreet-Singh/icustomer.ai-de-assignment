#### What the script is doing?
##### About data:
- Generating 2000 data points as defined in the constants [here](https://github.com/Chanpreet-Singh/icustomer.ai-de-assignment/blob/main/utils/constants.py#L4).
- Every value in the <b>interaction_id</b> is unique.
- <b>user_id</b> is from a pool of 25 user_ids which are unique and generated dynamically
- <b>product_id</b> is from a pool of 25 product_ids which are unique and generated dynamically
- <b>action</b> is a random value between [1, 5]
- <b>timestamp</b> is a random epoch timestamp between 1st Jan 2024 and current time of execution
- Random values in <b>interaction_id</b>, <b>user_id</b> and <b>product_id</b> is generated with the help of [secrets](https://pypi.org/project/secrets/) library.

##### File and Folder I/O
- In the beginning, it is create a new folder <b>data</b>, if already present then it deletes the old one and creates a new one.
- The final csv file is named as <b>synthetic_data.csv</b> and the file path would be <b>data/synthetic_data.csv</b>
- Each execution will override the file with new data, if a file is already present.
