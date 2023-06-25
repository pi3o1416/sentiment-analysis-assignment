
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import sentiment_model
from .serializers import RequestSerializer, ResponseSerializer


class TextSentimentAnalysis(APIView):
    @extend_schema(request=RequestSerializer, responses={200: ResponseSerializer})
    def post(self, request):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data.get('text')
            highest_ranked_lebel = sentiment_model.classify_text(text)
            return Response(data={"sentiment": highest_ranked_lebel}, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
