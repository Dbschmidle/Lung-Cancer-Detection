import requests

def main():
    '''
    Tests app.py
    '''

    url = "http://127.0.0.1:5000/predict"


    files = {'file': open('./lung_colon_image_set/lung_image_sets/lung_n/lungn1.jpeg', 'rb')}
    response = requests.post(url, files=files)
    print(response.json())

    files = {'file': open('./lung_colon_image_set/lung_image_sets/lung_aca/lungaca1.jpeg', 'rb')}
    response = requests.post(url, files=files)
    print(response.json())


    files = {'file': open('./lung_colon_image_set/lung_image_sets/lung_scc/lungscc1.jpeg', 'rb')}
    response = requests.post(url, files=files)
    print(response.json())
    
    
if __name__ == "__main__":
    main()