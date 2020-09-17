import pandas as pd

def readvanilla():
    # Reads Dataset and stores results in dictionary
    # Only for python3.8
    data = {"S_L":[],"S_W":[],"P_L":[],"P_W":[],"CL":[]}
    filepath = "data/iris.data"
    with open(filepath,"r") as f:
        while (line:=f.readline().strip("\n").split(",")) and len(line) == len(data.keys()):
            for idx,key in enumerate(data.keys()):
                try:
                    data[key].append(float(line[idx]))
                except ValueError as e:
                    data[key].append(line[idx])
    return data


def read_pandas(filepath):

    df = pd.read_csv(filepath)

    return df

if __name__ == "__main__":
    filepath = "./data/iris.data"
    df = read_pandas(filepath)
    print(df)
