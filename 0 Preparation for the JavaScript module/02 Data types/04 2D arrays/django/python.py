from django.shortcuts import render

def arrays(request):
    arrayOfNumbers = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    mixedArray = [
        ["Maria", "John", "Peter"],
        [1, 2, 3, 4, 5, 6]
    ]

    context = {
        "second_element": arrayOfNumbers[0][1],
        "second_row": arrayOfNumbers[1],
        "third_row_length": len(arrayOfNumbers[2]),
        "third_name": mixedArray[0][2],
        "fifth_number": mixedArray[1][4],
        "second_row_length": len(mixedArray[1]),
    }

    return render(request, "arrays.html", context)