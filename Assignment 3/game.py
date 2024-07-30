from __future__ import annotations
# ^ In case you aren't on Python 3.10

from random_gen import RandomGen
from potion import Potion
from avl import AVLTree
from hash_table import LinearProbePotionTable
from array_sorted_list import ArraySortedList


class Game:

    def __init__(self, seed=0) -> None:
        self.rand = RandomGen(seed)
        self.inventory_tree = AVLTree()
        self.option_tree = AVLTree()
        self.vendors = None

    def set_total_potion_data(self, potion_data: list) -> None:
        linear_probe_data = LinearProbePotionTable(len(potion_data), True, len(potion_data))
        for i in range(len(potion_data)):
            # Creating empty potion
            p = Potion.create_empty(potion_data[i][1], potion_data[i][0], potion_data[i][2])
            # Hash each potion in the potion_data and store them into a hash table
            linear_probe_data.__setitem__(p.name, p)
            # Get the position of each potion in the potion_data
            pos = linear_probe_data.get_pos(p.name)
            # and store them into an AVL Tree
            self.inventory_tree.__setitem__(pos, p)

    def add_potions_to_inventory(self, potion_name_amount_pairs: list[tuple[str, float]]) -> None:
        """
        Add the potions into inventory by setting their quantity
        Time Complexity: O(C x log(n))
        Since AVL Tree is a self-balancing Binary Search Tree
        and a balanced Binary Search Tree has a time complexity of O(log(n)) when searching,
        the time complexity of this function will be O(C x log(n)), where C is the number of potions to be added
        """
        linear_probe_pairs = LinearProbePotionTable(len(potion_name_amount_pairs), True, len(potion_name_amount_pairs))
        for i in range(len(potion_name_amount_pairs)):
            # Hash each potion in the potion_name_amount_pairs
            key = linear_probe_pairs.hash(potion_name_amount_pairs[i][0])
            # If the item exists in the AVL Tree
            if self.inventory_tree.__getitem__(key):
                # Set the potion's quantity
                p = self.inventory_tree.__getitem__(key)
                p.quantity = potion_name_amount_pairs[i][1]
                # Add this potion as an option to be chosen later
                self.option_tree.__setitem__(p.buy_price, p)

    def choose_potions_for_vendors(self, num_vendors: int) -> list:
        if num_vendors <= 0:
            raise Exception("num_vendors is a positive integer")
        result_list = []
        chosen_potions_list = []

        linear_probe_vendors = LinearProbePotionTable(self.option_tree.__len__(), True, self.option_tree.__len__())
        for _ in range(num_vendors):
            p = self.rand.randint(
                self.option_tree.__len__())  # random number between 1 to C (number of potions in inventory (tree))
            potion = self.option_tree.kth_largest(p).item  # p^th most expensive potion
            result_list.append((potion.name, potion.quantity))  # add this potion to result_list

            # temporarily remove from inventory (tree) so that it does not appear again
            chosen_potions_list.append(potion)
            key = linear_probe_vendors.hash(potion.name)
            self.option_tree.__delitem__(key)

        # adding back to inventory
        for i in range(num_vendors):
            self.option_tree.__setitem__()
        self.vendors = result_list

        return self.vendors

    def solve_game(self, potion_valuations: list[tuple[str, float]], starting_money: list[int]) -> list[float]:

        """

        if The number of potion that can be purchased by starting money is < 2   #if starting money can only buy one potion
            use all staring money to buy as much as it can buy that potion and then calculate the total profit
        else
             find the potion which have most net profit and buy it  # for example if full_vendor_info = [(“Potion of Health Regeneration”, 30),(“Potion of Extreme Speed”, 15)]
                                                                    #and G.set_total_potion_data([[“Potion of Health Regeneration”, “Health”, 20],[“Potion of Extreme Speed”, “Buff”, 10]])
                                                                    #for each litre Health Regeneration can earn 10$ but Extreme Speed can only earn 5$
                if money left > 0                 #if the money still left after buy one of the potion
                    find the potion which have second most net profit and buy it and calculate total profit   #if Health Regeneration sold out buy Extreme Speed
                else
                    calculate total profit


        """

        """
        Solve game works by first iterating over the potion_valuation argument to obtain the potion information and buy price. With this information
        the ratio between the sell and buy price is found. This is then stores in a sorted list from smallest to largest ratio value. Then the maximum ratio is_empty
        """
        sorted_list = ArraySortedList(len(potion_valuations))
        revenue_list = []  # stores total money made with each starting_money

        for i in potion_valuations:
            potion_info = self.potions[i][0]
            buy_price = potion_info.buy_price
            if buy_price in self.inventory_tree:
                ratio = i[1] / buy_price  # gives desired ratio
                game_econ = (ratio, buy_price, i[1])
                sorted_list.add(game_econ)
            else:
                raise Exception("Potion is not for sale today")

        for i in starting_money:
            count = 0
            income = 0
            for j in sorted_list:
                if i == 0:  # if no money remains, loop breaks
                    break
                transaction = sorted_list[(len(sorted_list) - 1 - count)]  # accessing largest value
                # getting corresponding buy and sell price
                buy_price = transaction[1]
                sell_price = transaction[2]
                affordable_potions = i / buy_price  # find all of what can be bought
                vendor_potion = self.inventory_tree[buy_price]

                if affordable_potions > vendor_potion.quantity:  # if the most expensive can be bought move on to next highest
                    i -= (buy_price * vendor_potion.quantity)  # updating money remaining
                    income += vendor_potion.quantity * sell_price
                else:  # case where all money is spent on first potion
                    # Take cost from money should be 0
                    i -= affordable_potions * buy_price
                    income += affordable_potions * sell_price
                count += 1
            # adds remaining money incase all potions are bought and there is still money left over
            income += i
            revenue_list.append(income)

        return revenue_list
