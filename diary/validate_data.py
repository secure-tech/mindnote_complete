from .models import Page
import random

def validate_check():
    pages = Page.objects.all()

    for page in pages:
        value = random.randint(0,10)
        if(page.score<0 or page.score>10):
            print("감정 점수는 0에서 10사이의 숫자만 가능합니다.")
            page.score = value
            page.save()