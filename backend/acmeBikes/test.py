from worker import Worker

def test_function():
    print('ciao')
    return {}


if __name__ == '__main__':
    print("ACMEManager Camunda Server started.")
    url = 'http://localhost:8080/engine-rest'
    worker_id = '1'
    worker = Worker(url=url, worker_id=worker_id)
    # I Topic vengono assegnati al worker
    worker.subscribe(
        topic='test_external_task',
        func=test_function,
        variables=[]
    )

    worker.run()
