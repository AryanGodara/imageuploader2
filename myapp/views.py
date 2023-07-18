from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory
from .models import Dataset, Image
from .forms import DatasetForm

def home(request):
    return render(request, 'myapp/base.html')

# def create_dataset(request):
#     ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=3)
#     if request.method == 'POST':
#         dataset_form = DatasetForm(request.POST)
#         image_formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
#         if dataset_form.is_valid() and image_formset.is_valid():
#             dataset = dataset_form.save()
#             for image_form in image_formset.cleaned_data:
#                 if image_form:
#                     image = image_form['image']
#                     name = image_form['name']
#                     Image.objects.create(name=name, image=image, dataset=dataset)
#             return redirect('dataset_list')
#     else:
#         dataset_form = DatasetForm()
#         image_formset = ImageFormSet(queryset=Image.objects.none())
#     return render(request, 'myapp/create_dataset.html', {'dataset_form': dataset_form, 'image_formset': image_formset})

# def create_dataset(request):
#     if request.method == 'POST':
#         print("\n\n\nPOST\n\n\n")
#         print(request.POST)
#         print("\n\n\nFILES\n\n\n")
#         print(request.FILES)
#         # dataset_form = DatasetForm(request.POST)
#         # image_formset = ImageFormSet(request.POST, request.FILES, prefix='images')
#         dataset_form = DatasetForm(request.POST, request.FILES)
#         image_formset = ImageFormSet(request.POST, request.FILES)
#         print("\n\nERROR\n\n", image_formset.errors)
#         print(dataset_form.is_valid())
#         print(image_formset.is_valid())
#         if dataset_form.is_valid() and image_formset.is_valid():
#             print("\n\n\nVALID\n\n\n")
#             dataset = dataset_form.save()
#             image_formset = ImageFormSet(request.POST, request.FILES, instance=dataset)
#             print(image_formset.is_valid())
#             images = image_formset.save(commit=False)
#             print(len(images))
#             for image in images:
#                 print("\nIMAGE\n")
#                 image.dataset = dataset
#                 image.save()
#             return redirect('list_dataset')
#             # Redirect to the dataset detail page
#             # return redirect('dataset_detail', dataset_id=dataset.id)
#     else:
#         dataset_form = DatasetForm()
#         image_formset = ImageFormSet(queryset=Image.objects.none())
#     return render(request, 'myapp/create_dataset.html', {'dataset_form': dataset_form, 'image_formset': image_formset})

def create_dataset(request):
    if request.method == 'POST':
        form = DatasetForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            images = request.FILES.getlist('images')

            # Create a new dataset object and save it
            dataset = Dataset(name=name, title=title, description=description)
            dataset.save()

            # Save each image to the dataset model
            for image in images:
                dataset.images.create(image=image)

            return redirect('list_dataset')  # Replace 'success_url' with the URL to redirect after successful upload
    else:
        dataset_form = DatasetForm()
    return render(request, 'myapp/create_dataset.html', {'dataset_form': dataset_form})

def dataset_list(request):
    datasets = Dataset.objects.all()
    return render(request, 'myapp/list_dataset.html', {'datasets': datasets})

def dataset_detail(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk)
    return render(request, 'myapp/dataset_detail.html', {'dataset': dataset})