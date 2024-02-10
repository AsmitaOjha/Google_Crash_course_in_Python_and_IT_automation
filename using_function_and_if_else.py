def translate_error_code(error_code):
    if error_code =='401 unauthorized':
        translation ="server received an unauthenticated request"
    elif error_code =="404 Not Found":
        translation ="Requested web page not found on server"
    elif error_code =="408 request timeout":
        translation= "Server request to close unused connection"
    else:
        translation = 'Unknown error code'
    
    return translation

print(translate_error_code("404 Not Found"))
print(translate_error_code("401 unauthorized"))