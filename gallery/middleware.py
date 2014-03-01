import os


class OwnerMiddleware(object):
    def process_view(self, request, view_func, args, kwargs):
        request.owner = False

        owner_id = kwargs.get('owner_id', None)

        if owner_id is not None and int(owner_id) == request.user.pk:
            request.owner = True

        return None


class ParentUrlMiddleware(object):
    def process_request(self, request):
        request_path = request.get_full_path()
        parent_path = os.path.abspath(os.path.join(request_path, os.pardir))
        request.parent_path = parent_path

        return None
