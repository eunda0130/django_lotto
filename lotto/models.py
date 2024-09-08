from django.db import models
from django.utils import timezone
import random


# Create your models here.
class GuessNumbers(models.Model):
   name = models.CharField(max_length=24) # �ζ� ��ȣ ����Ʈ�� �̸�
   text = models.CharField(max_length=255) # �ζ� ��ȣ ����Ʈ�� ���� ����
   lottos = models.CharField(max_length=255, default='[1, 2, 3, 4, 5, 6]') # �ζ� ��ȣ���� ��� str
   num_lotto = models.IntegerField(default=5) # 6�� ��ȣ set�� ����
   update_date = models.DateTimeField()
   def generate(self):
       self.lottos = ""
       origin = list(range(1,46)) # 1~45�� ���� ����Ʈ [1, 2, 3, ..., 43, 44, 45]
 # 6�� ��ȣ set ������ŭ 1~46 �ڼ��� �� ���� 6�� ��󳻾� sorting
       for _ in range(0, self.num_lotto):
            random.shuffle(origin) # [10, 21, 36, 2, ... , 1, 11]
            guess = origin[:6] # [10, 21, 36, 2, 15, 23]
            guess.sort() # [2, 10, 15, 21, 23, 36]
            self.lottos += str(guess) +'\n' # �ζ� ��ȣ str�� 6�� ��ȣ set �߰� -> '[2, 10, 15, 21, 23, 36]\n'
 # self.lottos : '[2, 10, 15, 21, 23, 36]\n[1, 15, 21, 27, 30, 41]\n...'
       self.update_date = timezone.now()
       self.save() # GuessNumbers object�� DB�� ����
   def __str__(self): 
        return "pk {} : {} - {} ".format(self.pk, self.name, self.text)