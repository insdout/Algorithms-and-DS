# You are tasked with developing a movie recommendation system.
# You are given a list of movies (their names) and a list of similarities between movies
# (pairs of movies that are similar). You are also given a list of user's friends,
# and for each friend a list of movies that he has already seen.
#
# Your system should recommend one movie with the highest discussability and uniqueness.
# Discussability is the number of friends of user, who have already seen that movie.
# Uniqueness is 1 divided by the mean number of similar movies that user's friends have already seen.
# So you should return the film with the highest number: F / S,
# where F = number of friends who have seen this movie,
# and S = mean of number of similar movies seen for each friend.
# Exclude the movies with S = 0.
#
# If (a, b) and (b, c) are pairs of similar movies, then (a, c) is a pair of similar movies too.
# Each movie is not counted in its Uniqueness.
#
# Input example.
# Basically it is up to you to come up with data structure you like or you think easy to work with.
# In a nutshell you have as an input these parameters (they can be in form of a list/dict etc):
#
# With discussability it is easy.
# Discussability is the number of friends of user, who have already seen that movie. We will have:
#
#     Joker - 4
#     1917 - 2
#     Parasite - 1
#     Jojo Rabbit - 1
#     Ford v Ferrari - 0
#
# Now let's go with uniqueness. Uniqueness is 1 divided by the mean number of similar movies
# that the user's friends have already seen. Similar movies have transitive property:
# if movie 1 is similar to movie 2 and movie 2 is similar to movie 3 -> movie 1 is similar to movie 3 and vice versa.
#
# Let's breakdown how many similar movies each movie has:
#
#     Joker - 1 (Ford v Ferrari)
#     1917 - 2 (Parasite, Jojo Rabbit)
#     Parasite - 2 (1917, Jojo Rabbit)
#     Jojo Rabbit - 2 (Parasite, 1917)
#     Ford v Ferrari - 1 (Joker)
#
# Okay, let's count for each movie how many friends seen similar movies.
#
#     Joker - 0 (None saw Ford v Ferrari)
#     1917 - 1 (Parasite), 1 (Jojo Rabbit)
#     Parasite - 2 (1917) , 1 (Jojo Rabbit)
#     Jojo Rabbit - 1 (Parasite), 2 (1917)
#     Ford v Ferrari - 4 (Joker)
#
#  Let's find mean values:
#
#     Joker - mean(0) = 0
#     1917 - mean(1,1) = 1
#     Parasite - mean(2 ,1) = 1.5
#     Jojo Rabbit - mean(1,2) = 1.5
#     Ford v Ferrari - mean(4) = 4
#
# In the end we need to return movie with highest score which is calculated like this: F/S,
# where F = number of friends who have seen this movie (discussability),
# and S = mean of the number of similar movies seen for each friend (uniqueness).
# Let's find out what movie should we recommend:
#
#     Joker - 4/0 = 0
#     1917 - 2/1 = 2
#     Parasite - 1/1.5 = 0.66666
#     Jojo Rabbit - 1/1.5 = 0.66666
#     Ford v Ferrari - 0/4 = 0
#
from typing import List

movies = ["Parasite", "1917", "Ford v Ferrari", "Jojo Rabbit", "Joker"]
similarities = [["Parasite", "1917"],
                ["Parasite", "Jojo Rabbit"],
                ["Joker", "Ford v Ferrari"]]
friends = [["Joker"],
            ["Joker", "1917"],
            ["Joker"],
            ["Parasite"],
            ["1917"],
            ["Jojo Rabbit", "Joker"]]


import numpy as np
from collections import Counter

# m = |movies|
# s = |similarities|
# f = |friends|

class Database:
    def __init__(self, movies, similarities):
        self.movies = movies
        self.movie_to_index = self.get_movie_to_index()                 # O(m)
        self.adjacency_list = self.get_adjacency_list(similarities)     # O(m+s)
        self.connected_components = self.get_connected_components()     # O(m+s)
        self.movie_to_component = self.get_component_assignment()       # O(m)

    def get_movie_to_index(self):                                       # O(m)
        d = {}
        for ind, movie in enumerate(self.movies):
            d[movie] = ind
        return d

    def get_adjacency_list(self, similarities):                 # Total: O(m+s)
        adj_list = [set() for _ in range(len(self.movies))]     # O(m)
        for movie1, movie2 in similarities:                     # O(s)
            ind1 = self.movie_to_index[movie1]                      # O(1)
            ind2 = self.movie_to_index[movie2]                      # O(1)
            if ind2 not in adj_list[ind1]:                          # O(1) adj_list[ind1] : set
                adj_list[ind1].add(ind2)                            # O(1) adj_list[ind1] : set
            if ind1 not in adj_list[ind2]:                          # O(1) adj_list[ind2] : set
                adj_list[ind2].add(ind1)                            # O(1) adj_list[ind2] : set
        return adj_list

    def dfs(self, node, visited):                               # O(m+s)
        # DFS implementation O(V+E)
        stack = [node]
        component = {node}
        while stack:
            node = stack.pop()
            component.update([node])
            if visited[node]:
                continue
            visited[node] = True
            for neighbour in self.adjacency_list[node]:
                if not visited[neighbour]:
                    stack.append(neighbour)
        return component, visited

    def get_connected_components(self):                             # O(m+s)
        # Находим компоненты связности
        # Для каждого непосещенного фильма запускаем DFS O(m+s)
        n = len(self.movies)
        components = []
        visited = [False for _ in range(n)]
        for ind in range(n):
            if not visited[ind]:
                component, visited = self.dfs(ind, visited)
                components.append(set(map(lambda x: self.movies[x], component)))
        return components

    def get_component_assignment(self):                                     # Total  O(m)
        assignment_dict = {}                                                # O(1)
        for ind, component in enumerate(self.connected_components):         # O(m) |U{components}| = |m|
            for movie in component:
                assignment_dict[movie] = ind
        return assignment_dict

    def count_films(self, friends):
        flat_list = []  # O(1)
        for item in friends:  # O(f)
            flat_list.extend(item)  # Тут вопрос
        d = Counter(flat_list)
        return d

    def get_discussability(self, friends):                          # Total O(f+m) ????
        # Считаем количество каждого фильма в friends O(N)
        n = len(self.movies)                                        # O(1)
        d = self.count_films(friends)                               # O(f) ???
        F = [0 for _ in range(n)]                                   # O(m)
        for ind, movie in enumerate(self.movies):                   # O(m)
            F[ind] = d.get(movie, 0)                                    # O(1)
        return F

    def get_uniqueness(self, friends):                                                      # Total O(m^2 * f)
        s = []
        for index, movie in enumerate(self.movies):                                         # O(m)
            temp = []                                                                           # O(1)
            component = self.connected_components[self.movie_to_component[movie]]               # O(m+s)
            for similar_movie in component - {movie}:                                           # O(m)
                movie_count = 0                                                                     # O(1)
                for friend_list in friends:                                                         # O(f)
                    movie_count += sum([1 for i in friend_list if i == similar_movie])                  # тут тоже вопрос
                temp.append(movie_count)                                                            # O(1)
            s.append(np.mean(temp))                                                             # O(1)
        return s

    def get_recommendation(self, friends):                                              # Total O(m^2 * f)
        f = self.get_discussability(friends)                                                # O(f+m) ????
        s = self.get_uniqueness(friends)                                                    # O(m^2 * f)
        rating = [f/s if s != 0 else 0 for f, s in zip(f, s)]                               # O(m)
        return self.movies[np.argmax(rating)]                                               # O(m)


if __name__ == "__main__":
    db = Database(movies, similarities)
    print(db.adjacency_list)
    print(movies)
    print(db.get_discussability(friends))
    print(db.connected_components)
    print(db.movie_to_component)
    print(db.get_uniqueness(friends))
    print(db.get_recommendation(friends))