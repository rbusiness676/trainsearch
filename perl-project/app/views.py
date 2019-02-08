import os
import pdb
from os.path import isfile, join

from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_400_BAD_REQUEST

def mysetsortfunc(element):
    index=4
    return element[index]

@api_view(['GET'])
def process_train_search(request):
    try:

        FIELD_SEP = ['-',',']
        origin = request.GET.get('origin')
        destination = request.GET.get('destination')
        if (len(origin) == 0) or (len(destination) == 0):
            return HttpResponse(content="Input Empty", status=HTTP_400_BAD_REQUEST)

        #build search string
        search_strs = []
        search_strs.append(origin + FIELD_SEP[0] + destination)
        search_strs.append(origin + FIELD_SEP[1] + destination)

        #get all input providerData files
        file_dir =  os.path.join(os.path.dirname(os.path.abspath(__file__)),'providerData')
        onlyfiles = [f for f in os.listdir(file_dir) if not isfile(f)]

        #get all the matching lines
        data = []
        for file in onlyfiles:
            file_path = os.path.join(file_dir, file)
            if isfile(file_path) == False:
                continue
            with open(file_path) as fp:
                for line in fp:
                    if line.startswith((search_strs[0],search_strs[1])):
                        line = line.rstrip('\r\n')
                        if line not in data:
                            data.append(line)

        #now make them order by 'Price', 'departure time
        dataset=set()
        for line in data:
            if line.startswith(search_strs[0]):
                dataset.add(tuple(line.split(FIELD_SEP[0])))
            elif line.startswith(search_strs[1]):
                dataset.add(tuple(line.split(FIELD_SEP[1])))

        if len(dataset) > 0:
            dataset = sorted(dataset, key=lambda x: (x[4], x[2]))#mysetsortfunc)

        response_data_list=[]

        for rec in dataset:
            response_data = {}
            response_data['Origin'] = rec[0]
            response_data['Destination'] = rec[1]
            response_data['Time'] = {}
            response_data['Time']['Departure Time'] = rec[2]
            response_data['Time']['Destination Time'] = rec[3]
            response_data['Price'] = rec[4]
            response_data['Currency'] = rec[5]
            response_data_list.append(response_data)

        if len(dataset):
            return JsonResponse(data=response_data_list,json_dumps_params={'indent': 2}, safe=False)
        else:
            return JsonResponse(data="No Record matches for this search", json_dumps_params={'indent': 2}, safe=False)

    except Exception as e:
        return JsonResponse(data="Internal server error", json_dumps_params={'indent': 2}, safe=False)