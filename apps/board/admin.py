"""
게시판 어드민 페이지 설정.
"""

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import AttachedFile, Board, Comment, Post, Tag


class BoardAdmin(TranslationAdmin):
    """
    :class:`Board` 모델에 대한 커스텀 어드민.

    `django-modeltranslation` 에서 제공하는 :class:TranslationAdmin` 을 상속받아
    다국어 처리를 사용자 친화적으로 변경하였습니다.
    """

    pass


class TagAdmin(TranslationAdmin):
    """
    :class:`Tag` 모델에 대한 커스텀 어드민.

    `django-modeltranslation` 에서 제공하는 :class:TranslationAdmin` 을 상속받아
    다국어 처리를 사용자 친화적으로 변경하였습니다.
    """

    pass


class PostAdmin(TranslationAdmin):
    """
    :class:`Post` 모델에 대한 커스텀 어드민.

    `django-modeltranslation` 에서 제공하는 :class:TranslationAdmin` 을 상속받아
    다국어 처리를 사용자 친화적으로 변경하였습니다.
    """

    pass


class CommentAdmin(TranslationAdmin):
    """
    :class:`Comment` 모델에 대한 커스텀 어드민.

    `django-modeltranslation` 에서 제공하는 :class:TranslationAdmin` 을 상속받아
    다국어 처리를 사용자 친화적으로 변경하였습니다.
    """

    pass


admin.site.register(Board, BoardAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(AttachedFile)
