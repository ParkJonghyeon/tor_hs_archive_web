import json
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect


def date_str_to_filename(date_str, hour_str):
    date_str = date_str.replace('-','') + hour_str.replace(':','')[:2]
    filename = 'hs_data_'+date_str+'.json'
    return filename


def filename_to_str(filename):
    date_str = filename.replace('.json','').split('_')[-1]
    formatted_date_str = date_str[0:4]+'-'+date_str[4:6]+'-'+date_str[6:8]
    formatted_hour_str = date_str[8:10]+':00'
    return formatted_date_str, formatted_hour_str


def data_init():
    data_list = os.listdir('/media/lark/extra_storage/onion_web/view_page/hs_data')
    data_list.sort()
    with open('/media/lark/extra_storage/onion_web/view_page/hs_data/'+data_list[-1],'r') as d:
        data = json.load(d)
    data_date, data_hour = filename_to_str(data_list[-1])
    return data, data_date, data_hour


def data_reload(date):
    with open('/media/lark/extra_storage/onion_web/view_page/hs_data/'+date) as d:
        data = json.load(d)
    return data


def main_view_load(request):
    if request.GET.get('date_selector'):
        data_date = request.GET.get('date_selector')
        data_hour = '00:00'
        return redirect('main_view_reload', date_str=data_date, hour_str=data_hour)
    data, data_date, data_hour = data_init()
    data = sorted(data, key=lambda k:len(k['bitcoin_wallet_address']), reverse=True)
    return render(request, 'view_page/index_view.html', {'d':data, 'date':data_date, 'hour':data_hour})


def main_view_reload(request, date_str, hour_str):
    if request.GET.get('date_selector'):
        data_date = request.GET.get('date_selector')
        data_hour = '00:00'
        return redirect('main_view_reload', date_str=data_date, hour_str=data_hour)
    data = data_reload( date_str_to_filename(date_str, hour_str) )
    data = sorted(data, key=lambda k:len(k['bitcoin_wallet_address']), reverse=True)
    return render(request, 'view_page/main_view.html', {'d':data, 'date':date_str, 'hour':hour_str, 'today_new_live':30, 'today_total_live':3000, 'today_change_dead':100, 'today_total_dead':9000 })


def bitcoin_list_view_load(request, date_str, hour_str, onion_address):
    onion_address = 'http://'+onion_address
    data = data_reload( date_str_to_filename(date_str, hour_str) )
    data = next(json_item for json_item in data if json_item['onion_address'] == onion_address)
    return render(request, 'view_page/bitcoin_list_view.html', {'d':data, 'date':date_str, 'hour':hour_str, 'today_new_live':30, 'today_total_live':3000, 'today_change_dead':100, 'today_total_dead':9000 })


def bitcoin_transaction_view_load(request, bitcoin_wallet_address):
    with open('/media/lark/extra_storage/onion_web/view_page/transaction/'+bitcoin_wallet_address+'.json') as d:
        transaction = json.load(d)
    return render(request, 'view_page/bitcoin_transaction_view.html', {'btc_address':bitcoin_wallet_address, 'transaction':transaction})

