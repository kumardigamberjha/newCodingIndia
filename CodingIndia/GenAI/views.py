from django.shortcuts import render
import os
import google.generativeai as genai
from CodingIndia.settings import geminiAPI
from IPython.display import Markdown
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.
def GenIntro(request):
    data = ""
    context = {'data': data}
    return render(request, 'GenAI/index.html', context)


'''###################################################################################################
                                Get AI Response
###################################################################################################'''

@csrf_exempt
def GenAIConversation(request):
    res = "Hello"
    """
    At the command line, only need to run once to install the package via pip:

    $ pip install google-generativeai
    """
    if request.method == "POST":
        name = request.POST.get('geninput')
        print("Name: ", name)
        genai.configure(api_key=geminiAPI)

        # Set up the model
        generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
        }

        safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        }
        ]

        model = genai.GenerativeModel(model_name="gemini-pro",
                                    generation_config=generation_config,
                                    safety_settings=safety_settings)

        prompt_parts = [
            name
        ]

        response = model.generate_content(prompt_parts)
        print(response.text)
        # model = genai.GenerativeModel('gemini-pro')

        # response = model.generate_content("List 5 planets each with an interesting fact")

        # data = Markdown(response.text)
        data = response.text
        return JsonResponse({'response': data}, status=200)
    return JsonResponse({'response': "error"}, status=400)