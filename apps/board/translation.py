"""
게시판 국제화 지원 모듈.

`django-modeltranslation` 을 이용하여 다국어 지원을 하는 모듈입니다.
"""

from modeltranslation.translator import TranslationOptions, register

from .models import BasePost, Board, Comment, Post, Tag


@register(Board)
class BoardTranslationOptions(TranslationOptions):
    """
    :class:`Board` 모델에 대한 국제화 지원.
    """

    fields = ()


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    """
    :class:`Tag` 모델에 대한 국제화 지원.
    """

    fields = ('name', 'abbr')


@register(BasePost)
class BasePostTranslationOptions(TranslationOptions):
    """
    :class:`BasePost` 모델에 대한 국제화 지원.
    """

    fields = ('content',)


@register(Post)
class PostTranslationOptions(TranslationOptions):
    """
    :class:`Post` 모델에 대한 국제화 지원.
    """

    fields = ('title',)


@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    """
    :class:`Comment` 모델에 대한 국제화 지원.
    """

    fields = ()
