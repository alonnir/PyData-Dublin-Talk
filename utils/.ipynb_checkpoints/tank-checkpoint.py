from time import sleep
import requests
import ast


def get_json(json_url, backup_path):
    """
    Fetches JSON from web address, falls back to reading from file.
    """
    
    print('Fetching JSON from website...')
    sleep(1)

    print('Live demo jitters...')
    
    headers = {'content-type': 'application/json', 
               'User-Agent': 'stat exercise'}

    
    r = requests.get(json_url, headers = headers)  # To do: headers
    
    if r.status_code == 200:
        print('Fetched successfully!')
        return r.json()
    
    else:
        print('Fetching failed :(. Status code: {}'.format(r.status_code))
        print('Reading backup JSON from file...')
        f = open(backup_path, 'r')
        json_bu = f.read()
        return ast.literal_eval(json_bu)
    
    


def find_example_spot(json):
    """
    Returns the first instance of a non-vacant parking space.
    """
    for i in range(len(json['cars'])):
        if len(json['cars'][i]['info']['carsList'])==0:
            continue
    else:
        return json['cars'][i]['info']

    # very unlikely, just in case of bug in the AutoTel system
    print('Could not find a non-empty parking space.')
    return None



def find_example_car(json):
    """
    Returns info on the first car parked in the first non-vacant parking space.
    """
    
    for i in range(len(json['cars'])):
        if len(json['cars'][i]['info']['carsList'])==0:
            continue
    else:

        k = list(json['cars'][i]['items'].keys())[0]
        
        return(json['cars'][i]['items'][k])



def describe_data(json):
    """
    Simple stats on currently parked cars in the JSON.
    """
    
    l = []

    for i in range(len(json['cars'])):
        cars_list = json['cars'][i]['info']['carsList']
        if len(cars_list)>0:
            l.extend(cars_list)
    
    print('Number of cars: {}\nMax car id: {}\nMin car id: {}\nMax-Min id: {}'.format(len(set(l)), max(l), min(l), max(l)-min(l)+1))




