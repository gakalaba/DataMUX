def schedule(jobs, cluster):
    '''
    Given a configuration of nodes over which all models are distributed
    M := memory budget of smallest node on a path
    Sort queue by latency tiers
    Within each latency tier, sort by accuracy
        For each (latency, accuracy) group:
            batch_size = M/avg_size_of_request
            multiplex_size = f(accuracy, model, mx_layer)
            Dequeue multiplex_size*batch_size
            If multiplex_size*batch_size > group_size then dequeue from next group
    '''
    jobs.sort(latency)
    jobs.sort(accuracy)
    while (True):
        job = jobs.peak()




# config file

class Queue:
    def __init__(self, config):
        self.config = config
    def parse(config):
        # parse the config

def main():
    jobs = create_jobs(config)
    jobs = queue()

