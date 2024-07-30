""" AVL Tree implemented on top of the standard BST. """

__author__ = 'Alexey Ignatiev'
__docformat__ = 'reStructuredText'

from bst import BinarySearchTree
from typing import TypeVar, Generic
from node import AVLTreeNode

K = TypeVar('K')
I = TypeVar('I')


class AVLTree(BinarySearchTree, Generic[K, I]):
    """ Self-balancing binary search tree using rebalancing by sub-tree
        rotations of Adelson-Velsky and Landis (AVL).
    """

    def __init__(self) -> None:
        """
            Initialises an empty Binary Search Tree
            :complexity: O(1)
        """

        BinarySearchTree.__init__(self)

        self.kth = None

    def get_height(self, current: AVLTreeNode) -> int:
        """
            Get the height of a node. Return current.height if current is 
            not None. Otherwise, return 0.
            :complexity: O(1)
        """

        if current is not None:
            return current.height
        return 0

    def get_balance(self, current: AVLTreeNode) -> int:
        """
            Compute the balance factor for the current sub-tree as the value
            (right.height - left.height). If current is None, return 0.
            :complexity: O(1)
        """

        if current is None:
            return 0
        return self.get_height(current.right) - self.get_height(current.left)

    def insert_aux(self, current: AVLTreeNode, key: K, item: I) -> AVLTreeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert
            it. After insertion, performs sub-tree rotation whenever it becomes
            unbalanced.
            returns the new root of the subtree.
        """

        if current is None:  # base case: at the leaf
            current = AVLTreeNode(key, item) #Perform normal Binary Seacrch
            self.length += 1 #Update length
        elif key < current.key:
            current.left = self.insert_aux(current.left, key, item)
        elif key > current.key:
            current.right = self.insert_aux(current.right, key, item)
        else:  #If the key is equal to the current key raise Error since it is a duplicate
            raise ValueError('Inserting duplicate item')

        #Update the height of the root node
        current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))

        #Find balance factor and rebalance
        return self.rebalance(current)

    def delete_aux(self, current: AVLTreeNode, key: K) -> AVLTreeNode:
        """
            Attempts to delete an item from the tree, it uses the Key to
            determine the node to delete. After deletion,
            performs sub-tree rotation whenever it becomes unbalanced.
            returns the new root of the subtree.
        """

        if current is None:  # key not found
            raise ValueError('Deleting non-existent item')
        elif key < current.key:
            current.left = self.delete_aux(current.left, key)
        elif key > current.key:
            current.right = self.delete_aux(current.right, key)
        else:  #Found key and perform deletion
            #If the node that is to be deleted has one child replace that
            #node with the child and remove the child using a temp variable
            if current is not None:
                if current.left is None:
                    temp = current.right
                    return temp
                elif current.right is None:
                    temp = current.left
                    return temp
                #If the node that is to be deleted had two children, find
                #minimal and replace that node with the node to be deleted,
                #removing the minimal node
                temp = self.get_minimal(current.right)
                current.key = temp.key
                current.right = self.delete_aux(current.right, temp.key)
        #Update height
        current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))
        #Find balance factor and balance
        return self.rebalance(current)

    def left_rotate(self, current: AVLTreeNode) -> AVLTreeNode:
        """
            Perform left rotation of the sub-tree.
            Right child of the current node, i.e. of the root of the target
            sub-tree, should become the new root of the sub-tree.
            returns the new root of the subtree.
            Example:

                 current                                       child
                /       \                                      /   \
            l-tree     child           -------->        current     r-tree
                      /     \                           /     \
                 center     r-tree                 l-tree     center

            :complexity: O(1)
        """

        child = current.right
        center = child.left

        #Rotate the nodes
        child.left = current
        current.right = center

        #Update heights of the current node and child node
        current.height = 1 + max(self.get_height(current.left),
                           self.get_height(current.right))
        child.height = 1 + max(self.get_height(child.left),
                           self.get_height(child.right))


        return child

    def right_rotate(self, current: AVLTreeNode) -> AVLTreeNode:
        """
            Perform right rotation of the sub-tree.
            Left child of the current node, i.e. of the root of the target
            sub-tree, should become the new root of the sub-tree.
            returns the new root of the subtree.
            Example:

                       current                                child
                      /       \                              /     \
                  child       r-tree     --------->     l-tree     current
                 /     \                                           /     \
            l-tree     center                                 center     r-tree

            :complexity: O(1)
        """

        child = current.left
        center = child.right

        #Rotate the child node and current node
        child.right = current
        current.left = center

        #Update heights for the current and child node
        current.height = 1 + max(self.get_height(current.left),
                           self.get_height(current.right))
        child.height = 1 + max(self.get_height(child.left),
                           self.get_height(child.right))


        return child

    def rebalance(self, current: AVLTreeNode) -> AVLTreeNode:
        """ Compute the balance of the current node.
            Do rebalancing of the sub-tree of this node if necessary.
            Rebalancing should be done either by:
            - one left rotate
            - one right rotate
            - a combination of left + right rotate
            - a combination of right + left rotate
            returns the new root of the subtree.
        """
        if self.get_balance(current) >= 2:
            child = current.right
            if self.get_height(child.left) > self.get_height(child.right):
                current.right = self.right_rotate(child)
            return self.left_rotate(current)

        if self.get_balance(current) <= -2:
            child = current.left
            if self.get_height(child.right) > self.get_height(child.left):
                current.left = self.left_rotate(child)
            return self.right_rotate(current)

        return current

    def kth_largest(self, k: int) -> AVLTreeNode:
        """
        Returns the kth largest element in the tree using reverse inorder traversal.
        k=1 would return the largest.
        Best Case time complexity: O(1)
        Worst Case time complexity: O(k)
        """
        count = 0

        # Finding kth_largest using accumulator
        self.kth_largest_aux(k, count, self.root)

        # Returns the kth largest element
        return self.kth

    def kth_largest_aux(self, k: int, count: int, current: AVLTreeNode) -> int:
        """
        Returns the number of nodes that had been traversed.
        """
        if current is not None:
            if current.right is None:  # Base Case, when current.right is None (the largest node found)
                count += 1
            else:  # if current.right is not None
                count = self.kth_largest_aux(k, count, current.right)  # continue moving right
            if count == k:  # when the kth largest node found
                self.kth = current  # initialise class variable self.kth as the current node
                return count + 1
            elif count < k:  # continue searching by checking the left child node
                if current.left is None:
                    return count + 1
                else:  # if the left child node is not None
                    return self.kth_largest_aux(k, count, current.left)  # move left
            else:  # if count > k, return count
                return count
