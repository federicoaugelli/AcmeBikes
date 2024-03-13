#Successful order
order = {
            "customer": "luca",
            "address": "via ercolani 1, Bologna",
            "bikes": [
                {
                    "productId": 4123,
                    "qty": 1,
                    "components": [
                        {
                            "productId": 5192,
                            "qty": 1
                        },
                        {
                            "productId": 6532,
                            "qty": 1
                        }
                    ]
                },
            ]
        }


#Unsuccessful order
order = {
            "customer": "luca",
            "address": "via ercolani 1, Bologna",
            "bikes": [
                {
                    "productId": 5623,
                    "qty": 1,
                    "components": [
                        {
                            "productId": 8723,
                            "qty": 1
                        },
                        {
                            "productId": 3251,
                            "qty": 1
                        }
                    ]
                },
            ]
        }


#Token refused
order = {
            "customer": "Mario Rossi",
            "address": "via ercolani 1, Bologna",
            "bikes": [
                {
                    "productId": 4123,
                    "qty": 1,
                    "components": [
                        {
                            "productId": 5192,
                            "qty": 1
                        },
                        {
                            "productId": 6532,
                            "qty": 1
                        }
                    ]
                },
            ]
        }
       
