import random
from util import Queue

def shuffle_array(array):
    for i in range(0, len(array)):
        rand_index = random.randint(i,len(array)-1)
        array[rand_index], array[i] = array[i], array[rand_index]

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # !!!! IMPLEMENT ME
        # Add users
        possible_friendships = []
        i=1
        while i < num_users+1:
            #print("USER", i)
            self.add_user(i)
            j=i
            while j < num_users+1:
                if j!=i:
                    possible_friendships.append((i,j))
                j+=1
            i+=1
        
        shuffle_array(possible_friendships)
        total_connections = int(num_users*avg_friendships/2)
        random_friendships= possible_friendships[:total_connections]
        for friend_tuple in random_friendships:
            #print(f"friend_tuple[0]: {friend_tuple[0]}, friend_tuple[1]: {friend_tuple[1]}")
            self.add_friendship(friend_tuple[0], friend_tuple[1])
            

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        #print("get_all friendships", self.friendships[1])
        queue = Queue()
        queue.enqueue([user_id])
        while queue.size() > 0:
            path = queue.dequeue()
            #print("PATH", path)
            vertex = path[-1]
            if vertex not in visited:
                visited[vertex] = path
                for next_vertex in self.friendships[vertex]:
                    if next_vertex not in path:
                        new_path = list(path)
                        new_path.append(next_vertex)
                        queue.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("friendships", sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
