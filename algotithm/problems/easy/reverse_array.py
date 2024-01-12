def reverse(arr):
        """
        
        Basicamente, trocando os nos indexes.
        O primeiro valor vai ser o ultimo,
        o ultimo vai ser o primeiro.



        """
    start = 0
    end = len(arr) - 1

    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

    return arr
    


example = [1,2,3,4,5]

assert reverse(example) == [5,4,3,2,1], reverse(example)
