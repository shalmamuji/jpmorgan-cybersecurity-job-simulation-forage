from collections import OrderedDict

class RolesCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.roles = OrderedDict()  # Using OrderedDict to maintain insertion order

    def get(self, role):
        # Returns the message corresponding to the last invocation of that role,
        # None if the role does not exist in the cache.
        return self.roles.get(role)

    def Set(self, role, message):
        # Adds the role and its corresponding message to the cache.
        # If the role already exists, only the message is updated.
        # Otherwise, the oldest role is removed to make space.
        if role in self.roles:
            del self.roles[role]
        elif len(self.roles) >= self.capacity:
            self.roles.popitem(last=False)  # Remove the oldest role
        self.roles[role] = message

    def _complexity(self):
        # Runtime complexity: O(1) for get and set methods
        # Space complexity: O(capacity)
        return {
            'get': 'O(1)',
            'set': 'O(1)',
            'space': f'O({self.capacity})'
        }

# Sample usage
cache = RolesCache(3)
cache.Set('Admin', 'Admin role used for system administration')
cache.Set('User', 'User role used for general access')
cache.Set('Guest', 'Guest role used for limited access')
print(cache.get('Admin'))  # Output: Admin role used for system administration
print(cache.get('User'))   # Output: User role used for general access
print(cache.get('Guest'))  # Output: Guest role used for limited access

cache.Set('Guest', 'Updated guest role message')
print(cache.get('Guest'))  # Output: Updated guest role message

cache.Set('Superuser', 'Superuser role used for privileged access')
print(cache.get('Admin'))  # Output: None (Admin role is removed due to capacity limit)
