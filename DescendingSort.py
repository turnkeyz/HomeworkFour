#Kyler Telge 1825829#
# TODO: Write a selection_sort_descend_trace() function that
#       sorts the numbers list into descending order
def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        max_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[max_index] < numbers[j]:
                max_index = j
        temp = numbers[i]
        numbers[i] = numbers[max_index]
        numbers[max_index] = temp
        for num in range(len(numbers)):
            print(numbers[num], end=' ')
        print()


if __name__ == "__main__":
    # TODO: Read in a list of integers into numbers, then call
    #       selection_sort_descend_trace() to sort the numbers
    input_string = input()
    numbers = input_string.split()
    selection_sort_descend_trace(numbers)
