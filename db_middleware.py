# from django.db.models.signals import class_prepared, post_init

class PrefixMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # def add_db_prefix(sender, **kwargs):
        #     if prefix and not sender._meta.db_table.startswith(prefix):
        #         sender._meta.db_table = prefix + sender._meta.db_table

        # post_init.connect(add_db_prefix)
        # class_prepared.connect(add_db_prefix)
        response = self.get_response(request)
        return response