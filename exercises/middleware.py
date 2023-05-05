class AddUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and hasattr(request.user, "author"):
            request.author = request.user.author
            print(request.author)

        response = self.get_response(request)
        return response


# user = request.user

# user.author = author
# author.save()

# # access author
# user.author
