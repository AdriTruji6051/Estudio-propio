def beautifullBynary(arr,perfNumb):
    if arr[0] > 0:
        if arr[0] > arr[2]: 
            arr[0] -=arr[2]
            perfNumb += arr[2]
        else: 
            perfNumb += arr[0]
            arr[0] -= arr[0]

        if arr[1] > 0:
            if arr[1] > arr[3]:
                arr[1] -= arr[3]
                perfNumb += arr[2]
            else:
                perfNumb += arr[1]
                arr[1] -= arr[1]
        else:
            print("Ultimo fue(ron) 0's Respuesta:")
            return perfNumb
        return beautifullBynary(arr,perfNumb)   
    else:
        print("Ultimo fue(ron) 1's Respuesta:")
        return perfNumb

print("Introduce los valores:")
arr = map(int, input().split())
arr = list(arr)
if arr[2] <= 0 and arr[3] <= 0:
    print("-1")
else:
    print(beautifullBynary(arr,0))