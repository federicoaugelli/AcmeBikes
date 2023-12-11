from worker import Worker
from verify_customisation import verify_customisation
from notify_client import cancel_order
from verify_availability import verify_availability
from create_order import create_order
from send_quote import send_quote
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
        variables=["process_instance_id", "process_dict"]
    )

    worker.subscribe(
        topic='verify_customisation',
        func=verify_customisation,
        variables=["process_instance_id", "process_dict"])

    worker.subscribe(
        topic='notify_client',
        func=cancel_order,
        variables=["process_instance_id", "process_dict"])
    
    worker.subscribe(
        topic='verify_availability',
        func=verify_availability,
        variables=["process_instance_id", "process_dict"])
    worker.subscribe(
        topic='create_order',
        func=create_order,
        variables=["process_instance_id", "process_dict"])
    worker.subscribe(
        topic='send_quote',
        func=send_quote,
        variables=["process_instance_id", "process_dict", "discount"])
    worker.run()
