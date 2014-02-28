class OwnerMiddleware(object):
    def process_view(self, request, view_func, args, kwargs):
        request.owner = False

        owner_id = kwargs.get('owner_id', None)

        if owner_id is not None and int(owner_id) == request.user.pk:
            request.owner = True

        return None


class LastVisitedMiddleware(object):
    def process_request(self, request):
        request_path = request.get_full_path()
        try:
            request.session['last_visited'] = request.session['currently_visiting']
        except KeyError:
            pass

        request.session['currently_visiting'] = request_path
