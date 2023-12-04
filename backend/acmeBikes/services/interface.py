from worker import Worker
from verify_customisation import verify_customisation
from cancel_order import cancel_order
from verify_availability import verify_availability
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

    worker.subscribe(
        topic='verify_customisation',
        func=verify_customisation,
        variables=['customisation_accepted'])

    worker.subscribe(
        topic='cancel_order',
        func=cancel_order,
        variables=['message'])
    
    worker.subscribe(
        topic='verify_availability',
        func=verify_availability,
        variables=['preventivo'])
    worker.run()