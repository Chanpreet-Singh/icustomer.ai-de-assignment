# icustomer.ai-de-assignment
### Solution to the hiring task of Data Engineer position at icustomer.ai
#### Technical stack used
- [Debian/Ubuntu 20.04 LTS](https://releases.ubuntu.com/focal/ "Debian/Ubuntu 20.04 LTS")
- [Python 3.11](https://www.python.org/downloads/release/python-3117/)
- [MySQL Server 8.0.39](https://dev.mysql.com/downloads/mysql/8.0.html)
- [Apache Airflow]()

#### Pre-requisites
Make sure you have Python, Airflow and MySQL installed in your machine.

#### Steps to setup the project
1. Take a clone of this repository using the command: `git clone https://github.com/Chanpreet-Singh/icustomer.ai-de-assignment.git`
2. Go inside the folder: `cd icustomer.ai-de-assignment`
3. Create Virtual Environment of the desired Python3 version(prefer: [Python 3.11](https://www.python.org/downloads/release/python-3117/) as stated above) using the command: `python3.11 -m venv ./setup/venv`
This will create a virtual environment named as venv. You can choose to name it accordingly. Just replace the last breadcrumb of the last parameter as your preferred name, say icustomer_env then: `python3.11 -m venv ./setup/icustomer_env`
4. Now, activate the virtual environment: `source ./setup/venv/bin/activate`
5. Install the dependencies by referring to the file attached: `pip install -r ./setup/requirements.txt`
Please note that, this step would be required only once in the beginning while setting up the project.

#### How to generate synthetic data for the assignment
- Synthetic data is nothing but generated in the format to showcase the working of the questions
- More details can be found [here](https://github.com/Chanpreet-Singh/icustomer.ai-de-assignment/blob/main/generate_synthetic_data/synthetic%20data%20README.md)
