from django.shortcuts import render, redirect
from django.http import HttpResponse
import pickle
import pandas as pd  # Assuming you'll use pandas for DataFrame
import os

# Create your views here.
# request -> response
# request handler

# Create your views here.
def index_func(request):
    # print(f"Request method: {request.method}")
    # print(f"Request POST data: {request.POST}")
    # print(f"Request2 POST data: {request}")
    # print('#####################00')
    try:
        predictions = 0.0
        print('#####################11')
        if request.method == 'POST':
            print('####################11#')
            name = request.POST.get('Name', '')
            year = request.POST.get('year', '')
            km = request.POST.get('km', '')
            fuel = request.POST.get('fuel', '')
            dealer = request.POST.get('dealer', '')
            trans = request.POST.get('trans', '')
            seats = request.POST.get('seats', '')
            rpm = request.POST.get('rpm', '')
            mil = request.POST.get('mil', '')
            eng = request.POST.get('eng', '')
            power = request.POST.get('power', '')
            owner = request.POST.get('owner', '')
            print('#####################22')
           
            if not name or not year or not km or not fuel or not dealer or not trans or not seats:
                return HttpResponse("All fields are required", status=400)

            if name != "":
                # df = pd.DataFrame(columns=['year', 'km_driven', 'fuel',
                #                            'seller_type', 'transmission', 'seats',
                #                            'torque_nm', 'mileage_kmpl', 'engine_cc', 'max_power_bhp',
                #                            'First Owner', 'Fourth & Above Owner',
                #                            'Second Owner', 'Test Drive Car', 'Third Owner'])
                
                 # Create a dictionary with the data
                # df2 = {'year': int(2019),'km_driven': float(105000),'fuel': float(1),
                #    'seller_type': int(1),'transmission': int(1),'seats': int(4),
                #    'torque_nm': float(280),'mileage_kmpl': float(21), 'max_power_bhp': float(85), 'engine_cc': float(1800),
                #    'First Owner': 1,'Fourth & Above Owner': 0,
                #    'Second Owner': 0,'Test Drive Car': 0,'Third Owner': 0}

                df = pd.DataFrame(columns=['year', 'km_driven', 'fuel',
                           'seller_type', 'transmission', 'seats',
                           'torque_nm', 'mileage_kmpl', 'max_power_bhp', 'engine_cc',
                           'First Owner', 'Fourth & Above Owner',
                           'Second Owner', 'Test Drive Car', 'Third Owner'])
                Ownership = Helper(owner)

                # df2 = {'year': int(year), 'km_driven': float(km), 'fuel': float(fuel),
                #        'seller_type': int(dealer), 'transmission': int(trans), 'seats': int(seats),
                #        'torque_nm': float(rpm), 'mileage_kmpl': float(mil), 'engine_cc': float(eng),
                #        'max_power_bhp': float(power), 'First Owner': Ownership[0], 'Fourth & Above Owner':
                #        Ownership[1], 'Second Owner': Ownership[2], 'Test Drive Car': Ownership[3],
                #        'Third Owner': Ownership[4]}
                df2 = {'year': int(year), 'km_driven': float(km), 'fuel': fuel,
                        'seller_type': int(dealer), 'transmission': int(trans), 'seats': int(seats),
                        'torque_nm': float(rpm), 'mileage_kmpl': float(mil), 'max_power_bhp': float(power), 
                        'engine_cc': float(eng), 'First Owner': Ownership[0], 
                        'Fourth & Above Owner': Ownership[1], 'Second Owner': Ownership[2], 
                        'Test Drive Car': Ownership[3], 'Third Owner': Ownership[4]}

                df = pd.concat([df, pd.DataFrame([df2])], ignore_index=True)

                filename = 'playground/CarSelling.pickle'
                if not os.path.exists(filename):
                    return HttpResponse("Model file not found.", status=500)
                loaded_model = pickle.load(open(filename, 'rb'))

                predictions = loaded_model.predict(df)
                print(predictions)
                return render(request, 'index.html', {'result': predictions[0]})
            else:
                print('name error ####22')

                return redirect('hellopage')
        return render(request, 'index.html')
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)
   
   
def Helper(x):
    if x == '1':
        return [1, 0, 0, 0, 0]
    elif x == '2':
        return [0, 0, 1, 0, 0]
    elif x == '3':
        return [0, 0, 0, 0, 1]
    if x == '4':
        return [0, 1, 0, 0, 0]
    if x == '5':
        return [0, 0, 0, 1, 0]

