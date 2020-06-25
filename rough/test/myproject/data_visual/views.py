from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import django_tables2 as tables
import csv

# Create your views here.
# def display_table(request):
#     a = pd.read_csv("data/data.csv")
#     a.to_html("templates/submission.html")
#     html_file = a.to_html()
#     return HttpResponse(html_file)
#
# def display_table(request):
#     a = pd.read_csv("data/data.csv")
#     a.to_html("templates/submission.html")
#     html_file = a.to_html()
#     return HttpResponse(html_file)

def display_table(request):
    data = []
    html_file = """
    <html>
    <head></head>
    <body>
    <h1> some header here</h1>
    <br>
    """
    with open("data/data.csv") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            data.append(row)
    html_file =   render(request, 'Table.htm',
                      {'data': data})
    return HttpResponse(html_file)
