### Red Black Tree
- Guaranteed height `O(log n)`
- Nodes are colored either red or black
- Root and leaves(NULL) are black
- If node is red its children are black
- All paths from a node to its NULL descendants contain the same number of black nodes
- Search/Delete/Insert complexity is `O(log n)`

#### Rotation
- Time complexity `O(1)`
- Alter the structure of a tree by re-arranging subtrees
- Goal is to decrease the height of tree
  - Red Black Tree's: maximum height `O(log n)`
  - Largest subtree up, smaller subtrees down
- Rotation does not affect the order of elements

- __Left Rotation__
  - Node which we are going to rotate lets say is Z
  - y = Z.right
  - y.parent = Z.parent, if y.left is not NULL
  - Set y.parent = Z.parent
  - Z.parent = y (Right child becomes parent)
  - Z.right = y.left (Left child of `y` becomes new right child of `Z`)
  - If parent of `Z` is NULL make `y` as `root`
  - If `Z` is left child of `Z.parent`, make `y` as left child of `Z.parent`
  - Else assign `y` as right child of `Z.parent`

- __Right Rotation__
  - Node which we are going to rotate lets say is Z
  - y = Z.left
  - y.parent = Z.parent, if y.right is not NULL
  - Z.parent = y (Left Child becomes parent)
  - Z.left = y.right (Right child of `y` becomes new left child of `Z`)
  - If parent of `Z` is NULL make `y` as `root`
  - If `Z` is right child of `Z.parent`, make `y` as right child of `Z.parent`
  - Else assign `y` as left child of `Z.parent`

#### Insertion
- Insert new node as red node
- Recolor and Rotate the tree to fix the violation
- 4 Possible scenarios(z is the node which we are going to insert)
  - Z = root -> (Color Black)
  - Z.uncle(Z.grandparent.other child than the z's parent) = red -> recolor(Z's parent, grandparent and uncle)
  - Z.uncle = black(triangle, meaning if Z is left child of its parent and Z's uncle is left child of Z's grandparent OR if Z is right child of its parent and Z's uncle is right child of Z's grandparent) -> rotate Z.parent
  - Z.uncle = black(line, meaning if Z is left child of its parent and Z's uncle is right child of Z's grandparent OR if Z is right child of its parent and Z's uncle is left child of Z's grandparent) -> rotate Z.grandparent and recolor

    ```psudo code
    function insert(T, z):
      y = T.null
      x = T.null
      
      while x != T.null
        y = x
        if z.data < x.data:
          x = x.left
        else:
          x = x.right
      
      z.p = y
      
      if y == T.null:
        T.root = z
      elseif z.data < y.data:
        y.left = z
      else:
        y.right = z


    function insert_fixup(T, z):
      while z.parent.color == RED:

        if z.parent == z.parent.parent.left:
          y = z.parent.parent.right
          if y.color == RED:
            z.parent.color = BLACK       # Case 1
            y.color = BLACK              # Case 1
            z.parent.parent = RED        # Case 1
            z = z.parent.parent
          else:
            if z == z.parent.right:
              z = z.parent                   # Case 2
              LEFT-ROTATE(T, z)              # Case 2
            z.parent.color = BLACK           # Case 3
            z.parent.parent.color = RED      # Case 3 
            RIGHT-ROTATE(T, z.parent.parent) # Case 3

        else if z.parent == z.parent.parent.right:
          y = z.parent.parent.left
          if y.color == RED:
            z.parent.color = BLACK       # Case 1
            y.color = BLACK              # Case 1
            z.parent.parent = RED        # Case 1
            z = z.parent.left
          else
            if z == z.parent.left:
              z = z.parent                   # Case 2
              RIGHT-ROTATE(T, z)             # Case 2
            z.parent.color = BLACK           # Case 3
            z.parent.parent.color = RED      # Case 3 
            LEFT-ROTATE(T, z.parent.parent)  # Case 3

      T.root.color = BLACK


    z = newNode(data=data)
    z.left = T.null
    z.right = T.null
    z.color = RED
    insert_fixup(T, z)
    ```
#### Delete
- Save the color of nodeToBeDeleted in origrinalColor.
- If the left child of nodeToBeDeleted is NULL
  - Assign the right child of nodeToBeDeleted to x.
  - Transplant nodeToBeDeleted with x.
- Else if the right child of nodeToBeDeleted is NULL
  - Assign the left child of nodeToBeDeleted into x.
  - Transplant nodeToBeDeleted with x.
- Else
  - Assign the minimum of right subtree of noteToBeDeleted into y.
  - Save the color of y in originalColor.
  - Assign the rightChild of y into x.
  - If y is a child of nodeToBeDeleted, then set the parent of x as y.
  - Else, transplant y with rightChild of y.
  - Transplant nodeToBeDeleted with y.
  - Set the color of y with originalColor.
- If the originalColor is BLACK, call DeleteFix(x).
