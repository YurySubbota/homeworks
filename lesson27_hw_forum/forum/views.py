from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from .forum_forms import CommentForm
from forum.models import Room, Comment
from copy import deepcopy


# Create your views here.

class RoomsListView(View):
    def get(self, request, *args, **kwargs):
        title = 'Rooms List'
        sort_by = request.GET.get('sort', 'created_at')
        order_by = request.GET.get('order', 'desc')
        sort_by = sort_by if order_by == 'asc' else f'-{sort_by}'
        rooms = Room.objects.order_by(sort_by)
        return render(request, 'rooms_list.html', {'rooms_list': rooms, 'title': title})


class RoomView(View):
    def get(self, request, pk, *args, **kwargs):
        room = Room.objects.get(pk=pk)
        title = room.title
        comments = Comment.objects.filter(room__pk=pk).order_by('created_at')
        id_ = 12

        comments = comment_list(pk)
        return render(request, 'room.html',
                      {'id_': id_, 'comments': comments, 'room': room,
                       'title': title})


class NewCommentView(View):
    def get(self, request, pk, *args, **kwargs):
        print(request.POST)
        room = Room.objects.get(pk=pk)
        title = 'New Comment'
        form = CommentForm()
        '''#form = CommentForm(request.GET)
        if form.is_valid():
            comment = form(commit=False)
            comment.room = room.id
            comment.comment_id
            comment.save()'''
        return render(request, 'new_comment.html', {'form': form, 'room': room, 'title': title})

    def post(self, request, pk, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            comment = Comment()
            comment.nickname = form.cleaned_data['nickname']
            comment.content = form.cleaned_data['content']
            comment.room = Room.objects.get(pk=pk)
            comment.save()

            return redirect(f'room', pk)
        return render(request, 'new_comment.html', {'form': form})


class NewCommentForCommentView(View):
    def get(self, request, pk, *args, **kwargs):
        print(request.POST)
        comment = Comment.objects.get(pk=pk)
        title = 'New Comment'
        form = CommentForm()
        '''#form = CommentForm(request.GET)
        if form.is_valid():
            comment = form(commit=False)
            comment.room = room.id
            comment.comment_id
            comment.save()'''
        return render(request, 'new_comment_for_comment.html', {'form': form, 'room': comment, 'title': title})

    def post(self, request, pk, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            comment = Comment()
            comment.nickname = form.cleaned_data['nickname']
            comment.content = form.cleaned_data['content']
            comment.room = (Comment.objects.get(pk=pk)).room
            comment.comment_id = Comment.objects.get(pk=pk)
            comment.save()
            return redirect(f'room', comment.room.pk)
        return render(request, 'new_comment_for_comment.html', {'form': form})


def comment_list(room_id):
    comment = {}
    comments_list = []
    sorted_comments = []
    comments_queryset = Comment.objects.filter(room=room_id).order_by('created_at')
    for comment_obj in comments_queryset:
        comment['pk'] = comment_obj.id
        comment['room'] = comment_obj.room.pk
        comment['nickname'] = comment_obj.nickname
        comment['content'] = comment_obj.content
        comment['likes'] = comment_obj.likes
        comment['dislikes'] = comment_obj.dislikes
        try:
            comment['comment_id'] = comment_obj.comment_id.id
        except AttributeError:
            comment['comment_id'] = None
        comment['indent'] = 25
        comments_list.append(deepcopy(comment))
    while comments_list:
        found = 0
        if not sorted_comments:
            sorted_comments.append(comments_list.pop(0))
            print("one ", sorted_comments)
            continue
        elif comments_list:
            for comment in comments_list:
                for element in sorted_comments:
                    if element['pk'] == comment['comment_id']:
                        sorted_comments.append(comments_list.pop(comments_list.index(comment)))
                        sorted_comments[-1]['indent'] += element['indent']
                        print("three ", sorted_comments)
            for comment in comments_list:
                print(comment['pk'], "comment['comment_id']", comment['comment_id'])
                print('last com in sorted', sorted_comments[-1]['pk'])
                if comment['comment_id'] == sorted_comments[-1]['pk']:
                    sorted_comments.append(comments_list.pop(comments_list.index(comment)))
                    sorted_comments[-1]['indent'] += sorted_comments[-2]['indent']
                    print("two ", sorted_comments)
                    break

            if comments_list:
                for comment in comments_list:
                    for element in sorted_comments:
                        if comment['comment_id'] == element['pk']:
                            found += 1
            if comments_list and found == 0:
                sorted_comments.append(comments_list.pop(0))

    return sorted_comments


'''def comment_list1(room_id):
    comments_queryset = Comment.objects.filter(room=room_id).order_by('created_at')
    sorted_comments = []
    comments_indent = {}
    while comments_queryset:
        if not sorted_comments:
            sorted_comments.append(comments_queryset.first())
            comments_queryset = comments_queryset.exclude(id=sorted_comments[-1].id)
            comments_indent[sorted_comments[-1].id] = 25
            print('first comment: ', sorted_comments[-1].id)

        if comments_queryset.filter(comment_id=sorted_comments[-1].pk):
            sorted_comments.append(comments_queryset.filter(comment_id=sorted_comments[-1].pk).first())
            comments_queryset = comments_queryset.exclude(id=sorted_comments[-1].pk)
            print('filtred comment: ', sorted_comments[-1].id)

            comments_indent[sorted_comments[-1].pk] = comments_indent[sorted_comments[-2].pk] + 25
        elif comments_queryset:
            sorted_comments.append(comments_queryset.first())
            comments_queryset = comments_queryset.exclude(id=sorted_comments[-1].id)
            comments_indent[sorted_comments[-1].id] = 25
    return sorted_comments'''

'''    
    comments_queryset = Comment.objects.filter(room=room_id).order_by('created_at')

    # for comment in comments_queryset:
    # comments_list.append(comment)
    while comments_queryset:

        if not sorted_comments:
            comment = comments_queryset.get(created_at=max(comments_queryset.values_list('created_at')))
            sorted_comments.append(comment)
            comments_indent = {comment.pk: 25}
            comments_queryset.delete(comment)
    print(sorted_comments)'''

'''
def comments_list(request, room_id):
    room = Room.objects.get(pk=room_id)
    comments_queryset = Comment.objects.filter(room=room_id).order_by('created_at')
    comments_list = []
    sorted_comments = []
    comments_indent = {}
    #for comment in comments_queryset:
        #comments_list.append(comment)
    while comments_queryset:
        comment = comments_queryset.get(created_at=max(comments_queryset.values_list('created_at')))



    while comments_list:
        if not sorted_comments:
            comments_indent = {comments_list[-1].pk: 25}
            sorted_comments.append(comments_list.pop())
        comments_list.objects.get(comment_id=comments_list[-1].pk)
        if sorted_comments[-1].pk in comments_list[-1 - ]
            comments_indent = {comment.pk: }

        for sorted_comments[-1].pk in comments_list

        if comment.comment_id not in sorted_comments and comment.comment_id is None:
            comments_indent.append({comment.pk: 25})
            sorted_comments.append(comments_list.pop(comment))





'''

'''def comments_list(comments):
    new_comments = []
    comments_for_comment =[]
    indent = {}
    for comment in comments:
        if comment.comment_id:
            comments_for_comment.append(comment)
        else:
            new_comments.append(comment)
        com = comments.filter(comment_id=comment.id)
    for element in comments_for_comment:
        for comment in new_comments:
            print(comment.id, comment.comment_id)'''

'''
def sort_comments(*args):
    sorted_comments = []
    comments_list, comments_for_comment_list = args
    while comments_list or comments_for_comment_list:
        found = 0
        if not sorted_comments:
            sorted_comments.append(comments_list[0])
            continue
        if comments_for_comment_list:
            for comment in comments_for_comment_list:
                for element in sorted_comments:
                    if element['pk'] == comment['comment_id']:
                        sorted_comments.append(comments_for_comment_list.pop(comments_for_comment_list.index(comment)))
            for comment in comments_for_comment_list:
                if comment['comment_id'] == sorted_comments[-1]['pk']:
                    sorted_comments.append(comments_for_comment_list.pop(comments_for_comment_list.index(comment)))
        if comments_list:
            for comment in comments_for_comment_list:
                for element in sorted_comments:
                    if comment['comment_id'] == element['pk']:
                        found += 1
        if comments_list and found == 0:
            sorted_comments.append(comments_list.pop(0))
    return sorted_comments




def comment_list3(room_id):
    comment = {}
    comments_list = []
    comments_for_comment_list = []
    comments_queryset = Comment.objects.filter(room=room_id).order_by('created_at')
    for comment_obj in comments_queryset:
        comment['pk'] = comment_obj.id
        comment['room'] = comment_obj.room.pk
        comment['nickname'] = comment_obj.nickname
        comment['content'] = comment_obj.content
        comment['likes'] = comment_obj.likes
        comment['dislikes'] = comment_obj.dislikes
        try:
            comment['comment_id'] = comment_obj.comment_id.id
        except AttributeError:
            comment['comment_id'] = None
        comment['indent'] = 25
        if comment['comment_id']:
            comments_for_comment_list.append(deepcopy(comment))
        else:
            comments_list.append(deepcopy(comment))
        return sort_comments(comments_list, comments_for_comment_list)

'''
