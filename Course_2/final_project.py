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


# m = total number of movies
# s = total number of similarities
# f = number of friends
# v = total number of films in friends

from numpy import argmax


class RecommenderSystem:

    def __init__(self, movies, similarities):
        self.movies = movies                                                         #           type: list[str]
        self.movie_to_index = self._get_movie_to_index()                             # O(m)      type: Dict[str, int]
        self.connected_components = self._get_connected_components(similarities)     # O(m+s)    type: List[set]
        self.movie_to_component = self._get_component_assignment()                   # O(m)      type: Dict[str, int]

    def _get_movie_to_index(self):                                                   # Total: O(m)
        """
        Creates dictionary to map movie title to index.
        :return:  dict[str, int]
        """
        d = {}                                                              # O(1)
        for ind, movie in enumerate(self.movies):                           # O(m)
            d[movie] = ind                                                      # O(1)
        return d

    def _get_adjacency_list(self, similarities):                             # Total: O(m+s)
        """
        Creates adjacency lis from list of similarities.
        We add only edges in similarities: total 2*|S|,
        twice as the graph is undirected.
        :param similarities:  list[list[str]]
        :return:  list[set]
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

    def _dfs(self, node, visited, adjacency_list):                           # Total: O(m+s)
        """
        Performs DFS starting from given node.
        Visit all vertices in current connected component and returns
        set of vertices in component and updates visited list.
        :param node: int
        :param visited:  list[bool]
        :param adjacency_list: list[set]
        :return: tuple(set(), list[bool])
        """
        stack = [node]                                                      # O(1)
        component = {node}                                                  # O(1)
        while stack:                                                        # O(m+s) Visit vertices only once
            node = stack.pop()                                                  # O(1)
            component.update([node])                                            # O(1)
            if visited[node]:                                                   # O(1)
                continue                                                        # O(1)
            visited[node] = True                                                # O(1)
            for neighbour in adjacency_list[node]:                              # O(|adjacent vertices|)
                if not visited[neighbour]:                                          # O(1)
                    stack.append(neighbour)                                         # O(1)
        return component, visited

    def _get_connected_components(self, similarities):                               # Total: O(m+s)
        """
        Performs DFS on all unvisited vertices, updating the
        list of connected components.

        :param similarities: list[list[str]]
        :return:  list[set[str]] list of sets of vertices in each component
        """
        n = len(self.movies)                                                        # O(1)
        adjacency_list = self._get_adjacency_list(similarities)
        components = []                                                             # O(1)
        visited = [False for _ in range(n)]                                         # O(m)
        for ind in range(n):                                                        # O(m)
            if not visited[ind]:                                                        # O(1)
                component, visited = self._dfs(ind, visited, adjacency_list)             # O(|V|+|E|) in this component
                components.append(set(map(lambda x: self.movies[x], component)))        # O(1)
        return components

    def _get_component_assignment(self):                                             # Total  O(m)
        """
        Creates a dictionary which maps movie title to connected
        component index.

        :return:  dict[str, int]
        """
        assignment_dict = {}                                                        # O(1)
        for ind, component in enumerate(self.connected_components):                 # O(m) |U{components}| = |m|
            for movie in component:                                                     # O(|component|)
                assignment_dict[movie] = ind                                            # O(1)
        return assignment_dict

    def _count_films(self, friends):                                                 # Total: O(f)
        """
        Iterates through two-dimensional list of similarities
        and counts frequencies of films in list.

        :param friends:  list[list[str]]
        :return:  dict[str, int]
        """
        d = {}
        for watched_list in friends:                                                # O(f) |U{friend list}| = |f|
            for movie in watched_list:                                              # O(|friend list|)
                d[movie] = d.get(movie, 0) + 1                                          # O(1)
        return d

    def get_discussability(self, friends):                                          # Total O(f+m)
        """
        Calculates discussability by calculating film frequencies
        in friends and assigning each film index its frequency.

        :param friends: list[list[str]]
        :return: list[int]
        """
        n = len(self.movies)                                                        # O(1)
        film_counts = self._count_films(friends)                                    # O(f)
        f = [0 for _ in range(n)]                                                   # O(m)
        for ind, movie in enumerate(self.movies):                                   # O(m)
            f[ind] = film_counts.get(movie, 0)                                      # O(1)
        return f

    def get_uniqueness(self, friends):                                                  # Total O(m+f)
        """
        Calculates uniqueness by calculating sum of film frequencies
        in friends for every component.
        In component_counts it stores sum of frequencies of films from this component
        and cardinality of each component.

        uniqueness[movie] =
        =(sum of component film frequencies - frequency[movie])
        /(cardinality[component] - 1)

        In case of cardinality == 1, we have single film in component, uniqueness
        can't be determined - 0 is assigned.

        :param friends: list[list[str]]
        :return: list[int]
        """
        s = []                                                                          # O(1)
        film_counts = self._count_films(friends)                                        # O(f)
        component_counts = [tuple() for _ in range(len(self.connected_components))]     # O(m)
        for ind, component in enumerate(self.connected_components):                     # O(m) |U{components}| = |m|
            component_counts[ind] = (                                                       # O(1)
                sum([film_counts.get(f, 0) for f in component]),                            # O(|component|)
                len(component))                                                             # O(1)

        for index, movie in enumerate(self.movies):                                     # O(m)
            component_id = self.movie_to_component[movie]                                   # O(1)
            component_sum, cardinality = component_counts[component_id]                     # O(1)
            s.append((component_sum - film_counts.get(movie, 0))/(cardinality-1)                   # O(1)
                     if cardinality > 1 else 0)
        return s

    def get_recommendation(self, friends):                                              # Total O(f+m+s)
        """
        Calculates ratings of films.
        If uniqueness == 0, rating is 0.
        Returns the film with the highest rating.
        :param friends: list[list[str]]
        :return: str
        """
        f = self.get_discussability(friends)                                            # O(f+m)
        s = self.get_uniqueness(friends)                                                # O(m) + O(m+s) to get components
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
    print(movies)
    print(rs.connected_components)
    print(rs.movie_to_component)
    print(rs.get_discussability(friends))
    print(rs.get_uniqueness(friends))
    print(rs.get_recommendation(friends))

    movies = ["Parasite", "1917", "Ford v Ferrari", "Jojo Rabbit", "Joker", "Alien"]
    similarities = [["Parasite", "1917"],
                    ["Ford v Ferrari", "Jojo Rabbit"],
                    ["Joker", "Ford v Ferrari"],
                    ["Joker", "Alien"]]
    friends = [["Joker", "Parasite"],
               ["Joker", "1917"],
               ["Joker", "Alien", "Ford v Ferrari"]]

    rs = RecommenderSystem(movies, similarities)
    print(movies)
    print(rs.connected_components)
    print(rs.movie_to_component)
    print(rs.get_discussability(friends))
    print(rs.get_uniqueness(friends))
    print(rs.get_recommendation(friends))

    movies = ["Parasite", "1917", "Ford v Ferrari", "Jojo Rabbit", "Joker", "Alien"]
    similarities = [["Joker", "1917"]]
    friends = [["Joker", "Parasite"],
               ["Joker", "1917"],
               ["Joker", "Alien", "Ford v Ferrari"]]

    rs = RecommenderSystem(movies, similarities)
    print(movies)
    print(rs.connected_components)
    print(rs.movie_to_component)
    print(rs.get_discussability(friends))
    print(rs.get_uniqueness(friends))
    print(rs.get_recommendation(friends))
