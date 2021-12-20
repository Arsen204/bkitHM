from django.shortcuts import render, redirect, get_object_or_404
from app.models import Computer, Processor
from app.forms import AddComputerForm


def get_computers(request):
    return render(request, 'report.html', {
        'data': {
            'computers': Computer.objects.all(),
            'processors': Processor.objects.all(),
        }
    })


def create_computer(request):
    if request.method == 'POST':
        form = AddComputerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            processor_id = form.cleaned_data['processor']
            processor = Processor.objects.filter(id=processor_id)[0]
            Computer.objects.create(name=name, processor=processor)
    return redirect('main')


def update_computer(request, computer_id):
    if request.method == 'POST':
        form = AddComputerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            processor_id = form.cleaned_data['processor']
            processor = Processor.objects.filter(id=processor_id)[0]
            Computer.objects.filter(id=computer_id).update(name=name, processor=processor)
    return redirect('main')


def delete_computer(request, computer_id):
    computer = get_object_or_404(Computer, id=computer_id)
    computer.delete()
    return redirect('main')
