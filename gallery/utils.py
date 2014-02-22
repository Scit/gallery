import os


def get_upload_path(instance, filename):
    #return u'photos/%s_%s/%s' % (instance.gallery.owner.username,
            #instance.gallery.title, filename)
    return os.path.join('photos', 
                        '%s_%s' % (instance.gallery.owner.username,
                                   instance.gallery.title),
                        filename)
