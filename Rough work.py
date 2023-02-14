
    #
    # intcountTreesRec(int numKeys) {
    #     if (numKeys <=1) {
    #         return(1);
    #     }
    #     else {
    #         int sum = 0;
    #         int left, right, root;
    #         for (root=1; root<=numKeys; root++) {
    #             left = countTreesRec(root - 1);
    #             right = countTreesRec(numKeys - root);
    #             sum += left*right;
    #         }
    #         return(sum);
    #     }
    # }

hmap = {}
hmap.__setitem__()
