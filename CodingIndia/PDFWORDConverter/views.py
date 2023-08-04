from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,  FileResponse
from PyPDF2 import PdfReader
import subprocess
import mimetypes
from .models import Document

def upload_file(request):
    if request.method == 'POST':
        pdf_file = request.FILES['pdf_file']
        document = Document.objects.create(pdf_file=pdf_file)
        convert_to_word(document)
        return render(request, 'PDFWORDConverter/success.html', {'document': document})
    return render(request, 'PDFWORDConverter/upload.html')

# def convert_to_word(document):
#     pdf_path = document.pdf_file.path
#     word_path = pdf_path[:-3] + 'docx'
#     subprocess.run(['unoconv', '-f', 'docx', '-o', word_path, pdf_path])
#     document.word_file.name = word_path
#     document.save()

def convert_to_word(document):
    pdf_path = document.pdf_file.path
    word_path = pdf_path[:-3] + 'docx'
    subprocess.run(['unoconv', '-f', 'docx', '-o', word_path, '--exec', '/path/to/libreoffice/bin/soffice', pdf_path])
    document.word_file.name = word_path
    document.save()

# def download_word(request, document_id):
#     document = get_object_or_404(Document, id=document_id)
#     word_file = open(document.word_file.path, 'rb')
#     response = HttpResponse(word_file, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#     response['Content-Disposition'] = 'attachment; filename="converted.docx"'
#     return response


def download_word(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    word_file = open(document.word_file.path, 'rb')
    response = FileResponse(word_file, content_type=mimetypes.guess_type(document.word_file.path)[0])
    response['Content-Disposition'] = 'attachment; filename="converted.docx"'
    return response