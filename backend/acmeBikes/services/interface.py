from worker import Worker
from verify_customisation import verify_customisation
from notify_client import notify_client
from verify_availability import verify_availability
from create_order import create_order
from send_quote import send_quote
from send_accept_quote import send_accept_quote
from cancel_order import cancel_order
from prepayment import prepayment
from verify_prepayment import verify_prepayment
from token_accepted import token_accepted
from token_refused import token_refused
from create_list import create_list
from send_bicycle import send_bicycle
from payment import payment

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
        variables=["process_instance_id", "process_dict", "order"])

    worker.subscribe(
        topic='notify_client',
        func=notify_client,
        variables=["process_instance_id", "process_dict"])
    
    worker.subscribe(
        topic='verify_availability',
        func=verify_availability,
        variables=["process_instance_id", "process_dict", "orderId", "order"])
    worker.subscribe(
        topic='create_order',
        func=create_order,
        variables=["process_instance_id", "process_dict"])
    worker.subscribe(
        topic='send_quote',
        func=send_quote,
        variables=["process_instance_id", "process_dict", "orderId"])
    worker.subscribe(
        topic='send_accept_quote',
        func=send_accept_quote,
        variables=["process_instance_id", "process_dict"])
    worker.subscribe(
        topic='cancel_order',
        func=cancel_order,
        variables=["process_instance_id", "process_dict", "orderId"])
    worker.subscribe(
        topic='prepayment',
        func=prepayment,
        variables=["process_instance_id", "process_dict", "order"])
    worker.subscribe(
        topic='verify_prepayment',
        func=verify_prepayment,
        variables=["process_instance_id", "process_dict", "pre_payment_token", "pre_payment_amount"])
    worker.subscribe(
        topic='token_accepted',
        func=token_accepted,
        variables=["process_instance_id", "process_dict"])
    worker.subscribe(
        topic='token_refused',
        func=token_refused,
        variables=["process_instance_id", "process_dict"])
    worker.subscribe(
        topic='create_list',
        func=create_list,
        variables=["process_instance_id", "process_dict", "orderId"])
    worker.subscribe(
        topic='send_bicycle',
        func=send_bicycle,
        variables=["process_instance_id", "process_dict"])
    worker.subscribe(
        topic='payment',
        func=payment,
        variables=["process_instance_id", "process_dict"])
    
    worker.run()
