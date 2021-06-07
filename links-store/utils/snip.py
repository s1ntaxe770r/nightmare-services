import redis 
from os import getenv
from typing import List


host:str =  getenv("REDIS_HOST")
port:str =  getenv("REDIS_PORT")




class Link:
    """
    Link class represents an image link 
    """
    def __init__(self,url:str) -> None:
        self.url = url
        



def add_link(link:Link) -> Link:
    """
    insert a new link into the cache 
    Input : Link
    Returns: Link
    """
    client = redis.Redis(host,port,0)
    client.rpush('links',link.url)
    return link.url


def get_links() -> List[bytes]:
    """
    Retrive all the links from the cache
    Returns: List
    """
    client = redis.Redis(host,port,0)
    links = client.lrange('links',0,-1)
    return links 



