import json, os

data_file = "expense.json"
base_path = os.getcwd()
data_file_path = os.path.join(base_path, data_file)

def load_expenses():
    if not os.path.exists(data_file_path):
        return []
    try:
        with open (data_file_path, "r") as exp:
            data = json.load(exp)
        return data
    except:
        return []
        
def save_expenses(expenses):
    with open (data_file_path, "w") as exp:
        json.dump([e.to_dict() for e in expenses], exp, indent=4)