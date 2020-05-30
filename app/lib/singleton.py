import threading


class SingletonMetaClass(type):
    """
    Meta class that encompasses all the singleton objects in the current process memory space.
    Checks if an instance of te object already exists and returns it. If it does not exist, a new
    object is created and set in the internal map.
    """
    _instance_map = {}
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance_map:
            with cls._instance_lock:
                # It is possible that the another thread created an instance just before the lock is
                # acquired.
                if cls not in cls._instance_map:
                    cls._instance_map[cls] = super(SingletonMetaClass, cls).__call__(
                        cls, *args, **kwargs
                    )
        return cls._instance_map[cls]
