from django.http import JsonResponse

from .models import User


def getUser(request):
    username = request.COOKIES.get("username", None)
    try:
        if username is None:
            raise ValueError("No username provided")

        else:
            user = User.objects.get(username=username)
            return JsonResponse({"username": user.username})

    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=404)

    except User.DoesNotExist:
        user = User.objects.create(username=username)
        return JsonResponse({"username": user.username})
