from django.utils import translation

class LanguageQueryMiddleware:
    """
    URL query ?lang=uz|ru|en bo'lsa shu tilni faollashtiradi.
    LocaleMiddleware'dan KEYIN turishi kerak (settings.py da shunday).
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lang = request.GET.get("lang")
        if lang in {"uz", "ru", "en"}:
            translation.activate(lang)
            request.LANGUAGE_CODE = lang
        response = self.get_response(request)
        translation.deactivate()
        return response
