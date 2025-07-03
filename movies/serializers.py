from rest_framework import serializers

from .models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'
    
    def get_rate(self, obj):
        reviews = obj.reviews.all()
        
        if reviews:
            sum_reviews = 0
            
            for review in reviews:
                sum_reviews += review.stars
            
            reviews_count = reviews.count()

            return round(sum_reviews / reviews_count, 1)
            
        return None
        
    def validate_synopsis(self, value):
        
        if len(value) > 200:
            raise serializers.ValidationError("A sinopse não pode ser maior que 200 caracteres.")
        return value
