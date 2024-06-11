# time complexity of O(N) since it loop through N one time.

def re_superman(n, k, arr):
    # stack represent list of chicken that are under roof (right now are first chicken)
    stack = [arr[0]]
    # mx represent max number of chickends under roof (right now is 1)
    mx = 1
    # loop from second to last chicken
    for i in range(1,n):
        # if current chick are under roof then add it in stack
        if (stack[0] +k) -1 >= arr[i]:
            stack.append(arr[i])
        # if not
        else:
            # first update mx if it more than current 
            mx = max(mx, len(stack))
            # loop and popout first chicken until it pass atleast one condition
            # allow current chicken to share the same roof 
            # there is no chicken under roof
            while stack != []:
                if (stack[0] +k) -1 >= arr[i]:
                    break
                stack = stack[1:]
            # add current chicken to the stack
            stack.append(arr[i])
    # update mx again
    mx = max(mx, len(stack))

    return mx
            
# TEST           
# print(re_superman(5, 5, [2, 5, 10, 12, 15]))
# print(re_superman(6, 10, [1, 11, 30, 34, 35, 37]))
# print(re_superman(8, 10, [1, 11, 30, 34, 35, 37, 37, 37]))


first_input = input()
second_input = input()

n,k = first_input.split(" ")
arr = second_input.split(" ")
print(re_superman(int(n), int(k), [int(x) for x in arr]))
