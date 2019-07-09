from django.test import TestCase

# Create your tests here.






from snippets.models import Snippet,Author
from snippets.serializers import SnippetSerializer,AuthorSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print("hello, world")\n')
snippet.save()


author = Author(title='print("hello, world")\n')
author.save()

author = Author(title='print("world")\n')
author.save()

serializer = SnippetSerializer(snippet)
serializer.data

serializer=AuthorSerializer(author)
serializer.data

import io

stream = io.BytesIO(content)
data = JSONParser().parse(stream)

serializer = SnippetSerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data
# OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save()
# <Snippet: Snippet object>