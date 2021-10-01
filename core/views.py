from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome,idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome,idade))

def soma(request, num_a,num_b):
    return HttpResponse('A soma de {} e {} é {}'.format(num_a,num_b,num_a+num_b))

def subtracao(request, num_a,num_b):
    return HttpResponse('A subtração de {} por {} é {}'.format(num_a,num_b,num_a-num_b))

def divisao(request, num_a,num_b):
    return HttpResponse('A divisão de {} por {} é {}'.format(num_a,num_b,num_a/num_b))

def multiplicacao(request, num_a,num_b):
    return HttpResponse('A multiplicação de {} e {} é {}'.format(num_a,num_b,num_a*num_b))