from django.shortcuts import render, redirect, get_object_or_404
from .forms import BehindForm, CommentForm
from .models import Behind, Comment
from django.http import JsonResponse
import json


## 아래부터 behind
def index(request):
    behinds = Behind.objects.all()
    context = {
        'behinds': behinds,
    }
    return render(request, 'behinds/index.html', context)

# 생성 폼과 생성 페이지
def create(request):
    # 로그인 한 사용자 중에 권한이 있는 사용자(감독)
    if request.user.is_authenticated and request.user.behind_auth:
        if request.method == "POST":
            title = request.POST.get('title')
            content = request.POST.get('content')
            csrfmiddlewaretoken = request.POST.get('csrfmiddlewaretoken')
            behind_values = {
                'title': title,
                'content': content,
                'csrfmiddlewaretoken': csrfmiddlewaretoken
            }
            form = BehindForm(behind_values)
            if form.is_valid():
                behind = form.save(commit=False)
                behind.user = request.user
                behind.save()
                return redirect('behinds:index')
            return render(request, 'behinds/create.html')
        else:
            return render(request, 'behinds/create.html')
    # 로그인을 했지만 권한이 없는 사용자
    elif request.user.is_authenticated :
        return redirect('behinds:index')
    # 로그인도 안했고 권한도 없는 사용자
    else:
        return redirect('http://127.0.0.1:8000/')

# 디테일 페이지
def detail(request, behind_pk):
    if request.user.is_authenticated:
        behind = Behind.objects.get(pk=behind_pk)
        form = CommentForm()
        comments = behind.comment_set.all()
        context = {
            'behind': behind,
            'form': form,
            'comments': comments
        }
        return render(request, 'behinds/detail.html', context)
    else:
        return redirect('http://127.0.0.1:8000/')

# 삭제
def delete(request, behind_pk):
    behind = Behind.objects.get(pk=behind_pk)
    if request.user == behind.user:
        behind.delete()
        return redirect('behinds:index')
    else:
        return redirect('behinds:detail', behind.pk)

# behind 수정
def update(request, behind_pk):
    behind = get_object_or_404(Behind, pk=behind_pk)
    if request.user == behind.user:
        if request.method == 'POST':
            form = BehindForm(request.POST, instance=behind)
            if form.is_valid():
                form.save()
                return redirect('behinds:detail', behind_pk)
        else:
            form = BehindForm(instance=behind)
    else:
        return redirect('behinds:detail', behind_pk)
    form = BehindForm(instance=behind)
    context = {
        'behind': behind,
        'form': form
    }
    return render(request, 'behinds/update.html', context)

## 아래부터 comment
# comment 생성
def comment_create(request, behind_pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        behind = Behind.objects.get(pk=behind_pk)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.behind = behind
            comment.user_comment = request.user
            form.save()
            return redirect('behinds:detail', behind.pk)
    else:
        form = CommentForm()
        context = {
            'form': form
        }
        return redirect('behinds:detail', behind_pk, context)
    return redirect('behinds:detail', behind_pk)

# comment 수정
def comment_update(request, behind_pk, comment_pk):
    
    if request.method == "POST":
        jsonObject = json.loads(request.body)
        comment = get_object_or_404 (Comment,pk=jsonObject.get('commentId'))
        behind = get_object_or_404 (Behind,pk=jsonObject.get('behindId'))
        if request.user == comment.user_comment:
            content = jsonObject.get('content')
            csrfmiddlewaretoken = jsonObject.get('csrftoken')
            comment_values = {
                'content': content,
                'csrfmiddlewaretoken': csrfmiddlewaretoken
            }
            form = CommentForm(comment_values, instance=comment)
            if form.is_valid():
                editComment = form.save(commit=False)
                editComment.behind = behind
                editComment.user_comment = request.user
                editComment.save()
                context = {
                    'editedContent': editComment.content
                }
                return JsonResponse(context)
        return redirect('behinds:detail', behind_pk)
    else : 
        return redirect('behinds:detail', behind_pk)    

# comment 삭제
def comment_delete(request, behind_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user_comment:
        comment.delete()
        return redirect('behinds:detail', behind_pk)
    else:
        return redirect('behinds:detail', behind_pk)

# likes
def likes(request, behind_pk):
    behind = Behind.objects.get(pk=behind_pk)
    if request.user.is_authenticated:
        if request.user != behind.user :
            if behind.like_user.filter(pk=request.user.pk).exists():
                behind.like_user.remove(request.user)
                isLiked = False
            else:
                behind.like_user.add(request.user)
                isLiked = True
        context = {
            'isLiked': isLiked,
            'like_user_count': behind.like_user.count(),
        }
        return JsonResponse(context)
    return redirect('accounts:login')