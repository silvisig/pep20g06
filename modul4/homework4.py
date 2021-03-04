def function_min(x):
    for i in range(-10, 10):
        minim = min(x ** 2 - 2 * x + 2, 2 * (x ** 2) - 4 * x + 4, 3 * (x ** 2) - 6 * x + 6)
        return minim
function_min(0)

def build(a, b, c):
    def response(x=0):
        return a * (x ** 2) + b * x + c

    return response
build(1, 2, 3)




def build(a, b, c):
    def response(x):
        return a * (x ** 2) + b * x + c
        print(response(1))
    list_of_functions = []

    list_of_functions.append(response(1))
    return list_of_functions


list_of_functions = []
for a, b, c in ((1, -2, 2), (2, -4, 4), (3, -6, 6)):
    responses = (build(a, b, c))
    list_of_functions.append(responses)

dict_of_results = {}
for function in list_of_functions:
        dict_of_results[function] = function(0)


print("Dict of results is: ", dict_of_results)

function_with_smallest_result = None
smallest_value = None
for function, values in dict_of_results.items():
    if smallest_value is None or smallest_value > values:
        function_with_smallest_result = function
        smallest_value = values
print(function_with_smallest_result(0))
