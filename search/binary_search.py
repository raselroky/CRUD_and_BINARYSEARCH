def binary_search(sorted_queryset, target_value):
    low = 0
    high = sorted_queryset.count() - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = sorted_queryset[mid].email
        if mid_value == target_value:
            return sorted_queryset[mid] 
        elif mid_value < target_value:
            low = mid + 1
        elif mid_value > target_value:
            high = mid - 1
    return None

