from dj_static import Cling

class SLCling(Cling):
    def __call__(self, environ, start_response):
        def patched_start_response(status, headers, exc_info=None):
            print headers
            return start_response(status, [(str(k), str(v)) for k,v in headers], exc_info)
        return super(SLCling, self).__call__(environ, patched_start_response)
