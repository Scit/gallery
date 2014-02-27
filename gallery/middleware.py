class OwnerMiddleware(object):
    def process_request(self, request):
        #request.owner = False

        #user_path = request.path.split('/')[1]
        #if user_path.isdigit() and \
                #int(user_path) == request.user.pk:
            #request.owner = True

        return None

    def process_view(self, request, view_func, args, kwargs):
        request.owner = False

        owner_id = kwargs.get('owner_id', None)

        if int(owner_id) == request.user.pk:
            request.owner = True

        return None
