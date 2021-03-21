import atexit
import grpc
import json
import logging
import os
import psycopg2

from concurrent import futures
from typing import Dict
from typing import List
from typing import Tuple


import sql_pb2
import sql_pb2_grpc
import sql_write_pb2
import sql_write_pb2_grpc


name: str = 'SQLWrite'
v: str = 'v2'

env_json_file: str = os.path.abspath('./env.json')

lingo = None
log = None

env = {}
env_list: List[str] = [
    "PORT",
    "PG_PORT",
    "PG_HOST",
    "PG_USER",
    "PG_PASS",
    "PG_DB"
]


def get(key: str) -> str:
    global env
    return env[key]


def init_sql() -> None:
    db: str = get('PG_DB')
    usr: str = get('PG_USER')
    host: str = get('PG_HOST')
    port: str = get('PG_PORT')
    pss: str = get('PG_PASS')

    global conn
    conn = psycopg2.connect(database=db,
                            user=usr,
                            password=pss,
                            host=host,
                            port=port)

    log.info('Successfully connected to db')


def init_env() -> None:
    for e in env_list:
        if e in env:
            msg: str = 'Found env var "%s" in file with default value "%s"'
            log.info(msg, e, get(e))
        else:
            env[e] = os.environ[e]
            log.info('Found env var "%s" with value "%s"', e, env[e])


def init_atexit() -> None:
    def end():
        log.info('bye')

    atexit.register(end)


def init_log() -> None:
    global log
    global name
    global v

    logging.basicConfig(
        format=f'[{v}] [{name}] %(asctime)s %(levelname)-8s %(message)s',
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S')

    log = logging.getLogger(name)
    log.info('hi')


def init_server() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    sql_write_pb2_grpc.add_SQLWriteServicer_to_server(Server(), server)
    port = get('PORT')
    server.add_insecure_port(f'localhost:{port}')

    server.start()
    log.info('Started server at %s', port)
    server.wait_for_termination()

    log.info('Ending server')


def init_json() -> None:
    global env

    try:
        json_file = open(env_json_file, 'r')
        env = json.load(json_file)
    except FileNotFoundError as fe:
        log.warning('Did not find env json file - using env vars')


class Server(sql_write_pb2_grpc.SQLWriteServicer):
    insert_1: str = 'INSERT INTO duolingo.data.users '
    insert_2: str = '(username) VALUES (%s) ON CONFLICT DO NOTHING'
    insert: str = insert_1 + insert_2

    @staticmethod
    def write_users(users: List[str]) -> None:
        curr = conn.cursor()

        for usr in users:
            curr.execute(Server.insert, [usr])

        conn.commit()
        curr.close()

    def WriteUsers(self, request, context):
        users: List[str] = request.names
        log.info('Received request to write users:')
        log.info(users)
        Server.write_users(users)

        return sql_pb2.Ack(msg=True)


def init() -> None:
    init_log()
    init_json()
    init_env()
    init_atexit()
    init_sql()
    init_server()


def main() -> None:
    init()


if __name__ == '__main__':
    main()
