class OwnerMiddleware(object):
    def process_view(self, request, view_func, args, kwargs):
        request.owner = False

        owner_id = kwargs.get('owner_id', None)

        if owner_id is not None and int(owner_id) == request.user.pk:
            request.owner = True

        return None
