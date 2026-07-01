import queue;

class Engine():

    # -> Metodo constructor
    # -> Atr ``
    def __init__(self):
        self.task_queue = queue.PriorityQueue()
        self.active_workers = []
        self.is_running = False
