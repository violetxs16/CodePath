#Problem 2: Queue of Performance Requests
#You are organizing a festival and want to manage the queue of requests to perform. 
# Each request has a priority. Use a queue to process the performance requests in the 
# order they arrive but ensure that requests with higher priorities are processed before 
# those with lower priorities. Return the order in which performances are processed.

def process_performance_requests(requests):
    requests.sort(reverse = True)
    val = []
    for key, value in requests:
        val.append(value)
    return val 
#Example Usage:

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))
#Understand: We will assume that the higher the num the higher priority
#Implement: sort the list, return the string in a list