from django.shortcuts import render
from . import ml_predict

def home(request):
    return render(request, 'index.html')

def result(request):
    print(request.GET)
    data = dict(**request.GET)
    data = dict(zip(data.keys(), [n[0] for n in data.values()]))

    prediction, probability = ml_predict.predict(**data)
    return render(request, 'result.html', {'prediction': prediction, 'probability': probability})


# def result(request):
#     age = request.GET['age']
#     fare = request.GET['fare']
#     title = request.GET['title']
#     pclass = request.GET['pclass']
#     sex = request.GET['sex']
#     sibsp = request.GET['sibsp']
#     age_input = request.GET['parch']
#     age_input = request.GET['embarked']

#     prediction = ml_predict.predict(age_input)
#     return render(request, 'result.html', {'prediction': prediction})
