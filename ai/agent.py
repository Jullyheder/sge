import json
from django.conf import settings
from django.core import serializers
from openai import OpenAI
from ai import prompts, models
from products.models import Product
from outflows.models import Outflow


class SGEAgent:

    def __init__(self):
        self.__client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def __get_data(self):
        products = Product.objects.all()
        outflows = Outflow.objects.all()

        data = {
            'products': serializers.serialize('json', products),
            'outflows': serializers.serialize('json', outflows),
        }

        return json.dumps(data)

    def invoke(self):
        response = self.__client.responses.create(
            model=settings.OPENAI_MODEL,
            input=[
                {
                    'role': 'system',
                    'content': prompts.SYSTEM_PROMPT
                },
                {
                    'role': 'user',
                    'content': prompts.USER_PROMPT.replace(
                        '{{data}}',
                        self.__get_data()
                    )
                }
            ]
        )

        result = response.output_text

        models.AIResult.objects.create(
            result=result
        )
