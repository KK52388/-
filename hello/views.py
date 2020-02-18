from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm

# Create your views here.
#ログ出し用
from logging import getLogger


#ログ出し用
logger = getLogger(__name__)

#ログ出し用
# def index(request):
#     logger.debug("デバッグ")
#     logger.info("インフォ")
#     logger.warning("ワーニング")
#     logger.error("エラー")
#     logger.critical("クリティカル")
#     return HttpResponse("日本一平凡なDjango")

class HelloView(TemplateView):
    try: 
        
        def __init__(self):
            self.params = {
                    'title': 'Hello',
                    'message': 'your data:',
                    'form': HelloForm()
                }
        
        def get(self, request):
            return render(request, 'hello/index.html', self.params)
    
        def post(self, request):
            
            msg = 'あなたは、<b>' + request.POST['name'] + \
                '（' + request.POST['age'] + \
                '）</b>さんです。<br>メールアドレスは <b>' + request.POST['mail'] + \
                '</b> ですね。'
            self.params['message'] = msg
            self.params['form'] = HelloForm(request.POST)
            return render(request, 'hello/index.html', self.params)
    except Exception as e:
        print(e)
        logger.debug(e)
        logger.debug("デバッグ")
        logger.info("インフォ")
        logger.warning("ワーニング")
        logger.error("エラー")
        logger.critical("クリティカル")


# def index(request):
#     params = {
#         'title':'Hello',
#         'message':'your data:',
#         'goto':'next',
#         'form': HelloForm()
#         }
#     if (request.method == 'POST'):
#         params['message'] = '名前：' + request.POST['name'] + \
#             '<br>メール：' + request.POST['mail'] + \
#             '<br>年齢：' + request.POST['age']
#         params['form'] = HelloForm(request.POST)
#     return render(request, 'hello/index.html', params)

# def next(request):
#     params = {
#         'title':'Hello/Index',
#         'msg':'これは、サンプルで作ったページです。',
#         'goto':'index',
#         }
#     return render(request, 'hello/index.html', params)

# def form(request):
#     msg = request.POST['msg']
#     params = {
#         'title':'Hello/Form',
#         'msg':'こんにちは、' + msg + 'さん。',
#         'goto':'index',
#         }
#     return render(request, 'hello/index.html', params)
"""
def index(request, id, nickname):
    #if 'msg' in request.GET:
        #msg = request.GET['msg']
    result = 'your id: '+ str(id) + ', name: "' \
            + nickname + '".'
        #result = 'you typed: "' + msg +'".'
    #else:
     #   result = 'please send msg parameter!'
        
    return HttpResponse(result)
"""
    