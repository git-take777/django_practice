from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from snippets.models import Snippet #Snippetモデルをインポート
from django.shortcuts import get_object_or_404

def top(request):
  snippets = Snippet.objects.all() #Snippetsの一覧を取得
  context = {"snippets" : snippets} #テンプレートエンジンに与えるPython オブジェクト
  return render(request, 'snippets/top.html', context) #top関数を書き換え

def snippet_new(request):
  return HttpResponse('スニペットの登録')

def snippet_edit(request, snippet_id):
  return HttpResponse('スニペットの編集')

def snippet_detail(request, snippet_id):
  snippet = get_object_or_404(Snippet, pk=snippet_id)
  return render(request, 'snippets/snippet_detail.html',
                  {'snippet': snippet})