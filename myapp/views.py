import os
import tempfile
import shutil
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.utils.text import slugify

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory
from .models import Dataset, Image
from .forms import DatasetForm

def home(request):
    return render(request, 'myapp/base.html')

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

def dataset_delete(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk)
    dataset.delete()
    return redirect('list_dataset')

def dataset_list(request):
    datasets = Dataset.objects.all()
    return render(request, 'myapp/list_dataset.html', {'datasets': datasets})

def dataset_detail(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk)
    return render(request, 'myapp/dataset_detail.html', {'dataset': dataset})

def download_images(request, dataset_id):
    dataset = Dataset.objects.get(id=dataset_id)
    images = dataset.images.all()

    # Create a temporary directory to store the images
    temp_dir = tempfile.mkdtemp()

    try:
        # Add the images to the temporary directory
        for image in images:
            image_path = image.image.path
            shutil.copy(image_path, temp_dir)

        # Create the zip file
        zip_filename = f"{slugify(dataset.title)}_images.zip"
        zip_file_path = os.path.join(tempfile.gettempdir(), zip_filename)
        shutil.make_archive(zip_file_path[:-4], 'zip', temp_dir)

        # Serve the zip file for download
        with open(zip_file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/zip')
            response['Content-Disposition'] = f'attachment; filename="{zip_filename}"'

        # Remove the temporary directory and zip file
        shutil.rmtree(temp_dir)
        os.remove(zip_file_path)

        return response

    except Exception as e:
        # In case of any error, make sure to clean up the temporary directory and file
        shutil.rmtree(temp_dir, ignore_errors=True)
        os.remove(zip_file_path, ignore_errors=True)
        raise e

def image(request):
    return render(request,'myapp/images.html')
