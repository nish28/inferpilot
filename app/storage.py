REQUESTS = []


def save_request(data: dict):
    REQUESTS.append(data)



def get_requests(limit: int = 10):
    return REQUESTS[-limit:]
