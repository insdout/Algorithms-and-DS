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


# m = |movies|
# s = |similarities|
# f = |friends|



from collections import Counter
from numpy import argmax


class RecommenderSystem:

    def __init__(self, movies, similarities):
        self.movies = movies                                                #           type: list[str]
        self.movie_to_index = self.get_movie_to_index()                     # O(m)      type: Dict[str, int]
        self.adjacency_list = self.get_adjacency_list(similarities)         # O(m+s)    type: List[set]
        self.connected_components = self.get_connected_components()         # O(m+s)    type: List[set]
        self.movie_to_component = self.get_component_assignment()           # O(m)      type: Dict[str, int]

    def get_movie_to_index(self):                                           # Total: O(m)
        """

        :return:
        """
        d = {}                                                              # O(1)
        for ind, movie in enumerate(self.movies):                           # O(m)
            d[movie] = ind                                                      # O(1)
        return d

    def get_adjacency_list(self, similarities):                             # Total: O(m+s)
        """

        :param similarities:
        :return:
        """
        adj_list = [set() for _ in range(len(self.movies))]                 # O(m)
        for movie1, movie2 in similarities:                                 # O(s)
            try:
                ind1 = self.movie_to_index[movie1]                                  # O(1)
                ind2 = self.movie_to_index[movie2]                                  # O(1)
                if ind2 not in adj_list[ind1]:                                      # O(1) adj_list[ind1] : set
                    adj_list[ind1].add(ind2)                                        # O(1) adj_list[ind1] : set
                if ind1 not in adj_list[ind2]:                                      # O(1) adj_list[ind2] : set
                    adj_list[ind2].add(ind1)                                        # O(1) adj_list[ind2] : set
            except KeyError as err:
                err_msg = "Warning! Similar movie \"{}\" not in movies!"
                print(err_msg.format(err.args[0]))
        return adj_list

    def dfs(self, node, visited):                                           # Total: O(m+s)
        """

        :param node:
        :param visited:
        :return:
        """
        stack = [node]                                                      # O(1)
        component = {node}                                                  # O(1)
        while stack:                                                        # O(m+s) Visit vertices only once
            node = stack.pop()                                                  # O(1)
            component.update([node])                                            # O(1)
            if visited[node]:                                                   # O(1)
                continue                                                        # O(1)
            visited[node] = True                                                # O(1)
            for neighbour in self.adjacency_list[node]:                         # O(|adjacent vertices|)
                if not visited[neighbour]:                                          # O(1)
                    stack.append(neighbour)                                         # O(1)
        return component, visited

    def get_connected_components(self):                                             # Total: O(m+s)
        """

        :return:
        """
        n = len(self.movies)                                                        # O(1)
        components = []                                                             # O(1)
        visited = [False for _ in range(n)]                                         # O(m)
        for ind in range(n):                                                        # O(m)
            if not visited[ind]:                                                        # O(1)
                component, visited = self.dfs(ind, visited)                             # O(|V|+|E|) in this component
                components.append(set(map(lambda x: self.movies[x], component)))        # O(1)
        return components

    def get_component_assignment(self):                                             # Total  O(m)
        """

        :return:
        """
        assignment_dict = {}                                                        # O(1)
        for ind, component in enumerate(self.connected_components):                 # O(m) |U{components}| = |m|
            for movie in component:                                                     # O(|component|)
                assignment_dict[movie] = ind                                            # O(1)
        return assignment_dict

    def count_films(self, friends):                                                 # Total: O(f)
        """

        :param friends:
        :return:
        """
        flat_list = []                                                              # O(1)
        for item in friends:                                                        # O(f) |U{friend list}| = |f|
            flat_list.extend(item)                                                      # O(|friend list|)
        d = Counter(flat_list)                                                      # O(f)
        return d

    def get_discussability(self, friends):                                          # Total O(f+m)
        """

        :param friends:
        :return:
        """
        n = len(self.movies)                                                        # O(1)
        film_counts = self.count_films(friends)                                     # O(f)
        f = [0 for _ in range(n)]                                                   # O(m)
        for ind, movie in enumerate(self.movies):                                   # O(m)
            f[ind] = film_counts.get(movie, 0)                                      # O(1)
        return f

    def get_uniqueness(self, friends):                                                  # Total O(m+f+c)
        """

        :param friends:
        :return:
        """
        s = []                                                                          # O(1)
        film_counts = self.count_films(friends)                                         # O(f)
        component_counts = [tuple() for _ in range(len(self.connected_components))]     # O(c)
        for ind, component in enumerate(self.connected_components):                     # O(m) |U{components}| = |m|
            component_counts[ind] = (                                                       # O(1)
                sum([film_counts.get(f, 0) for f in component]),                            # O(|component|)
                len(component))                                                             # O(1)

        for index, movie in enumerate(self.movies):                                     # O(m)
            component_id = self.movie_to_component[movie]                                   # O(1)
            component_sum, cardinality = component_counts[component_id]                     # O(1)
            s.append((component_sum - film_counts[movie])/(cardinality-1)                   # O(1)
                     if cardinality > 1 else 0)
        return s

    def get_recommendation(self, friends):                                              # Total O(f+m)
        """

        :param friends:
        :return:
        """
        f = self.get_discussability(friends)                                            # O(f+m)
        s = self.get_uniqueness(friends)                                                # O(m)
        rating = [f / s if s != 0 else 0 for f, s in zip(f, s)]                         # O(m)
        print(rating)
        return self.movies[argmax(rating)]                                              # O(m)


if __name__ == "__main__":
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

    rs = RecommenderSystem(movies, similarities)
    print(rs.adjacency_list)
    print(movies)
    print(rs.get_discussability(friends))
    print(rs.connected_components)
    print(rs.movie_to_component)
    print(rs.get_uniqueness(friends))
    print(rs.get_recommendation(friends))

    movies = ["Parasite", "1917", "Ford v Ferrari", "Jojo Rabbit", "Joker", "Alien"]
    similarities = [["Parasite", "1917"],
                    ["Parasite", "Jojo Rabbit"],
                    ["Joker", "Ford v Ferrari"]]
    friends = [["Joker", "Parasite"],
               ["Joker", "1917"],
               ["Joker", "Parasite", "Alien"],
               ["Parasite"],
               ["1917","Parasite"],
               ["Jojo Rabbit", "Joker"]]

    rs = RecommenderSystem(movies, similarities)
    print(rs.adjacency_list)
    print(movies)
    print(rs.get_discussability(friends))
    print(rs.connected_components)
    print(rs.movie_to_component)
    print(rs.get_uniqueness(friends))
    print(rs.get_recommendation(friends))
