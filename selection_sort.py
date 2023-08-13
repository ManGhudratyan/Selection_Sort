def selectionSort(ml):
    newl = [];
    while ml:
        maxValue = max(ml);
        newl.append(maxValue);
        ml.remove(maxValue);
    return newl;

ml = [10, 5, 2, 6, 8, 3, 1, 7, 4, 9];
sorted_list = selectionSort(ml);
print('Sorted list =>', sorted_list);
