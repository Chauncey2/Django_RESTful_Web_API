from .models import Name
from  rest_framework import serializers

class NameSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Name
        fields =('id','name','sex','age')
    # class Meta:
    #
    #     module=Name
    #     field={'name','sex','age'}