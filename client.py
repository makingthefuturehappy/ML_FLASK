import requests

if __name__ == '__main__':
    # features_params = [1,1,1,0]
    r = requests.post('http://localhost:5000/predict', json={'params': [3,5]})
