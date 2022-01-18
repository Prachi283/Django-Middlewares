#  Function Based Midleware
#  if there is any middleware after this My_middleware , then control goes to that middleware otherwise,
# control goes to view 
def my_middleware(get_response):
	print("One time initialization")

	def func(request):
		print(" Before View (Function-Based Middleware.")
		response= get_response(request)   
		print("after view")
		return response
	return func


# Class - Based Middleware


class Mymiddleware:
	def __init__(self,get_response):
		self.get_response= get_response
		print("One time initialization")

	def __call__(self,request):
		print("This is before view ( Class-Based Middleware.)")
		response=self.get_response(request)
		print("This is after view ")
		return response