from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length = 100)
    content = serializers.CharField()

    class Meta:
        model = Post # serializer와 관련된 모델 클래스 지정
        fields = ["id", "title", "content"] # 직렬화할 필드 정의
        # exclude -> 직렬화에서 제외할 필드, fields나 exclude중 하나만 사용 가능, 근데 fields 사용하기
        # read_only_fields -> 읽기 전용 필드 정의, 모델의 역직렬화된 표현에 포함되지 x
        # extra_kwargs -> 사용자 정의 검증, 필드 수준의 권한 또는 기타 필드별 설정 ...
        # validators -> 추가적인 유효성 검사를 할 수 있는 검증기 지정